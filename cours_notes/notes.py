# jour = "samedi"
# jour1 = 6
# date =f"aujourd'hui on est {jour} le {jour1}"
# print(date)
# date2 = "aujourd'hui on est" + jour + " le " + jour1
# print(date2)

# le f" permet de créer les chaines de caractères avec des variables sans forcement connaître leur type. la concatenation se fait entre les éléments ou vari    ble de même type à priori. le f" permet de resoudre ou de contourner cette contrainte.

# Méthode de traitement des chaine de caractères

# salut  =  " Bienvenue "
# salu_t = salut.strip()
# print(salu_t)
# # la méthode .strip() permet de supprimer les spaces au debut et à la fin dans une chaine de caratères. 
# salut_1 = salu_t.upper()
# print(salut_1)
# salut_2 = salut_1.lower()
# print(salut_2)

# salut_3 = salu_t + " à Lomé "
# print(salut_3)

# salut_4 = salut_3.replace("Lome", "Kara")
# print(salut_4)
# # la méthode replace("","") permet de rechercher et remplacer un éléments

# is_lome = "Lome" in salut_4
# print(is_lome)

# mot = "abracadabradaro  "
# nb = mot.count("a")
# print(nb)
# nb1= mot.count("n")
# print(nb1)
# nb2 = len(mot)
# print(nb2)
# nb3 = " " in mot
# print(nb3)

# # Découpage de chaine de caractères
# ville = "Djarkpangacity"
# lettre = ville[0]
# print(lettre)
# lettre1 = ville[-4]
# print(lettre1)
# ville1 = "KARACITY"
# long = len(ville1)
# print(long)
# ville2 = ville1[0:6]
# print(ville2)
# ville3 = ville1[4:8]
# print(ville3)
# ville4 = ville1[:5]
# print(ville4)
# mot_envers = ville[::-1]
# print(mot_envers)

# Exercice d'application

# boutique = " EPICERIE DU SOLEIL "
# boutique_net = boutique.strip()
# print(boutique_net)
# print(len(boutique), len(boutique_net))
# print(" " in boutique, " " in boutique_net)
# print(" " in boutique_net)
# print("  " in boutique_net)

# longitude = " 6.42553 "
# latitude = " 1.3435 "

# boutique_re = boutique_net.replace("SOLEIL", "MATIN")
# print(boutique_re)
# boutique_8 = boutique_re[0:8]
# print(boutique_8)
# print("EPICERIE" in boutique)

# nom = "Koffi"
# commune = "Golfe 1"
# nb = 20
# message = f" La boutique de {nom} est à {commune} et propose {nb} produits"
# print(message)

# # les listes
# produits = ['lait', 'sucre', 'café']
# print(produits[0])
# # Si on veut ajouter par exemple un produit dans la boutique ou dans un centre qui a commencer par offrir ce service, on utilise la méthode .append
# produits.append("riz")
# print(produits)
# #.append ajoute les éléments à la fin de la liste
# # .insert ajoute les éléments à la place indiquée par indexation.
# produits.insert(1, "farine")
# print(produits)
# #  on veut retirer un élément de la liste: on utilise la méthode .remove, .remove("lait")
# produits.remove("lait")
# print(produits)
# # la métgode .pop enlève le dernier élément de la liste si on ne lui précise rien. si on lui fournit l'index, il supprime l'élément indexé. 
# produits.pop()
# print(produits)
# produits.pop(1)
# print(produits)
# print("café" in produits)

# # Les conditions

# entree = " salut "
# if " " in entree:
#     print(len(entree))
#     entree = entree.strip()
#     print(len(entree))

# age = int(input('Entrez votre age:'))
# if age >= 18:
#     print("Vous êtes majeur")
# elif age == 5: 
#     print("Vous êtes trop petit")
# elif age == 6:
#     pass # pass dit de ne rien faire
# else:
#     print("vous êtes mineur")


# Les boucles: permettent de répéter une instructionou de reprendre des opération
# For
# ma_liste = ["Hello", "Hier", "suivante", "samedi"]
boutique = [ 
    "chez Mamadou",
    "Epicerie du soir",
    "supermarché plus",
    "Boulangerie Fatou",
    "Marché Central"
]
# for x in boutique:
#     print(f'Nom Boutique: {x}')
# for x in boutique:
#     if len(x) > 12:
#         print(f'Nom Boutique: {x}')
# nombre_boutique = 0
# nom = ""
# for x in boutique:
#     if "de" in x or "du" in x:
#         nombre_boutique = nombre_boutique + 1
#         nom = x
# print(nombre_boutique)
# print(f"nom de la boutique: {nom}")

