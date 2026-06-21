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
#     print(i, parcelle)
# Question 1.2
# for i, parcelle in enumerate(parcelles, start=1):
#     print(f"{i}, {parcelle}-{surfaces[i-1]} m²")
# Question 1.3- Repérer les grandes parcelles
# for i, (parcelle, surface) in enumerate(zip(parcelles, surfaces)): #zip qui permet d'aasocier chaque élément de parcelle à chaque élément de surface
#     if surface > 500 :
#         print(f"{parcelle} - {surface} m²")
#Question 1.4: le bilan des surfaces
# 1. La surface total
surfaces_total = sum(surfaces)
print(f"la surface totale est : {surfaces_total}")
# Le nombre de parcelles situées dans Golfe 1


