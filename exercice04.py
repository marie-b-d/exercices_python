"""

    EXERCICE PYTHON 04 (révisions jusqu'aux boucles)

    > Développer un mini-terminal tournant en boucle et gérant quelques commandes définies :
        - Votre programme invitera l'utilisateur à saisir une commande (comme la ligne de commande Windows, MacOS...)
        - Gérer le cas où une commande n'existe pas
        - Aucun module ne doit être importé

    > Quatre commandes à prévoir :
        - run (affiche 5 fois un point avec une pause chaque affiche de 1s)
        - name (modifie le nom du terminal, s'appellera "Défaut" de base)
        - help (affiche la liste des commandes + description brève)
        - quit (termine l'exécution du programme)

    > Ce qui devra être affiché :
            [Defaut] >
            [nom_terminal]>

"""

import time
#mettre en pause 1s -> time.sleep(1)#

terminal_launched = True
terminal_name = "Defaut"
user_command = ""
cpt = 0

while terminal_launched:
    user_command = input(f"[{terminal_name}]> ")

    if user_command == "run":
       while cpt < 5:
           print(".")
           cpt += 1
           time.sleep(1)
       cpt = 0
    elif user_command == "name":
        terminal_name = input("Choisir nouveau nom du terminal : ")
    elif user_command == "help":
        print("\
-------------------------------\n\
LISTE DES COMMANDES DISPONIBLES\n\
-------------------------------\n\
run : affiche 5 fois un point avec une pause chaque affiche de 1s\n\
name : modifie le nom du terminal\n\
help : affiche la liste des commandes\n\
quit : termine l'exécution du programme\n\
-------------------------------")
    elif user_command == "quit":
        terminal_launched = False
    else :
        print("commande introuvable...")