# La boucle for ave range
# elle permet de limiter le nombre de chance sur une action, par exemple, entrer un code
# range(5)
# for i in range(5):
#     print(i)
# print('Table de multiplication paar 2')
# for a in range(13):
#     print(f' 2*{a}= {2*a}')
# # une méthode de for qui permet de savoir on est à la quellième itération dans la boucle:
# # enumerate:
# for numero, nom in enumerate(boutique, start=1):
#     print(f'{numero}:{nom}')
# for i in range(2,11):
#     print(i)

# Boucle while 
# try:
#     nom = (input('nom de la boutique est: '))
#     print("Vous avez entré une chaine de caractère")
#     print(nom) 
# except:
#     print("Veuillez entrez une chaine de caractère")

# while True:
#     a = input("Entrer le nom d'une boutique: ")
#     if a != "fin":
#         if a in boutique:
#             print("Boutique Trouvé")
#         else:
#             print("Boutique pas trouvé")
#     else:
#         break
# les dictionnaires: ils s'affichent clé : valeur c'est-)-dire nom: chez mamadou
# boutique = {
#     'nom':"Chez mamadou",
#     "quartier": "Leo 2000",
#     "Ouvert": True,
#     "Nb_produits": 12
#     }
# print(boutique["non"])
# print(boutique.get('nom', "Aucun nom trouvé"))
# boutique["nom"] = "Epicerie du matin" # changer la clé dans le dictionnaire
# print(boutique.get("nom"))
# on peut ajpouter une nouvelle clé avec sa valeur par la même méthode ci-haut:
# boutique["numero"] = 900000
# print(boutique)
# si on considère que c'est une erreur d'ajouter un numéro et qu'on veut l'enlever;
# boutique.pop("numero")
# del boutique["numéro"]
# On peut tout simplement récupérer les clés ou juste les valeurs
# for cle in boutique:
#     print(cle)
# for valeur in boutique.values():
#     print(valeur)
# # On veut récupérer et les clés et les valeurs et les afficher de façon personnalisée
# for cle, valeur in boutique.items():
#     print(f'{cle} : {valeur}')

range(12)
# 
# for i in range(10):for i in range(0,12):
#     print(f'2*{i} = {2*i}')
#     print(i)
# for n in range(0,12):
#     if n%2 ==0:
#         print(1+n)

# annee = 1822
# print(f"Le premier ordinateur fut inventé en {annee}")

# les fonctions
# def salutation():
#     print("Bonjour")
# # On peut l'appeler plus loin
# salutation()
# def date():
#     print("On est aujourd'hui le 21 juin 2026")
# date()
# on peut donner un paramètre à la fonction saliutation(): salutation(Abalo)
# def salutation(prenom):
#     print(f"Bonjour {prenom}")
# salutation("Abalo")
# salutation("Faure Gnassingbé")
# les fonction permettent aussi de faire des opération grâce au mot return:
# def somme_age(annee):
#     age = 2026-annee
#     return age
# n_age = somme_age(2006)
# print(n_age)

# def calculer_total(prix, quantite):
#     Total = prix*quantite
#     return Total
# achat = calculer_total(500,3)
# print(achat)

# def afficher_menu():
#     print("""
#           ====MENU===
#           1) Voir les agences
#           2) rechercher
#           3) Quitter
#           """)
# afficher_menu()

# def est_dans_liste(liste, valeur):
#     # b=False
#     for val in liste:
#         if val == valeur:
#             return True
#         else:
#             return False
    
# test = ["hey", "test", "hello"]    
# valeu = input("Entrer une valeur :")
# recuper = est_dans_liste(boutique, valeu)
# if recuper  == True:
#     print(f"La valeur se trouve dans la liste")
# else:
#     print("Aucune valeur correspondante dans la liste")

noms = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for i, (nom, score) in enumerate(zip(noms, scores), start=1):
    print(f"{i}. {nom} a obtenu {score} points")

     