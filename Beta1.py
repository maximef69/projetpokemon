import random
import pygame

# Initialisation de Pygame
pygame.init()

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)

# Taille de l'écran
LARGEUR = 800
HAUTEUR = 600
TAILLE_CARTE = (100, 150)

# Configuration de l'écran
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Jeu de Cartes")

# Polices
police = pygame.font.Font(None, 24)

# Définition de la classe Carte
class Carte:
    def __init__(self, nom, points_de_vie, attaque, energie, type, chemin_image):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.attaque = attaque
        self.energie = energie
        self.type = type
        self.chemin_image = chemin_image
        self.image = pygame.image.load(chemin_image)
        self.image = pygame.transform.scale(self.image, TAILLE_CARTE)

    def __str__(self):
        return (
            f"Nom : {self.nom} - PV: {self.points_de_vie}, "
            f"Attaque: {self.attaque}, Énergie: {self.energie}, Type: {self.type}"
        )

# Classe Joueur
class Joueur:
    def __init__(self):
        self.pile = []
        self.defausse = []
        self.mana = 0
        self.nom = ""

# Classe Jeu
class Jeu:
    def __init__(self):
        self.Joueur1 = Joueur()
        self.Joueur2 = Joueur()
        self.nombre_tours = 0
        self.tour_actuel = 0

    def DistributionEtMelangeDesCartes(self, cartes):
        random.shuffle(cartes)
        self.Joueur1.pile = [cartes[i] for i in range(len(cartes)) if i % 2 == 0]
        self.Joueur2.pile = [cartes[i] for i in range(len(cartes)) if i % 2 != 0]

    def LancerPartie(self):
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
        for carte in pile:
            if nom == carte.nom:
                if carte.energie > joueurmana:
                    print("Vous n'avez pas assez d'énergie pour choisir cette carte.")
                    return None
                else:
                    return carte
        return None

    def AfficherCartes(self):
        # Affichage des cartes des joueurs sur l'écran Pygame
        print(f"\n############## {self.Joueur1.nom} ################")
        for carte in self.Joueur1.pile:
            print(carte)
        print(f"Energie de {self.Joueur1.nom} : {self.Joueur1.mana}")
        print("\n########################################\n")
        print(f"############## {self.Joueur2.nom} ################")
        for carte in self.Joueur2.pile:
            print(carte)
        print(f"Energie de {self.Joueur2.nom} : {self.Joueur2.mana}")
        print("########################################")
                
    def ChoisirCarte(self, joueur):
        carte = None
        while carte == None:
            choix = input(f"{joueur.nom}: Saisir le nom de la carte ou entrer 'Passe' pour passer votre tour")
            if choix == "Passe":
                return None
            carte = self.RechercheCarte(joueur.pile, choix, joueur.mana)
            if carte == None:
                print("Erreur, veuillez ressaisir une carte valide.")
            else:
                joueur.mana -= carte.energie
                joueur.pile.remove(carte)
        return carte
        
    def ResoudreDuel(self, carte1, carte2):
        if carte1 and carte2:
            print(f"{carte1.nom} attaque {carte2.nom}")
            if carte1.attaque > carte2.attaque:
                self.Joueur1.defausse.append(carte2)
                self.Joueur1.pile.append(carte1)
                print(f"Joueur 1 gagne avec {carte1.nom} !")
            elif carte1.attaque < carte2.attaque:
                self.Joueur2.defausse.append(carte1)
                self.Joueur2.pile.append(carte2)
                print(f"Joueur 2 gagne avec {carte2.nom} !")
            else:
                self.Joueur1.pile.append(carte1)
                self.Joueur2.pile.append(carte2)
                print(f"Égalité entre {carte1.nom} et {carte2.nom} !")

    def DuelCarte(self):
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
        TailleJoueur1 = len(self.Joueur1.defausse)
        TailleJoueur2 = len(self.Joueur2.defausse)

        print(f"Cartes remportées par Joueur 1: {TailleJoueur1}")
        print(f"Cartes remportées par Joueur 2: {TailleJoueur2}")

        if TailleJoueur1 > TailleJoueur2:
            print("Joueur 1 a gagné la partie!")
        elif TailleJoueur1 < TailleJoueur2:
            print("Joueur 2 a gagné la partie!")
        else:
            print("Il y a égalité entre les joueurs!")

    def Jouer(self, cartes):
        self.Joueur1.nom = input("Joueur 1 : Saisir votre nom: ")
        self.Joueur2.nom = input("Joueur 2 : Saisir votre nom: ")
        
        self.DistributionEtMelangeDesCartes(cartes)
        self.LancerPartie()

        while self.tour_actuel < self.nombre_tours and self.Joueur1.pile and self.Joueur2.pile:
            self.DuelCarte()

        self.FinPartie()

