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
print(dd_vers_dms(3.87))
print(dd_vers_dms(11.52))

