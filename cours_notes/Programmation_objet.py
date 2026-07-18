
# Création d'une class
class Agence: 
    def __init__(self, nom, commune, quartier, region, heure_ouverture_matin, heure_fermeture_matin, heure_ouverture_apres_midi, heure_fermeture_apres_midi):
        self.nom = nom
        self.commune = commune
        self.quartier = quartier
        self.region = region
        self.service = []
        self.heure_ouverture_matin = heure_ouverture_matin
        self.heure_fermeture_matin = heure_fermeture_matin
        self.heure_ouverture_apres_midi = heure_ouverture_apres_midi
        self.heure_fermeture_apres_midi = heure_fermeture_apres_midi

# Création de méthodes

    def afficher(self):
        print(f"l'Agence {self.nom} se trouve dans la commune de {self.commune} de la région {self.region} et plus précisement dans le quartier {self.quartier} ")
    def ajouter_services(self, prestations):
        self.service.append(prestations)
    def Retirer_dernier_service(self, index):
        self.service.pop(index)
    def Disponible_Agence(self, heure):
        if (self.heure_ouverture_matin <= heure <self.heure_fermeture_matin) or (self.heure_ouverture_apres_midi <= heure <self.heure_fermeture_apres_midi):
            print("Service Ouvert")
        else:
            print("Service fermé")

# Création des Objets

Obj1 = Agence("Casablanca", "Golfe3", "Casablanca", "Maritime", 7, 12, 14, 17)
Obj2 = Agence("Adawlato", "Golfe4", "Adawlato", "Maritime", 7, 12, 14, 17)
Obj3 = Agence("Hedzranawoe", "Golfe2", "Novissi", "Maritime", 7, 12, 14, 17)

# Utilisation des méthodes

Obj1.afficher()

# print(f"l'Agence {Obj2.nom} se trouve dans la commune de {Obj2.commune} de la région {Obj2.region} et plus précisement dans le quartier {Obj2.quartier} ")
# print(f"l'Agence {Obj3.nom} se trouve dans la commune de {Obj3.commune} de la région {Obj3.region} et plus précisement dans le quartier {Obj3.quartier} ")
Obj1.ajouter_services("TVM")
Obj1.ajouter_services("Recouvrement")
Obj1.ajouter_services("Déclaration")
Obj1.ajouter_services("E,nregistrement")
# Obj1.service.append("Recouvrement")
# Obj1.service.append("Déclaration")
# Obj1.service.append("Enregistrement")
print(Obj1.service)
# la fonction _init_ est un constructeur, il permet de reconstituer les données
# On peut vréer une fonction pour ajouter les agences:
Obj1.Retirer_dernier_service(0)
print(Obj1.service)

Obj1.Disponible_Agence(7)
Obj2.Disponible_Agence(3)
Obj3.Disponible_Agence(11)


