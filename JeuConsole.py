import random

class Carte:
    def __init__(self, nom, points_de_vie, attaque, energie, type, chemin_image):
        
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.attaque = attaque
        self.energie = energie
        self.type = type
        self.chemin_image = chemin_image

    def __str__(self):
        return (
            f"Nom :{self.nom} - PV: {self.points_de_vie}, "
            f"Attaque: {self.attaque}, Énergie: {self.energie}, Type: {self.type}"
        )

# Création des cartes 
cartes = [
    Carte("Aquariel", 25, 3, 1, "Eau", "./Cartes/Aquariel.jpg"),
    Carte("Ardwind", 30, 10, 5, "Feu", "./Cartes/ardwind.jpg"),
    Carte("Auradyn", 90, 8, 5, "Eau", "./Cartes/Auradyn.jpg"),
    Carte("Chromilex", 45, 4, 3, "Plante", "./Cartes/Chromilex.jpg"),
    Carte("Cryovore", 15, 5, 4, "Eau", "./Cartes/Cryovore.jpg"),
    Carte("Cryowind", 60, 3, 2, "Eau", "./Cartes/Cryowind.jpg"),
    Carte("Eclipserra", 85, 4, 3, "Feu", "./Cartes/Eclipserra.jpg"),
    Carte("Fulgorion", 55, 7, 5, "Plante", "./Cartes/Fulgorion.jpg"),
    Carte("Fulgoryx", 95, 9, 5, "Feu", "./Cartes/Fulgoryx.jpg"),
    Carte("Lumysol", 20, 3, 2, "Plante", "./Cartes/Lumysol.jpg"),
    Carte("Lunargent", 10, 2, 1, "Eau", "./Cartes/Lunargent.jpg"),
    Carte("Nebulo", 35, 3, 3, "Eau", "./Cartes/Nebulo.jpg"),
    Carte("Obscurion", 45, 4, 3, "Feu", "./Cartes/Obscurion.jpg"),
    Carte("Shadowis", 75, 6, 4, "Feu", "./Cartes/Shadowis.jpg"),
    Carte("Solairis", 80, 10, 4, "Feu", "./Cartes/Solairis.jpg"),
    Carte("Solfang", 40, 4, 3, "Plante", "./Cartes/Solfang.jpg"),
    Carte("Terragos", 15, 3, 1, "Plante", "./Cartes/Terragos.jpg"),
    Carte("Tornalyx", 60, 10, 5, "Eau", "./Cartes/Tornalyx.jpg"),
    Carte("Venoxis", 40, 6, 3, "Plante", "./Cartes/Venoxis.jpg"),
    Carte("Voltaryx", 30, 9, 4, "Feu", "./Cartes/Voltaryx.jpg")
]

class Joueur:
    def __init__(self):
        self.pile = []
        self.defausse = []
        self.mana = 0
        self.nom = ""

