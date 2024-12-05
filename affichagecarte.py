from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random

class Carte:
    def __init__(self, nom, points_de_vie, attaque, energie, type, chemin_image):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.attaque = attaque
        self.energie = energie
        self.type = type
        self.chemin_image = chemin_image

        self.image = None
        self.img = None

    def afficher(self, frame):
        canvas = Canvas(frame, width=200, height=200)
        self.img = Image.open(self.chemin_image).resize((200, 200))
        self.image = ImageTk.PhotoImage(self.img)
        canvas.create_image(0, 0, image=self.image, anchor='nw')
        canvas.pack()

        label_infos = Label(
            frame,
            text=f"{self.nom}\nPV: {self.points_de_vie} | Attaque: {self.attaque}\nÉnergie: {self.energie} | Type: {self.type}",
            font=("Arial", 12),
            justify="center",
        )
        label_infos.pack()

class Jeu:
    def __init__(self, root, cartes):
        self.root = root
        self.cartes = cartes
        self.joueur1_score = 0
        self.joueur2_score = 0

        self.joueur1_carte = None
        self.joueur2_carte = None

        self.setup_ui()

    def setup_ui(self):
        # Titre
        Label(self.root, text="Jeu de cartes Pokémon", font=("Courier", 24)).pack(pady=10)

        # Zones des joueurs
        self.frame_joueur1 = Frame(self.root, padx=20, pady=20, bg="lightblue")
        self.frame_joueur1.pack(side=LEFT, fill=BOTH, expand=True)

        self.frame_joueur2 = Frame(self.root, padx=20, pady=20, bg="lightpink")
        self.frame_joueur2.pack(side=RIGHT, fill=BOTH, expand=True)

        # Zone centrale pour actions
        self.frame_centrale = Frame(self.root, padx=20, pady=20)
        self.frame_centrale.pack(fill=BOTH, expand=True)

        self.label_resultat = Label(self.frame_centrale, text="", font=("Arial", 14), fg="green")
        self.label_resultat.pack(pady=10)

        self.bouton_combat = Button(
            self.frame_centrale, text="Attaquer !", font=("Arial", 14), command=self.combattre
        )
        self.bouton_combat.pack(pady=10)

        self.bouton_nouvelle_carte = Button(
            self.frame_centrale, text="Nouvelle carte", font=("Arial", 14), command=self.piocher_cartes
        )
        self.bouton_nouvelle_carte.pack(pady=10)

        # Scores
        self.label_score = Label(
            self.frame_centrale, text=f"Score Joueur 1: {self.joueur1_score} | Score Joueur 2: {self.joueur2_score}", font=("Arial", 14)
        )
        self.label_score.pack(pady=10)

        # Initialisation des cartes
        self.piocher_cartes()

    def piocher_cartes(self):
        # Nettoyer les zones de cartes
        for widget in self.frame_joueur1.winfo_children():
            widget.destroy()
        for widget in self.frame_joueur2.winfo_children():
            widget.destroy()

        # Piocher des cartes aléatoires
        self.joueur1_carte = random.choice(self.cartes)
        self.joueur2_carte = random.choice(self.cartes)

        # Afficher les cartes
        Label(self.frame_joueur1, text="Joueur 1", font=("Arial", 16), bg="lightblue").pack()
        self.joueur1_carte.afficher(self.frame_joueur1)

        Label(self.frame_joueur2, text="Joueur 2", font=("Arial", 16), bg="lightpink").pack()
        self.joueur2_carte.afficher(self.frame_joueur2)

        # Réactiver le bouton Combat
        self.bouton_combat.config(state="normal")

        self.label_resultat.config(text="")

    def combattre(self):
        if not self.joueur1_carte or not self.joueur2_carte:
            self.label_resultat.config(text="Les cartes ne sont pas prêtes!", fg="red")
            return

        # Désactiver le bouton Combat
        self.bouton_combat.config(state="disabled")

        # Comparaison des attaques
        if self.joueur1_carte.attaque > self.joueur2_carte.attaque:
            self.joueur1_score += 1
            gagnant = "Joueur 1 gagne ce tour!"
        elif self.joueur1_carte.attaque < self.joueur2_carte.attaque:
            self.joueur2_score += 1
            gagnant = "Joueur 2 gagne ce tour!"
        else:
            gagnant = "Égalité!"

        # Mise à jour de l'interface
        self.label_resultat.config(text=gagnant, fg="green")
        self.label_score.config(
            text=f"Score Joueur 1: {self.joueur1_score} | Score Joueur 2: {self.joueur2_score}"
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

# Lancer l'application
root = Tk()
root.title("Jeu de cartes Pokémon")
root.geometry('1080x720')

jeu = Jeu(root, cartes)

root.mainloop()