# Début de la partie
jeu = Jeu()
cartes = [
    Carte("Aquariel", 25, 3, 1, "Eau", "C:/Users/Max/OneDrive/24-25/ort/td_dev/projets/projet_1/Cartes/Aquariel.jpg"),
    Carte("Ardwind", 30, 10, 5, "Feu", "C:/Users/Max/OneDrive/24-25/ort/td_dev/projets/projet_1/Cartes/ardwind.jpg"),
    Carte("Auradyn", 90, 8, 5, "Eau", "C:/Users/Max/OneDrive/24-25/ort/td_dev/projets/projet_1/Cartes/Auradyn.jpg"),
    Carte("Chromilex", 45, 4, 3, "Plante", "C:/Users/Max/OneDrive/24-25/ort/td_dev/projets/projet_1/Cartes/Chromilex.jpg"),
    Carte("Cryovore", 15, 5, 4, "Eau", "C:/Users/Max/OneDrive/24-25/ort/td_dev/projets/projet_1/Cartes/Cryovore.jpg"),
    Carte("Cryowind", 60, 3, 2, "Eau", "C:/Users/Max/OneDrive/24-25/ort/td_dev/projets/projet_1/Cartes/Cryowind.jpg"),
    Carte("Eclipserra", 85, 4, 3, "Feu", "C:/Users/Max/OneDrive/24-25/ort/td_dev/projets/projet_1/Cartes/Eclipserra.jpg"),
    Carte("Fulgorion", 55, 7, 5, "Plante", "C:/Users/Max/OneDrive/24-25/ort/td_dev/projets/projet_1/Cartes/Fulgorion.jpg"),
    Carte("Fulgoryx", 95, 9, 5, "Feu", "C:/Users/Max/OneDrive/24-25/ort/td_dev/projets/projet_1/Cartes/Fulgoryx.jpg"),
    Carte("Lumysol", 20, 3, 2, "Plante", "C:/Users/Max/OneDrive/24-25/ort/td_dev/projets/projet_1/Cartes/Lumysol.jpg"),
    Carte("Lunargent", 10, 2, 1, "Eau", "C:/Users/Max/OneDrive/24-25/ort/td_dev/projets/projet_1/Cartes/Lunargent.jpg"),
    Carte("Nebulo", 35, 3, 3, "Eau", "C:/Users/Max/OneDrive/24-25/ort/td_dev/projets/projet_1/Cartes/Nebulo.jpg"),
    Carte("Obscurion", 45, 4, 3, "Feu", "C:/Users/Max/OneDrive/24-25/ort/td_dev/projets/projet_1/Cartes/Obscurion.jpg"),
    Carte("Shadowis", 75, 6, 4, "Feu", "C:/Users/Max/OneDrive/24-25/ort/td_dev/projets/projet_1/Cartes/Shadowis.jpg"),
    Carte("Solairis", 80, 10, 4, "Feu", "C:/Users/Max/OneDrive/24-25/ort/td_dev/projets/projet_1/Cartes/Solairis.jpg"),
    Carte("Solfang", 40, 4, 3, "Plante", "C:/Users/Max/OneDrive/24-25/ort/td_dev/projets/projet_1/Cartes/Solfang.jpg"),
    Carte("Terragos", 15, 3, 1, "Plante", "C:/Users/Max/OneDrive/24-25/ort/td_dev/projets/projet_1/Cartes/Terragos.jpg"),
    Carte("Tornalyx", 60, 10, 5, "Eau", "C:/Users/Max/OneDrive/24-25/ort/td_dev/projets/projet_1/Cartes/Tornalyx.jpg"),
    Carte("Venoxis", 40, 6, 3, "Plante", "C:/Users/Max/OneDrive/24-25/ort/td_dev/projets/projet_1/Cartes/Venoxis.jpg"),
    Carte("Voltaryx", 30, 9, 4, "Feu", "C:/Users/Max/OneDrive/24-25/ort/td_dev/projets/projet_1/Cartes/Voltaryx.jpg")
]

jeu.Jouer(cartes)
