# Devoir de maison sur les boucles et les dictionnaires
# SECTION 1
# Ex01.1
list_A = ["PARC-001", "PARC-002", "PARC-003"]
list_B = [350, 1200, 95]
list_C = ["Golfe 1", "Agoè-Nyivé 1", "Golfe 1"]
# for i, valeur_a in enumerate(list_A, start=0):
#     print(f"{valeur_a} - {list_B[i]} m² - {list_C[i]}")
# Le relevé de terrain
parcelles = ["PARC-001", "PARC-002", "PARC-003", "PARC-004", "PARC-005", "PARC-0036"]
surfaces = [350, 1200, 95, 640, 210, 1500] # en m²
communes = ["Golfe 1", "Agoè-Nyivé 1", "Golfe 1", "Bas-Mono 1", "Agoè-Nyivé 1", "Bas-Mono 1"]
# Question 1.1
# for i, parcelle in enumerate(parcelles, start = 1):
    # print(i, parcelle)
# Question 1.2
# for i, parcelle in enumerate(parcelles, start=1):
#     print(f"{i}, {parcelle}-{surfaces[i-1]} m²")
# Question 1.3- Repérer les grandes parcelles
# for i, (parcelle, surface) in enumerate(zip(parcelles, surfaces)): #zip qui permet d'aasocier chaque élément de parcelle à chaque élément de surface
#     if surface > 500 :
#         print(f"{parcelle} - {surface} m²")
# #Question 1.4: le bilan des surfaces
# # 1. La surface total
# surfaces_total = sum(surfaces)
# print(f"la surface totale est : {surfaces_total}")
# # Le nombre de parcelles situées dans Golfe 1
# nombre_parcelles_golfe_1 = 0
# # print(f"le nombre de parcelles dans la commune Golfe 1 est : {nombre_parcelles_golfe_1}")
# for i, parcelle in enumerate(parcelles):
#     if communes[i] == "Golfe 1":
#         nombre_parcelles_golfe_1 = nombre_parcelles_golfe_1 +1
# print(f'le nombre de parcelle dans Golfe 1 est : {nombre_parcelles_golfe_1}')

# # les étiquettes de classeurs
# for i in range(len(parcelles)):
#     print(f'Etiquette n°{i+1}')
# Question 1.6-La recherche au guichet (while + break)
# while True:
#     id_parcelle = input("Entrer l'identifiant de votre parcelle :")
#     if id_parcelle in parcelles:
#         print("Parcelle trouvée dans le relevé.")
#     else: 
#         print("Aucune parcelle à cet identifiant.")
#     if id_parcelle == "fin":
#         print("Fermeture du guichet")
#         break
# Exercie 2-Le suivi des demandes de permis de construire
dossiers = ["DOS-201","DOS-202", "DOS-203", "DOS-204", "DOS-205"]
demandeurs = ["Atta Koffi", "Mireille Yao", "Ibrahim Dosso", "Fatou Coulibaly", "Ernest Bah"]
statuts    = ["approuvé", "en_attente", "rejeté", "en_attente", "approuvé"]
# # Question2.1
for i, (dossier, demandeur) in enumerate(zip(dossiers, demandeurs)):
    print(f'{i+1}. {dossier} - {demandeur}')
for i, dossier in enumerate(dossiers):
    print(f"{i+1}. {dossier} - {demandeurs[i]} avec statut : {statuts[i]}")
# liste_2 = [1, 2, 3, 4, 5, 6, 7]
# liste_3 = ["un", "deux", "trois", "quatre"]
# for a, b in enumerate(liste_3):
#     print(f"{liste_2[a]} = {b}")