# création de la classe agence
class Agence:
    def __init__(self, nom, open_matin, close_matin, open_soir, close_soir):
        self.nom = nom
        self.services = []
        self.telephone = None
        self.open_matin = open_matin
        self.close_matin = close_matin
        self.open_soir = open_soir
        self.close_soir = close_soir
    
    def afficher(self):
        has_service = False
        Services = ""
        if self.services != []:
            has_service = True
        if has_service:
            for index, i in enumerate(self.services):
                Services = Services + i
                if self.services[index] != self.services[-1]:
                    Services = Services + ", "
                else:
                    Services = Services + "."
        else:
            Services = "Aucun service pour l'instant"

        return f"""Agence {self.nom}
Horaires : {self.open_matin}h-{self.close_matin}h / {self.open_soir}h-{self.close_soir}h
Services: {Services}"""
    
    def ajouter_service(self, nom_service):
        self.services.append(nom_service)
    
    def retirer_service(self, index):
        if 0 <= index <= (len(self.services) - 1):
            self.services.pop(index)
        else:
            print("index invalide")

# Créer des agences (Objets)
Agence1 = Agence("Adidogomé", 7, 12, 14, 17,)
Agence2 = Agence("Baguida", 7, 12, 14, 17)

Agence1.ajouter_service("Déclaration")

print(Agence1.afficher())
print(Agence2.afficher())

Agence1.retirer_service(0)
print(Agence1.afficher())
Agence1.retirer_service(0)
print(Agence1.afficher())


