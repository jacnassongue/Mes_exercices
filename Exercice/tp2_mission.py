# Exercice_1
# nom_mission = "SENTINEL-TG-2026"
# altitude_satellite = 830 # en km
# longitude_depart = -4.0254 # Abidjan
# latitude_depart = 5.5411
# vitesse_orbitrale = 7662.5 # en m/s
# mission_active = True
# date_lancement =  None 
# print("Nom_Mission:", nom_mission)
# print(type(nom_mission))
# print("Altitude_Satellite:", altitude_satellite, "km")
# print(type(altitude_satellite))
# print("Longitude_Depart:", longitude_depart)
# print(type(longitude_depart))
# print("Latitude_Depart:", latitude_depart)
# print(type(latitude_depart))
# print("Vitesse_Orbitrale:", vitesse_orbitrale, "m/s")
# print(type(vitesse_orbitrale))
# print("Mission_Active:", mission_active)
# print(type(mission_active))
# print("Date_Lancement:", date_lancement)
# print(type(date_lancement))

# exercice_2

# altitude_str = "750"
# vitesse_str= "7800.5"
# nb_capteurs_str ="12"
# altitude = int(altitude_str)
# vitesse = float(vitesse_str)
# nb_capteurs = int(nb_capteurs_str)
# print("Altitude:", altitude)
# print("Vitesse:", vitesse)
# print("Nombre de capteurs:", nb_capteurs)

# exercice_3
#zone_1
# largeur = 250 # en km
# longueur = 180 # en km
# #zone_2
# largeur_2 = 320 # en km
# longueur_2 = 220 # en km
# #calcul de la surface de la zone 1
# surface_zone_1 = largeur * longueur
# print("Surface de la zone 1:", surface_zone_1, "km²")
# #calcul de la surface de la zone 2
# surface_zone_2 = largeur_2 * longueur_2
# print("Surface de la zone 2:", surface_zone_2, "km²")
# # Calcul de la surface totale
# surface_totale = surface_zone_1 + surface_zone_2
# print("Surface totale:", surface_totale, "km²")

# # 4- 

# # exercice_4
# images_reçues = 2457
# images_traitées_par_lot = 12
# # 1-Nombre de lots complets:
# lots_complets = images_reçues // images_traitées_par_lot
# print("Nombre de lots complets:", lots_complets)
# # 2-Nombre d'images restantes:
# images_restantes = images_reçues % images_traitées_par_lot
# print("Nombre d'images restantes:", images_restantes)
# # 3-Temps de traitement de tous les lots en minutes
# nbr_serveur = 10
# minutes_par_lot_par_serveur = 1
# # ===> en une minute, on traite 10 lots (1 lot par serveur)
# nobre_minute = lots_complets / nbr_serveur *     minutes_par_lot_par_serveur    
# print("Temps de traitement de tous les lots en minutes:", nobre_minute, "minutes")

# exercice_5
# mission = "SENTINEL-TG"
# date = "30/05/2026"
# zone = "Côte d'Ivoire"
# altitude = 830 
# capteur = 5
# Rapport = "la mission s'est déroulée sous le nom de " + mission + " le "  +  date  +  " en "  +  zone  +  " d'une altitude de "  +  str(altitude) + " avec "  + str(capteur) + " capteurs."
# print("Rapport de mission:", Rapport)

# exercice_6
message = """
CENTRE SPATIAL DE LOME
---------------------------------

Bienvenue, technicien satellite!

Equipe: 5 personnes
Missions actives: 3
"""
print(message)

# exercice_7
