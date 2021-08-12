"""

EXERCICE PYTHON 3

> Créer un programme simulant un combat qui respecte les contraintes suivantes :
    - Deux joueurs, auxquels on demandera de choisir un pseudo
    - Les deux combattants démarrent avec 250 points de vie chacun
    - Le combat se déroule en 4 attaques (Joueur 1, Joueur 2, Joueur 1 et enfin Joueur 2)
    - Chaque attaque est une tentative (si elle réussit, le joueur infligera un nombre de dégats en 0 et 100 -
                                        si elle échoue, l'attaque est ratée, et c'est au tour de l'autre joueur)
    - A la fin du combat (les 4 attaques), on déclare le gagant (celui à qui il reste le plus de points de vie)

> Indications :
    - Le déroulement du combat doit être logique et annoncé à l'utilisateur (afficher du txt, décrire ce qu'il se passe)
    - Coder dans un 1er temps uniquement avec des affichages/saisies, variables, opérations, conditions.
    - Pour les plus avancés, on peut optimiser ce code ensuite en l'adaptant avec nos connaissances
    (boucles, fonctions, classe, etc).

"""

import random

titan1_name = ""
titan1_hp = 250

titan2_name = ""
titan2_hp = 250

random_attack = True # True = Face / False = Pile #
random_damage = 0

titan1_name = input("Joueur 1, choisissez un pseudo : ")
#on peut ensuite mettre print("{} est le Joueur 1."format(titan1_name)). Ce code est valable mais python 3.6 l'a
# amélioré#
print(f"{titan1_name} est le Joueur 1.") #valable depuis 3.6

titan2_name = input("Joueur 2, choisissez un pseudo : ")
print(f"{titan2_name} est le Joueur 2.")


print("\nLE COMBAT COMMENCE !\n")

#----------------------------------------------------------------------------------------------------------------------

# PREMIERE ATTAQUE #

input()
print(f"{titan1_name}, à vous de commencer !")
print(f" {titan1_name} : {titan1_hp} PV / {titan2_name} : {titan2_hp}")
random_attack = random.randint(0,1)
random_damage = bool(random_attack)

if random_attack == True :
    #Si l'attaque réussit #
    random_damage = random.randint(0,100)
    print(f"{titan2_name} subit une attaque de {titan1_name} ! Il lui inflige {random_damage} points de dégâts !")
    titan2_hp -= random_damage
else:
    #Si l'attaque échoue#
    print(f"{titan1_name} rate son attaque...")

#----------------------------------------------------------------------------------------------------------------------

# DEUXIEME ATTAQUE #

input()
print(f"{titan2_name}, à vous de commencer !")
print(f" {titan1_name} : {titan1_hp} PV / {titan2_name} : {titan2_hp}")
random_attack = random.randint(0,1)
random_damage = bool(random_attack)

if random_attack == True :
    #Si l'attaque réussit #
    random_damage = random.randint(0,100)
    print(f"{titan1_name} subit une attaque de {titan2_name} ! Il lui inflige {random_damage} points de dégâts !")
    titan1_hp -= random_damage

else:
    #Si l'attaque échoue#
    print(f"{titan2_name} rate son attaque...")

#----------------------------------------------------------------------------------------------------------------------

# TROISIEME ATTAQUE #

input()
print(f"{titan1_name}, à vous de commencer !")
print(f" {titan1_name} : {titan1_hp} PV / {titan2_name} : {titan2_hp}")
random_attack = random.randint(0,1)
random_damage = bool(random_attack)

if random_attack == True :
    #Si l'attaque réussit #
    random_damage = random.randint(0,100)
    print(f"{titan2_name} subit une attaque de {titan1_name} ! Il lui inflige {random_damage} points de dégâts !")
    titan2_hp -= random_damage

else:
    #Si l'attaque échoue#
    print(f"{titan1_name} rate son attaque...")

#----------------------------------------------------------------------------------------------------------------------

# QUATRIEME ATTAQUE #

input()
print(f"{titan2_name}, à vous de commencer !")
print(f" {titan1_name} : {titan1_hp} PV / {titan2_name} : {titan2_hp}")
random_attack = random.randint(0,1)
random_damage = bool(random_attack)

if random_attack == True :
    #Si l'attaque réussit #
    random_damage = random.randint(0,100)
    print(f"{titan1_name} subit une attaque de {titan2_name} ! Il lui inflige {random_damage} points de dégâts !")
    titan1_hp -= random_damage

else:
    #Si l'attaque échoue#
    print(f"{titan2_name} rate son attaque...")

#----------------------------------------------------------------------------------------------------------------------

#Resultat final#

print("\nFIN DU COMBAT\n")
print(f" {titan1_name} : {titan1_hp} PV / {titan2_name} : {titan2_hp}")

if titan1_hp > titan2_hp :
    print(f"{titan1_name} remporte la victoire !")
elif titan1_hp < titan2_hp :
    print(f"{titan2_name} remporte la victoire !")
else :
    print("Match nul !")
