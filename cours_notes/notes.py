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

nom = "Koffi"
commune = "Golfe 1"
nb = 20
message = f" La boutique de {nom} est à {commune} et propose {nb} produits"
print(message)

# les listes
produits = ['lait', 'sucre', 'café']
print(produits[0])
# Si on veut ajouter par exemple un produit dans la boutique ou dans un centre qui a commencer par offrir ce service, on utilise la méthode .append
produits.append("riz")
print(produits)
#.append ajoute les éléments à la fin de la liste
# .insert ajoute les éléments à la place indiquée par indexation.
produits.insert(1, "farine")
print(produits)
#  on veut retirer un élément de la liste: on utilise la méthode .remove, .remove("lait")
produits.remove("lait")
print(produits)
# la métgode .pop enlève le dernier élément de la liste si on ne lui précise rien. si on lui fournit l'index, il supprime l'élément indexé. 
produits.pop()
print(produits)
produits.pop(1)
print(produits)
print("café" in produits)

# Les conditions

entree = " salut "
if " " in entree:
    print(len(entree))
    entree = entree.strip()
    print(len(entree))

age = int(input('Entrez votre age:'))
if age >= 18:
    print("Vous êtes majeur")
elif age == 5: 
    print("Vous êtes trop petit")
elif age == 6:
    pass # pass dit de ne rien faire
else:
    print("vous êtes mineur")

