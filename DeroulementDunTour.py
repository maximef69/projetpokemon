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


def DeroulementTour(PileJoueur1, PileJoueur2,PileDefausseJoueur1,PileDefausseJoueur2):
    # Extraire la première carte de chaque pile
    CarteJoueur1 = PileJoueur1.pop(0)
    CarteJoueur2 = PileJoueur2.pop(0)
    
    #Affiche des cartes en duel
    print(f"Carte du Joueur 1: {CarteJoueur1}")
    print(f"Carte du Joueur 2: {CarteJoueur2}")

    
    # Comparer la valeur d'attaque des deux cartes
    if CarteJoueur1.attaque > CarteJoueur2.attaque:
        PileDefausseJoueur1.append(CarteJoueur2)
        print("Joueur 1 gagne le duel")   
    elif CarteJoueur1.attaque < CarteJoueur2.attaque:
        PileDefausseJoueur2.append(CarteJoueur1)
        print("Joueur 2 gagne le duel")       
    else:
        PileJoueur1.append(CarteJoueur1)
        PileJoueur2.append(CarteJoueur2)
        print(f"Égalité entre {CarteJoueur1.nom} et {CarteJoueur2.nom}!")

carte1 = Carte("Dragon de Feu", 30, 8, 3, "Feu")
carte2 = Carte("Hydre Aquatique", 25, 6, 2, "Eau")
carte3 = Carte("Etoile d'air",28, 7, 1, "Air" )
carte4 = Carte("Libélule des près",31, 10, 5, "Terre")
carte5 = Carte("Dragon de l'eau", 29, 5, 4, "Eau")
carte6 = Carte("Cheval aquatique", 26, 7, 2, "Eau")
carte7 = Carte("Pikachu",23, 8, 6, "Terre" )
carte8 = Carte("Sacapuce",30, 6, 3, "Terre")         

PileJoueur1 = [carte1, carte2, carte3, carte4] 
PileJoueur2 = [carte5, carte6, carte7, carte7]

PileDefausseJoueur1 = []
PileDefausseJoueur2 = []

DeroulementTour(PileJoueur1, PileJoueur2,PileDefausseJoueur1,PileDefausseJoueur2)
DeroulementTour(PileJoueur1, PileJoueur2,PileDefausseJoueur1,PileDefausseJoueur2)         
DeroulementTour(PileJoueur1, PileJoueur2,PileDefausseJoueur1,PileDefausseJoueur2)         
         