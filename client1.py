import socket  # Importation de la bibliothèque socket pour gérer la communication réseau

# Fonction pour afficher le message de bienvenue
def display_welcome_message():
    print("""
 _______  _______  ___      __   __  _______  _______  _______  __   __ 
|       ||       ||   |    |  | |  ||       ||       ||       ||  | |  |
|    _  ||   _   ||   |    |  |_|  ||_     _||    ___||       ||  |_|  |
|   |_| ||  | |  ||   |    |       |  |   |  |   |___ |       ||       |
|    ___||  |_|  ||   |___ |_     _|  |   |  |    ___||      _||       |
|   |    |       ||       |  |   |    |   |  |   |___ |     |_ |   _   |
|___|    |_______||_______|  |___|    |___|  |_______||_______||__| |__|
    """)
    print("Bienvenue au jeu de Pierre-Feuille-Ciseaux !")

# Fonction pour afficher le résultat d'un round
def display_round_result(result):
    print("\n=============================================")
    print(f"Résultat du round : {result}")
    print("=============================================\n")

# Fonction pour afficher le résultat final après 5 rounds
def display_final_result(final_result):
    if "Joueur 1 est le gagnant" in final_result:
        print("""

 __ __  ____    __  ______   ___  ____  ____     ___ 
|  |  ||    |  /  ]|      | /   \|    ||    \   /  _]
|  |  | |  |  /  / |      ||     ||  | |  D  ) /  [_ 
|  |  | |  | /  /  |_|  |_||  O  ||  | |    / |    _]
|  :  | |  |/   \_   |  |  |     ||  | |    \ |   [_ 
 \   /  |  |\     |  |  |  |     ||  | |  .  \|     |
  \_/  |____|\____|  |__|   \___/|____||__|\_||_____|
                                                     
  
        """)
    elif "Joueur 2 est le gagnant" in final_result:
        print("""

 ___      ___  _____   ____  ____  ______    ___ 
|   \    /  _]|     | /    ||    ||      |  /  _]
|    \  /  [_ |   __||  o  | |  | |      | /  [_ 
|  D  ||    _]|  |_  |     | |  | |_|  |_||    _]
|     ||   [_ |   _] |  _  | |  |   |  |  |   [_ 
|     ||     ||  |   |  |  | |  |   |  |  |     |
|_____||_____||__|   |__|__||____|  |__|  |_____|
                                                 

        """)
    else:
        print("""

   ___   ____   ____  _      ____  ______    ___ 
  /  _] /    | /    || |    |    ||      |  /  _]
 /  [_ |   __||  o  || |     |  | |      | /  [_ 
|    _]|  |  ||     || |___  |  | |_|  |_||    _]
|   [_ |  |_ ||  _  ||     | |  |   |  |  |   [_ 
|     ||     ||  |  ||     | |  |   |  |  |     |
|_____||___,_||__|__||_____||____|  |__|  |_____|
                                                 

        """)

# Fonction principale pour exécuter le client du jeu
def main():
    HOST = '127.0.0.1'  # Adresse IP du serveur
    PORT = 5000  # Port du serveur

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Création du socket UDP du client
    server_address = (HOST, PORT)  # Définition de l'adresse et du port du serveur

    display_welcome_message()  # Affichage du message de bienvenue

    rounds = 0  # Initialisation du compteur de rounds

    valid_choices = ['pierre', 'feuille', 'ciseau']  # Liste des choix valides

    while rounds < 5:  # Boucle pour jouer 5 rounds
        while True:
            # Demande à l'utilisateur de saisir son choix
            choice = input(f"Round {rounds + 1}, entrez votre choix (pierre, feuille, ciseau): ").strip().lower()
            print("\n")

            if choice in valid_choices:#si le choix est dans les choix valide
                break#on arrete
            else:
                print("=============================================")
                print("Choix invalide. Veuillez entrer 'pierre', 'feuille' ou 'ciseau'.")#sinon un message d'erreur
                print("=============================================")

        client_socket.sendto(choice.encode(), server_address)  # Envoi du choix au serveur

        data, _ = client_socket.recvfrom(1024)  # Réception du résultat du round depuis le serveur
        display_round_result(data.decode())  # Affichage du résultat du round
        rounds += 1  # Incrémentation du compteur de rounds

    data, _ = client_socket.recvfrom(1024)
    display_final_result(data.decode())  # Affichage du résultat final

    client_socket.close()  # Fermeture du socket client

# Point d'entrée du script
if __name__ == "__main__":
    main()  # Appel de la fonction principale
