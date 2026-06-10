# liste_1 = [14, 25, 28]
# nb = "10 est un nombre"
# print(10 in liste_1 and 10 in nb)
# # Exercice_2
# surface = 350
# zone_urbaine = True
# print((surface > 250) and (zone_urbaine ==True))

# #Exercice_3
# annees_depuis_releve = 8
# print((annees_depuis_releve >= 10) or ("cadastre" in "departement du cadastre"))

# # Exercice_4
# zone = "zone_B"
# pente = 30
# print((zone in ["zone_A", "zone_B", "zone_C"]) and (pente <= 25))

# Exercice_5_1: conditions imbriquées
# 1
# print("zone" in "zone_cadastrale")
# # 2
# print("limite" in "limite de propriete")
# # 3
# print(("zone" in "zone_cadastrale") or ("limite" in "limite de propriete"))
# # 4
# print(100 > 50) 
# # 5
# print(("zone" in "zone_cadastrale") or ("limite" in "limite de propriete") and (100 > 50)) 

# Exercice_5_2 iùbrication avec variables
# parcelle_id = 105
# commune = 'Golfe 1'
# surface = 350
# # 1
# print( parcelle_id in [101, 102,    103])
# # 2
# print(commune == 'Golfe 1')
# # 3
# print((parcelle_id in [101, 102, 103]) or (commune == 'Golfe 1'))
# # 4
# print((surface > 200))
# # 5
# print((parcelle_id in [101, 102, 103]) or (commune == 'Golfe 1') and (surface > 200))

#Exercice_5_3 imbrication plus complexes

# litige = False
# nb_produits = 3
# pente = 28
# # 1
# print(("proprietaire" in "proprietaire absent"))
# # 2
# print(litige == False)
# # 3
# print(("proprietaire" in "proprietaire absent") or (litige == False))
# # 4
# print(nb_produits >= 5)
# # 5
# print(pente <= 30)
# # 6
# print((nb_produits >= 5) or (pente <= 30))
# # 7
# print((("proprietaire" in "proprietaire absent") or (litige == False)) and ((nb_produits >= 5) or (pente <= 30)))

# Exercice_6_1
# surface = 300
# zone = "urbaine"
# litige = False
# print((surface > 200) and (zone == "urbaine") and (litige == False))

# Exercice_6_2
# annees = 5
# releve_a_jour = False
# print((annees >= 10) or (releve_a_jour == True) or ("cadastre" in "dept du cadastre"))

# Exercice_6_3
# pente = 20
# zone_inondable = True
# surface = 150
# jugement = False
# expression = ((pente > 25) and (zone_inondable ==True) and (surface < 100)) or (jugement ==True)
# print(expression)

# Exercice_6_4
proprietaire = 'Kofi'
surface = 400
actes_complets = True 
delai_expire = True
expression_1 = ((proprietaire in ['Kofi', 'Amina', 'coco']) and (surface > 250)) or ((actes_complets == False) and (delai_expire == True))
print(expression_1)