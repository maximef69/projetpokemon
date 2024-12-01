import random 
class Carte:
    
    def __init__(self, nom, points_de_vie, attaque, energie, type):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.attaque = attaque
        self.energie = energie
        self.type = type
        
    def __str__(self):
        return(
                f"{self.nom} - PV: {self.points_de_vie}, "
                f"Attaque: {self.attaque}, Énergie: {self.energie}, Type: {self.type}")
            
class MainCartes:
    def __init__(self, nom, listeCartes):
        self.nom = nom
        self.listeCartes = listeCartes
        
    def afficherMain(self):
        print(f"Nom : {self.nom}")
        for i in self.listeCartes:
            print(i)
 
 
# Début du programme

# Création des cartes   
carte1 = Carte("Dragon de Feu", 30, 8, 3, "Feu")
carte2 = Carte("Hydre Aquatique", 25, 6, 2, "Eau")
carte3 = Carte("Etoile d'air",28, 7, 1, "Air" )
carte4 = Carte("Libélule des près",31, 10, 5, "Terre")

# Création des listes
ListeJoueur1 = [carte1, carte2]
ListeJoueur2 = [carte3, carte4]

#Création des mains des joueurs avec la classe MainCartes
MainJoueur1 = MainCartes("Paul", ListeJoueur1)
MainJoueur2 = MainCartes("Marie", ListeJoueur2)

MainJoueur1.afficherMain()
MainJoueur2.afficherMain()