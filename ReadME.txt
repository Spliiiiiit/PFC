# Pierre-Feuille-Ciseaux - Guide de Lancement

## Introduction
Ce projet implémente un jeu de Pierre-Feuille-Ciseaux en utilisant des sockets UDP pour la communication entre un serveur et un client. Le jeu se déroule en 5 rounds et détermine le gagnant en fonction des choix faits par les deux joueurs.

## Prérequis
- Python 3.x
- Bibliothèque standard de Python (socket)
- Deux terminaux ou machines pour exécuter le serveur et le client



## Instructions de Lancement

### Étape 1 : Lancement du Serveur

1. Ouvrez un terminal.
2. Accédez au répertoire contenant le fichier `server.py`.
3. Exécutez la commande suivante :

python server.py

4. Le serveur affichera le message "Le serveur est prêt et attend des connexions...".



### Étape 2 : Lancement du Client

1. Ouvrez un autre terminal (ou une autre machine).
2. Accédez au répertoire contenant le fichier `client.py`.
3. Exécutez la commande suivante :

python client.py

4. Le client affichera un message de bienvenue et vous demandera de saisir votre choix pour chaque round.



### Fonctionnement du Jeu

1. Le client enverra votre choix (pierre, feuille, ou ciseau) au serveur pour chaque round.
2. Le serveur recevra les choix des deux joueurs, déterminera le gagnant du round et mettra à jour les scores.
3. Le serveur enverra le résultat du round à chaque client.
4. Après 5 rounds, le serveur enverra le résultat final (gagnant du Bo5) aux clients.



### Fichiers Inclus

- `server.py` : Contient le code du serveur qui gère le jeu.
- `client.py` : Contient le code du client qui permet aux joueurs de participer au jeu.
- `ReadMe.txt` : Ce fichier, expliquant comment lancer le jeu.



## Remarques

- Assurez-vous que le serveur est en cours d'exécution avant de lancer le client.
- Si le serveur et le client sont exécutés sur des machines différentes, remplacez `127.0.0.1` par l'adresse IP appropriée du serveur dans le fichier `client.py`.

Nous espérons que vous apprécierez ce super jeu ultra original de Pierre-Feuille-Ciseaux. Amusez-vous bien !

---

Auteur : [Brieuc Le Carluer]
Date : [14/06/24]

