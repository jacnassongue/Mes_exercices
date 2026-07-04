#Partie 1 — Coordonnées et Points Géographiques (Exo 1 à 10)
# Exercice 1 — Conversion DMS → Degrés Décimaux
def  dms_vers_dd(degres, minutes, secondes):
    " Cette fonction convertit le format et retourne les coordonnées en degré decimaux"
    DD = float(degres) + float(minutes)/60 + float(secondes)/3600
    return round(DD, 2)
# print(dms_vers_dd(3, 52, 12.0))
# print(dms_vers_dd(11, 31, 12.0))

# xercice 2 — Conversion Degrés Décimaux → DMS
def  dd_vers_dms(dd):
    "cette fonction convertit le format decimal et retourne les coordonnées en degres, minute, seconde"
    d= int(dd)
    md = abs(dd - d) * 60
    m = int(md)
    sd = (md - m) * 60
    return [d, m, round(sd, 2)]
# print(dd_vers_dms(3.87))
# print(dd_vers_dms(11.52))

# Exercice 3 — Validation de Latitude
def est_latitude_valide(lat):
    "valide latitude si la coordonnée est comprise entre -90 et 90 inclus."
    if lat >= -90 and lat <= 90:
        return True
    else:
        return False
print(est_latitude_valide(3.87))
print(est_latitude_valide(95.0))
print(est_latitude_valide(-90.0))

# Exercice 4 — Validation de Longitude
def  est_longitude_valide(lon):
    "valide la longueur en retournant True si celle-ci est comprise entre - 180 et 180"
    if lon >= -180 and lon <= 180:
        return True
    else:
        return False
# Exercice 5 — Création d’un Point Géographique
def  creer_point(lat, lon):
    "vérifie les fonctions est_latitude_valide et est_longitude_valide, au cas contraire, affiche un message d'erreur et retourne None"
    if est_latitude_valide(lat) == True:
        
    if est_longitude_valide(lon)

