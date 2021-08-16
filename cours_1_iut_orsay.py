

"""
    Cours no 1 : « Premiers pas en Python »
    1. Affectez les variables temps et distance par les valeurs 6.892 et 19.7.
    > Calculez et affichez la valeur de la vitesse.
    > Améliorez l’affichage en imposant un chiffre après le point décimal.
    2. Saisir un nom et un âge en utilisant l’instruction input(). Les afficher.
    > Refaire la saisie du nom, mais avec l’instruction raw_input(). L’afficher.
    > Enfin, utilisez la « bonne pratique » : recommencez l’exercice en transtypant les saisies
    effectuées avec l’instruction raw_input()
 """
#----------------------------------------------------------------------------------------------------------------------
# 1)
temps = 6.892
distance = 19.7
vitesse = (distance/temps)
print(vitesse)
print("%.2f" % vitesse)

# 2)
name = input("nom ?")
age = input("age ?")
print("ton nom est ",name, "et tu as ",age, " ans.")





