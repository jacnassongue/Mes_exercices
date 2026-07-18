# Question 1.1 — L’addition
def additionner(a,b):
    # la fonction retourne la somme des paramètres
    somme = a + b
    return somme
# print(additionner(350, 640))
# print(additionner(0, 1500))

# Question 1.2 — La soustraction et la multiplication
def soustraire(a, b):
    return a - b
# print(soustraire(1200, 350))
def multiplier(a, b):
    return a * b
# print(multiplier(640, 500))

# Question 1.3 — La division (avec précaution)

def diviser(a, b):
    if b == 0:
        return "Erreur: la division par zéro"
    else:
        return a / b
# print(diviser(1200, 4)) 
# print(diviser(500, 0)) 

# Question 1.4 — Le menu

def afficher_menu():

    print("""
        ====== 
          CALCULATRICE CADASTRE
        ======
        1 — Addition 
        2 — Soustraction 
        3 — Multiplication 
        4 — Division 
        fin — Quitter
        ======
          """
    )
# afficher_menu()

# a = "=" * 6
# print(a)
# SECTION 2 — L’assemblage
# Question 2.1 — Le chef d’orchestre
def calculer(choix, a, b):
    a = int(a)
    b = int(b)
    if choix == "1":
        return additionner(a,b)
    elif choix == "2":
        return soustraire(a, b)
    elif choix == "3":
        return  multiplier(a, b)
    elif choix == "4":
        return diviser(a, b)
    else:
        return "Choix invalide"
# print(calculer("1", 350, 640))
# print(calculer("4", 1200, 0))
# print(calculer("9", 10, 5))

# Question 2.2 — La calculatrice en action
# while True:
#     afficher_menu()
#     choix = input("choisier un menu : ")
#     if choix.lower() == "fin":
#         print("Au revoir")
#         break
#     else:
#         premier_nb=input("Entrer le premier nombre :")
#         second_nb = input("Entrer le second nombre :")
#         print(f'Résultat: {calculer(choix, premier_nb, second_nb)}')

def calculer_boucle(choix, new, old,c):
    new = int(new)
    if choix == "1":
        if c == 1:
            old = 0
        return new + old
    if choix == "2":
        if c == 1:
            old = 0
        return new - old
    if choix == "3":
        if c == 1:
            old = 1
        return new * old
    if choix == "4":
        if c == 1:
            old = 1
        return new / old
    else:
        return "Option invalide"   
while True:
    afficher_menu()
    choix = input("choisier un menu : ")
    if choix.lower() == "fin":
        print("Au revoir")
        break
    else:
        next = True
        compteur = 0
        total =0
        while next:
            
            Entrer = input("Entrer la valeur ou fin pour arrêter :")
            if Entrer.lower() != "fin":
                compteur = compteur + 1
                total = calculer_boucle(choix, Entrer, total, compteur)
            if Entrer.lower() == "fin":
                print(total)
                next= False



    




    