class Jeu:
    def __init__(self):
        # Variables pour le jeu
        self.Joueur1 = Joueur()
        self.Joueur2 = Joueur()
        self.nombre_tours = 0
        self.tour_actuel = 0

    def DistributionEtMelangeDesCartes(self, cartes):
        """
        Mélange les cartes et les distribue entre les deux joueurs :
        - Joueur 1 reçoit les cartes aux indices pairs.
        - Joueur 2 reçoit les cartes aux indices impairs.
        """
        random.shuffle(cartes)  # Mélanger les cartes
        # Distribution des cartes 
        self.Joueur1.pile = [cartes[i] for i in range(len(cartes)) if i % 2 == 0]# indices pairs
        self.Joueur2.pile = [cartes[i] for i in range(len(cartes)) if i % 2 != 0]# indice impairs

    def LancerPartie(self):
        """
        Demande au joueur d'indiquer le nombre de tours et initialise le jeu.
        """
        while True:
            try:
                self.nombre_tours = int(input("Saisir un nombre de tours : "))
                if self.nombre_tours > 0:
                    break
                print("Veuillez saisir un nombre de tours positif.")
            except ValueError:
                print("Entrée invalide. Veuillez saisir un nombre entier positif.")
        
        self.Joueur1.mana = 2
        self.Joueur2.mana = 2
        print("-------------La partie commence-------------")
        print("Vous disposez de 2 points d'énergie")
        
                
    def RechercheCarte(self, pile, nom, joueurmana):
        
        """
        Retourne la carte demandée si le joueur dispose assez d'énergie.
        
        """

        for carte in pile:
            if nom == carte.nom :
                if carte.energie > joueurmana:
                    print("Vous n'avez assez d'énergie pour choisir cette carte")
                    return None
                else:
                    return carte
        return None

    def ComparaisonTypes(self, type1, type2):
        """Compare le type des cartes, Feu bat Plante, Plante bat Eau, Eau bat Feu.
        
        Et retourne le numéro du joueur vainqueur.
        """
        
        
        vainqueur = 0
        if type1 == type2:
            return vainqueur
        match type1, type2 :
            case "Feu", "Plante":
                vainqueur = 1
            case "Plante","Feu":
                vainqueur = 2                
            case "Eau", "Feu":
                vainqueur = 1
            case "Feu","Eau":
                vainqueur = 2    
            case "Plante", "Eau":
                vainqueur = 1
            case "Eau","Plante":
                vainqueur = 2 
        return vainqueur  
    
    def AfficherCartes(self):
        print(f"\n############## {self.Joueur1.nom}################")
        for carte in self.Joueur1.pile:
            print(carte)
        print(f"Energie de {self.Joueur1.nom} : {self.Joueur1.mana}")
        print("\n########################################\n")
        print(f"##############{self.Joueur2.nom}################")
        for carte in self.Joueur2.pile:
            print(carte)
        print(f"Energie de {self.Joueur2.nom} : {self.Joueur2.mana}")
        print("########################################")
               
    def AvantageCarte(self, carte1, carte2):          
        avantage = self.ComparaisonTypes(carte1.type, carte2.type)
        if avantage == 1:
            print(f"{carte1.nom} a un avantage de type ! Bonus de 50% sur l'attaque.")
            carte1.attaque *= 1.5
        elif avantage == 2:
            print(f"{carte2.nom} a un avantage de type ! Bonus de 50% sur l'attaque.")
            carte2.attaque *= 1.5
        
    def AttaqueCarte(self, carte1, carte2):
        # Le joueur 1 gagne le duel
        if carte1.attaque > carte2.attaque:
            self.Joueur1.defausse.append(carte2)
            self.Joueur1.pile.append(carte1)
            print(f"Joueur 1 gagne avec {carte1.nom} !")
        # Le joueur 2 gagne le duel
        elif carte1.attaque < carte2.attaque:
            self.Joueur2.defausse.append(carte1)
            self.Joueur2.pile.append(carte2)
            print(f"Joueur 2 gagne avec {carte2.nom} !")
        # Egalité entre les joueurs
        else:
            self.Joueur1.pile.append(carte1)
            self.Joueur2.pile.append(carte2)
            print(f"Égalité entre {carte1.nom} et {carte2.nom} !")
        
    def ChoisirCarte(self,joueur):
        carte = None  
        while carte == None:
            choix = input(f"{joueur.nom}: Saisir le nom de la carte ou entrer 'Passe' pour passer votre tour  ")
            if choix == "Passe":
                return None
            carte = self.RechercheCarte(joueur.pile, choix, joueur.mana)
            if carte == None:
                print("Erreur, veuillez ressaisir une carte valide.")
            else:
                joueur.mana = joueur.mana - carte.energie # On soustrait l'énergie de joueur par l'énergie de la carte
                joueur.pile.remove(carte)   # La carte du joueur est enlevée de sa main pour rentrer en duel
        return carte
        
    def ResoudreDuel(self, carte1, carte2):
        # Le joueur 1 passe son tour et le joueur 2 joue une carte
        if carte1 == None and carte2 != None:
                print(f"\nTour {self.tour_actuel + 1} passé par le joueur : {self.Joueur1.nom}")
                lenPile = len(self.Joueur1.pile) - 1
                carteApop = random.randint(0, lenPile)
                self.Joueur2.pile.append(carte2)
                self.Joueur2.defausse.append(self.Joueur1.pile.pop(carteApop))

        # Le joueur 2 passe son tour et le joueur 1 joue une carte
        elif carte2 == None and carte1 != None:
                print(f"\nTour {self.tour_actuel + 1} passé par le joueur : {self.Joueur2.nom}")
                lenPile = len(self.Joueur2.pile) - 1
                carteApop = random.randint(0, lenPile)
                self.Joueur1.pile.append(carte1)
                self.Joueur1.defausse.append(self.Joueur2.pile.pop(carteApop))
                
        # Les deux joueurs ont passé leur tour.
        elif carte2 == None and carte1 == None:
                print(f"\nTour {self.tour_actuel + 1} passé par les 2 joueurs")
                print("Aucune action sera effectuée.")
                
        # Les deux joueurs jouent une carte.
        elif carte1 != None and carte2 != None: 
                print(f"\nTour {self.tour_actuel + 1}:")
                print(f"  Joueur 1: {carte1}")
                print(f"  Joueur 2: {carte2}")
                
                self.AvantageCarte(carte1, carte2)            
                self.AttaqueCarte(carte1, carte2)
        

    def DuelCarte(self):
        """
        Réalise un duel entre la première carte de chaque joueur.
        """
        self.AfficherCartes()
        if not self.Joueur1.pile or not self.Joueur2.pile:
            print("Un des joueurs n'a plus de cartes. Fin du jeu.")
            return
        
        CarteJoueur1 = self.ChoisirCarte(self.Joueur1)
        CarteJoueur2 = self.ChoisirCarte(self.Joueur2)
        
        self.ResoudreDuel(CarteJoueur1, CarteJoueur2)

        self.Joueur1.mana += 2
        self.Joueur2.mana += 2
        self.tour_actuel += 1

    def FinPartie(self):
        """
        Affiche les résultats finaux et déclare le vainqueur.
        """
        print("\n******** Résultats finaux *********")
        TailleJoueur1 = len(self.Joueur1.defausse)
        TailleJoueur2 = len(self.Joueur2.defausse)

        print(f"Cartes remportées par Joueur 1: {TailleJoueur1}")
        print(f"Cartes remportées par Joueur 2: {TailleJoueur2}")

        if TailleJoueur1 > TailleJoueur2:
            print(f"{self.Joueur1.nom} a gagné la partie!")
        elif TailleJoueur1 < TailleJoueur2:
            print(f"{self.Joueur2.nom} a gagné la partie!")
        else:
            print(f"Il y a égalité entre {self.Joueur1.nom} et {self.Joueur2.nom} !")

    def Jouer(self, cartes):
        """
        Gère le déroulement du jeu.
        """

        self.Joueur1.nom = input("Joueur 1 : Saisir votre nom :  ")#Saisie du nom du joueur1
        self.Joueur2.nom = input("Joueur 2 : Saisir votre nom :  ")#Saisie du nom du joueur2
        
        self.DistributionEtMelangeDesCartes(cartes)
        self.LancerPartie()

        while self.tour_actuel < self.nombre_tours and self.Joueur1.pile and self.Joueur2.pile:
            self.DuelCarte()

        self.FinPartie()

# Début
jeu = Jeu()
jeu.Jouer(cartes)

