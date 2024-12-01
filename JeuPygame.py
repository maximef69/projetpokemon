import pygame
import tkinter as tk


# 1. Initialiser Tkinter
# Créer la fenêtre principale Tkinter
root = tk.Tk()

# Définir les dimensions et le titre de la fenêtre
root.title("Fenêtre Tkinter avec Pygame")
root.geometry("800x600")  # Taille de la fenêtre

# 2. Ajouter un canevas Tkinter dans la fenêtre principale
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

# 3. Initialiser Pygame
pygame.init()

# Créer une surface Pygame qui sera affichée sur le canevas Tkinter
pygame_screen = pygame.Surface((800, 600))  # Créer une surface Pygame avec les mêmes dimensions que le canevas

# 4. Initialiser la fenêtre Pygame pour le rendu dans le canevas Tkinter
def update_pygame_surface():
    # Remplir la surface Pygame avec une couleur (par exemple, un fond bleu)
    pygame_screen.fill((0, 0, 255))
    
    # Ajouter d'autres éléments graphiques avec Pygame (ex: un cercle rouge)
    pygame.draw.circle(pygame_screen, (255, 0, 0), (400, 300), 50)
    
    # Convertir l'image Pygame en un format compatible avec Tkinter
    pygame_image = pygame.image.tostring(pygame_screen, 'RGB')
    tk_image = tk.PhotoImage(width=800, height=600, data=pygame_image)
    
    # Afficher l'image sur le canevas Tkinter
    canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)

    # Mettre à jour l'image à chaque 30ms (pour avoir une animation fluide)
    root.after(30, update_pygame_surface)

# Démarrer la mise à jour de la surface Pygame dans la fenêtre Tkinter
update_pygame_surface()

# Lancer la boucle principale de l'interface Tkinter
root.mainloop()
