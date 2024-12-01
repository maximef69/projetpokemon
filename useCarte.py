import pygame


class Carte:
    def __init__(self, nom, points_de_vie, attaque, energie, type, chemin_image):
        """
        Initialise une carte.
        :param nom: Nom de la carte
        :param points_de_vie: Points de vie de la carte
        :param attaque: Valeur d'attaque
        :param energie: Énergie requise
        :param type: Type de la carte (Feu, Eau, Plante, etc.)
        :param chemin_image: Chemin de l'image associée à la carte
        """
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.attaque = attaque
        self.energie = energie
        self.type = type
        self.chemin_images = chemin_image

        # Chargement de l'image avec Pygame
        try:
            self.image = pygame.image.load(chemin_image)  # Charge l'image
        except pygame.error as e:
            print(f"Erreur lors du chargement de l'image pour {nom}: {e}")
            self.image = None  # Met à None si le chargement échoue

    def afficher(self, surface, position):
        """
        Affiche l'image de la carte sur une surface donnée.
        :param surface: Surface Pygame où dessiner l'image
        :param position: Tuple (x, y) pour la position d'affichage
        """
        if self.image:
            surface.blit(self.image, position)
        else:
            print(f"Aucune image chargée pour {self.nom}")

    def __str__(self):
        return (
            f"{self.nom} - PV: {self.points_de_vie}, "
            f"Attaque: {self.attaque}, Énergie: {self.energie}, Type: {self.type}"
        )


# # Exemple de création de cartes
carte1 = Carte("Dragon de Feu", 30, 8, 3, "Feu", "C:/Users/Max/OneDrive/24-25/ort/td_dev/projets/projet_1/Ressources/Ressources/images/dragon_feu.png")
carte2 = Carte("Hydre Aquatique", 25, 6, 2, "Eau", "C:/Users/Max/OneDrive/24-25/ort/td_dev/projets/projet_1/Ressources/Ressources/images/Foretoress.png")


# Afficher les cartes dans une fenêtre Pygame

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
screen = pygame.display.set_mode((1400, 800))
pygame.display.set_caption("Jeu de Cartes")

# Couleur de fond
background_color = (30, 30, 30)

# Liste de cartes pour affichage
cartes = [carte1, carte2]

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Remplir l'écran avec une couleur de fond
    screen.fill(background_color)

    # Afficher les cartes
    x, y = 50, 50
    for carte in cartes:
        carte.afficher(screen, (x, y))
        x += 300  # Décaler chaque carte horizontalement pour éviter les superpositions

    # Mettre à jour l'écran
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
