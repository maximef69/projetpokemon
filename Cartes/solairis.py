import pygame
import sys

# Initialiser Pygame
pygame.init()

# Dimensions de la fenêtre
largeur, hauteur = 600, 800
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Carte Pokémon")

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
BLEU = (0, 0, 255)
JAUNE = (255, 255, 0)
ROUGE = (255, 0, 0)
ORANGE = (255, 128, 0)

# Définir la police
font_title = pygame.font.Font(None, 40)   # Police pour le titre
font_subtitle = pygame.font.Font(None, 30) # Police pour le sous-titre
font_text = pygame.font.Font(None, 24)     # Police pour le texte

# Charger une image pour le Pokémon
pokemon_image = pygame.image.load("Solairis.jpg")
pokemon_image = pygame.transform.scale(pokemon_image, (300, 300))  # Redimensionner l'image

# Données de la carte Pokémon
pokemon_nom = "Solairis"
pokemon_type = "Feu"
pokemon_pv = 90
attaque_1 = "Éxplosion de chaleur"
atk_1_degats = 60
description = "Desciption : Pokemon solaire majestueux, dont l'aura brûlante peut incinérer quiconque s'aventure trop près. Il est vénéré dans de nombreuses légendes anciennes"

# Fonction pour dessiner la carte Pokémon
def draw_card():
    # Remplir l'arrière-plan
    screen.fill(ORANGE)

    # Dessiner la bordure de la carte
    pygame.draw.rect(screen, NOIR, (10, 10, largeur - 20, hauteur - 20), 5)

    # Dessiner le nom du Pokémon
    title_text = font_title.render(pokemon_nom, True, NOIR)
    screen.blit(title_text, (250, 30))

    # Dessiner le type du Pokémon
    type_text = font_subtitle.render(f"Type: {pokemon_type}", True, NOIR)
    screen.blit(type_text, (30, 80))

    # Dessiner les PV
    pv_text = font_subtitle.render(f"PV: {pokemon_pv}", True, NOIR)
    screen.blit(pv_text, (30, 120))

    # Dessiner l'image du Pokémon
    screen.blit(pokemon_image, (150, 200))

    # Dessiner les attaques
    attaque_1_text = font_text.render(f"Attaque 1: {attaque_1} ({atk_1_degats} dégats)", True, NOIR)
    screen.blit(attaque_1_text, (30, 510))

    # Dessiner la barre de points de vie
    pygame.draw.rect(screen, NOIR, (30, 150, 200, 30))  # Barre de fond
    pygame.draw.rect(screen, ROUGE, (30, 150, 200 * (pokemon_pv / 100), 30))  # Barre de vie
    pygame.draw.rect(screen, NOIR, (30, 150, 200, 30), 3)  # Contour de la barre de vie
    
    #Dessiner la description
    type_text = font_text.render(description, True, NOIR)
    screen.blit(type_text, (30, 580))

    # Mettre à jour l'écran
    pygame.display.flip()

# Boucle principale du jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dessiner la carte
    draw_card()

    # Limiter le taux de rafraîchissement
    pygame.time.Clock().tick(30)

# Quitter Pygame
pygame.quit()
sys.exit()
