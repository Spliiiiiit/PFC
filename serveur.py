import socket
import threading

def choix_utilisateur(conn):
    print("Attente du choix de l'utilisateur...")
    choix = conn.recv(1024).decode().lower()
    print("Choix reçu:", choix)
    while choix not in ['pierre', 'feuille', 'ciseaux']:
        conn.send("Choix invalide. Choisissez pierre, feuille ou ciseaux: ".encode())
        choix = conn.recv(1024).decode().lower()
        print("Nouveau choix reçu:", choix)
    return choix


def comparer(choix_joueur1, choix_joueur2):
    if choix_joueur1 == choix_joueur2:
        return "Égalité !"
    elif (choix_joueur1 == 'pierre' and choix_joueur2 == 'ciseaux') or \
         (choix_joueur1 == 'feuille' and choix_joueur2 == 'pierre') or \
         (choix_joueur1 == 'ciseaux' and choix_joueur2 == 'feuille'):
        return "Joueur 1 a gagné !"
    else:
        return "Joueur 2 a gagné !"

def handle_client(conn, addr, players):
    try:
        players.append(conn)
        print("Connexion ajoutée à la liste des joueurs.")

        if len(players) == 2:
            print("Deux joueurs connectés, démarrage du jeu...")
            conn1 = players[0]
            conn2 = players[1]
            print("Connexions des joueurs récupérées.")

            # Commencer le jeu
            jeu(conn1, conn2)
    except Exception as e:
        print(f"Erreur dans handle_client : {e}")

def jeu(conn1, conn2):
    try:
        print("Le jeu commence entre les joueurs.")

        score_joueur1 = 0
        score_joueur2 = 0
        while score_joueur1 < 3 and score_joueur2 < 3:
            print("Nouveau tour de jeu.")

            conn1.send("Choisissez pierre, feuille ou ciseaux: ".encode())
            joueur1 = choix_utilisateur(conn1)

            conn2.send("Choisissez pierre, feuille ou ciseaux: ".encode())
            joueur2 = choix_utilisateur(conn2)

            print(f"Joueur 1 a choisi: {joueur1}")
            print(f"Joueur 2 a choisi: {joueur2}")

            result = comparer(joueur1, joueur2)
            print(f"Résultat du tour: {result}")

            conn1.send(result.encode())
            conn2.send(result.encode())

            if "Joueur 1 a gagné" in result:
                score_joueur1 += 1
            elif "Joueur 2 a gagné" in result:
                score_joueur2 += 1

            print(f"Score actuel: Joueur 1 - {score_joueur1}, Joueur 2 - {score_joueur2}")

            score_message = f"Score: {score_joueur1} - {score_joueur2}"
            conn1.send(score_message.encode())
            conn2.send(score_message.encode())

        if score_joueur1 == 3:
            conn1.send("Vous avez gagné la BO5 !".encode())
            conn2.send("Vous avez perdu la BO5 !".encode())
        else:
            conn1.send("Vous avez perdu la BO5 !".encode())
            conn2.send("Vous avez gagné la BO5 !".encode())

        print("Le jeu est terminé.")
    except Exception as e:
        print(f"Erreur dans jeu : {e}")

def main():
    HOST = '127.0.0.1'
    PORT = 5000
    players = []

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Attente du joueur sur {HOST}:{PORT}...")
        print("Serveur en attente de connexions...")

        while True:
            conn, addr = s.accept()
            print(f"Joueur connecté: {addr}")

            threading.Thread(target=handle_client, args=(conn, addr, players)).start()
        print("Fin de la boucle principale.")

if __name__ == "__main__":
    main()
