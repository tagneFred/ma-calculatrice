
# =====================================
# PROJET 1 : CALCULATRICE EN PYTHON
# =====================================

# Afficher le titre du programme
print("===== MA CALCULATRICE =====")

# Demander à l'utilisateur de saisir deux nombres
nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))

# Afficher les opérations disponibles
print("\nChoisissez une opération :")
print("1. Addition (+)")
print("2. Soustraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Demander le choix de l'utilisateur
choix = input("Votre choix (1, 2, 3 ou 4) : ")

# Effectuer l'opération choisie
if choix == "1":
    resultat = nombre1 + nombre2
    print("Résultat :", resultat)

elif choix == "2":
    resultat = nombre1 - nombre2
    print("Résultat :", resultat)

elif choix == "3":
    resultat = nombre1 * nombre2
    print("Résultat :", resultat)

elif choix == "4":
    # Vérifier que le deuxième nombre n'est pas zéro
    if nombre2 != 0:
        resultat = nombre1 / nombre2
        print("Résultat :", resultat)
    else:
        print("Erreur : division par zéro impossible !")

else:
    # Si le choix n'est pas valide
    print("Choix invalide. Veuillez recommencer.")

# Message de fin
print("Merci d'avoir utilisé ma calculatrice !")
