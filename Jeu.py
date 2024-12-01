import random


class Carte:
    def __init__(self, nom, points_de_vie, attaque, energie, type):
        """
        Initialise une carte.
        :param nom: Nom de la carte
        :param points_de_vie: Points de vie de la carte
        :param attaque: Valeur d'attaque
        :param energie: Énergie requise
        :param type: Type de la carte (Feu, Eau, Plante, etc.)

        """
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.attaque = attaque
        self.energie = energie
        self.type = type

    def __str__(self):
        return (
            f"{self.nom} - PV: {self.points_de_vie}, "
            f"Attaque: {self.attaque}, Énergie: {self.energie}, Type: {self.type}"
        )

class Jeu:
    
    def __init__(self):
        # Variables pour le jeu
        self.PileJoueur1 = []
        self.PileJoueur2 = []
        self.PileDefausseJoueur1 = []
        self.PileDefausseJoueur2 = []
        self.nombre_tours = 0
        self.tour_actuel = 0
        
    def DistributionEtMelangeDesCartes(cartes):
        """
        Mélange les cartes et les distribue entre les deux joueurs : 
        - Joueur 1 reçoit les cartes aux indices pairs.
        - Joueur 2 reçoit les cartes aux indices impairs.
        """
        random.shuffle(cartes)  # fonction qui permet de mélanger les cartes

        PileJoueur1 = [cartes[i] for i in range(len(cartes)) if i % 2 == 0]
        PileJoueur2 = [cartes[i] for i in range(len(cartes)) if i % 2 != 0]
        return PileJoueur1, PileJoueur2
                
    def LancerPartie(self):
        self.NombreTours = int(input("Saisir un nombre de tour "))
        if self.NombreTours == 0:
            print("Saisir un nombre de tour positif")
        self.tour_actuel += 1
        
    
    def DuelCarte(self):
        if self.NombreTours == 0:
            print("Saisir un nombre de tour positif")
        self.tour_actuel += 1
        
        CarteJoueur1 = self.PileJoueur1.pop(0)
        CarteJoueur2 = self.PileJoueur2.pop(0)
        
        # Affichage carte 
        self.afficher_message(f"Tour {self.tour_actuel}:")
        self.afficher_message(f"  Joueur 1: {self.CarteJoueur1}")
        self.afficher_message(f"  Joueur 2: {self.CarteJoueur2}")

        # Duel entre les deux cartes
        if CarteJoueur1.attaque > CarteJoueur2.attaque:  #Joueur1 gagne le duel
            self.PileDefausseJoueur1.append(CarteJoueur2)
            self.afficher_message(f"  Joueur 1 gagne le duel avec {CarteJoueur1.nom} !")
        elif CarteJoueur1.attaque < CarteJoueur2.attaque: # Joueur2 gagne le duel
            self.PileDefausseJoueur2.append(CarteJoueur1)
            self.afficher_message(f"  Joueur 2 gagne le duel avec {CarteJoueur2.nom} !")
        else:                                     # En cas d'égalité
            self.PileJoueur1.append(CarteJoueur1)
            self.PileJoueur2.append(CarteJoueur2)
            self.afficher_message(f"  Égalité entre {CarteJoueur1.nom} et {CarteJoueur2.nom} !")
        
        self.fin_partie()

    def fin_partie(self):
        self.bouton_tour.config(state="disabled")

        TailleJoueur1 = len(self.PileDefausseJoueur1)
        TailleJoueur2 = len(self.PileDefausseJoueur2)

        self.afficher_message("\n*** Résultats finaux ***")
        self.afficher_message(f"Cartes remportées par Joueur 1: {TailleJoueur1}")
        self.afficher_message(f"Cartes remportées par Joueur 2: {TailleJoueur2}")

        if TailleJoueur1 > TailleJoueur2:
            self.afficher_message("Joueur 1 a gagné la partie!")
        elif TailleJoueur1 < TailleJoueur2:
            self.afficher_message("Joueur 2 a gagné la partie!")
        else:
            self.afficher_message("Il y a égalité entre les joueurs!")            