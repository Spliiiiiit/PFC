import socket  # Importation de la bibliothèque socket pour gérer la communication réseau

# Fonction pour déterminer le gagnant d'un round en fonction des choix des joueurs
def determine_winner(choice1, choice2):
    # Dictionnaire des résultats possibles pour chaque combinaison de choix
    outcomes = {
        'pierre': {'pierre': 'Égalité', 'feuille': 'Joueur 2 gagne', 'ciseau': 'Joueur 1 gagne'},
        'feuille': {'pierre': 'Joueur 1 gagne', 'feuille': 'Égalité', 'ciseau': 'Joueur 2 gagne'}, #cas spéciaux pour savoir qui gagne
        'ciseau': {'pierre': 'Joueur 2 gagne', 'feuille': 'Joueur 1 gagne', 'ciseau': 'Égalité'},
    }
    return outcomes[choice1][choice2]  # Retourne le résultat en fonction des choix des joueurs

# Fonction pour mettre à jour les scores en fonction du résultat d'un round
def update_scores(result, scores):
    if result == 'Joueur 1 gagne':  # Si le joueur 1 gagne
        scores['Joueur 1'] += 1  # Incrémenter le score du joueur 1
    elif result == 'Joueur 2 gagne':  # Si le joueur 2 gagne
        scores['Joueur 2'] += 1  # Incrémenter le score du joueur 2

# Fonction pour déterminer le gagnant final après 5 rounds
def determine_final_winner(scores):
    if scores['Joueur 1'] > scores['Joueur 2']:  # Si le joueur 1 a plus de points
        return 'Joueur 1 est le gagnant du Bo5'  # Le joueur 1 est le gagnant
    elif scores['Joueur 1'] < scores['Joueur 2']:  # Si le joueur 2 a plus de points
        return 'Joueur 2 est le gagnant du Bo5'  # Le joueur 2 est le gagnant
    else:  # Si les scores sont égaux
        return 'Le Bo5 est une égalité'  # Il y a égalité

# Configuration de l'adresse et du port du serveur
HOST = '127.0.0.1'  # Adresse IP locale
PORT = 5000  # Port d'écoute

# Création du socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))  # Liaison du socket à l'adresse et au port

print("Le serveur est prêt et attend des connexions...")  # Message indiquant que le serveur est prêt

# Initialisation des scores et du compteur de rounds
scores = {'Joueur 1': 0, 'Joueur 2': 0}  # Scores initiaux des joueurs
rounds = 0  # Compteur de rounds

# Variables pour stocker les choix et les adresses des joueurs
player1 = None
player2 = None

# Adresses des joueurs pour envoyer le résultat final
player1_addr = None
player2_addr = None

# Boucle principale du jeu, exécutée jusqu'à ce que 5 rounds soient joués
while rounds < 5:
    valid_choices = ['pierre', 'feuille', 'ciseau']
    while player1 is None or player2 is None:  # Attente des choix des deux joueurs
        data, addr = server_socket.recvfrom(1024)  # Réception des données des joueurs
        choice = data.decode().strip().lower()  # Convertir le choix en minuscules pour normalisation

        if choice not in valid_choices:  # Vérifier si le choix est invalide
            error_msg = "Choix invalide. Veuillez entrer 'pierre', 'feuille' ou 'ciseau'."
            server_socket.sendto(error_msg.encode(), addr)  # Envoyer le message d'erreur au client
            continue  # Demander une nouvelle entrée

        if player1 is None:  # Si le joueur 1 n'a pas encore envoyé son choix
            player1 = (choice, addr)  # Stocker le choix et l'adresse du joueur 1
            player1_addr = addr  # Enregistrer l'adresse du joueur 1
            print(f"Joueur 1 connecté de {addr} avec choix {choice}")  # Afficher le choix du joueur 1
        elif player2 is None:  # Si le joueur 2 n'a pas encore envoyé son choix
            player2 = (choice, addr)  # Stocker le choix et l'adresse du joueur 2
            player2_addr = addr  # Enregistrer l'adresse du joueur 2
            print(f"Joueur 2 connecté de {addr} avec choix {choice}")  # Afficher le choix du joueur 2

    # Déterminer le résultat du round en fonction des choix des joueurs
    result = determine_winner(player1[0], player2[0])
    update_scores(result, scores)  # Mettre à jour les scores
    print(f"Résultat du round : {result}")  # Afficher le résultat du round
    rounds += 1  # Incrémenter le compteur de rounds

    # Envoyer le résultat du round aux deux joueurs
    server_socket.sendto(result.encode(), player1[1])
    server_socket.sendto(result.encode(), player2[1])

    # Réinitialiser les choix des joueurs pour le prochain round
    player1 = player2 = None

# Déterminer le gagnant final après 5 rounds
final_result = determine_final_winner(scores)
print(final_result)  # Afficher le résultat final

# Envoyer le résultat final aux deux joueurs
server_socket.sendto(final_result.encode(), player1_addr)
server_socket.sendto(final_result.encode(), player2_addr)

server_socket.close()  # Fermer le socket du serveur
