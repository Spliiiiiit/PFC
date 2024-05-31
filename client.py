import socket
import threading

def recevoir_instructions(sock):
    try:
        print("En attente d'instructions du serveur...")
        while True:
            instruction = sock.recv(1024).decode()
            print("Instruction reçue du serveur:", instruction)

            if "Choisissez pierre, feuille ou ciseaux: " in instruction:
                choix_utilisateur(sock)
    except Exception as e:
        print(f"Erreur dans recevoir_instructions : {e}")

def choix_utilisateur(sock):
    try:
        print("En attente du choix de l'utilisateur...")
        choix = input("Choisissez pierre, feuille ou ciseaux: ").lower()
        sock.send(choix.encode())
        print("Choix envoyé au serveur.")
    except Exception as e:
        print(f"Erreur dans choix_utilisateur : {e}")

def main():
    HOST = '127.0.0.1'
    PORT = 5000

    try:
        print("Tentative de connexion au serveur...")
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        print("Connecté au serveur.")

        recevoir_instructions(sock)
    except Exception as e:
        print(f"Erreur lors de la connexion au serveur : {e}")

if __name__ == "__main__":
    main()

