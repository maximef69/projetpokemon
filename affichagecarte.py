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

        self.frame = None
        self.canvas = None
        self.image = None
        self.img = None

    def __str__(self):
        return (
            f"Nom : {self.nom} - PV: {self.points_de_vie}, "
            f"Attaque: {self.attaque}, Énergie: {self.energie}, Type: {self.type}"
        )

    def afficherCarteInfos(self):
        label_infos = Label(
            self.frame,
            text=f"Nom: {self.nom} PV: {self.points_de_vie}  Attaque: {self.attaque}\nÉnergie: 4  Type: {self.type}",
            font=("Arial", 10),
            justify="left",
        )
        label_infos.grid(column=0, row=1, pady=5)

    def afficher(self, frame):
        self.frame = frame
        self.canvas = Canvas(frame, width=200, height=200)
        self.img = Image.open(self.chemin_image).resize((200, 200))
        self.image = ImageTk.PhotoImage(self.img)

        self.canvas.grid(column=0, row=0)
        self.canvas.create_image(0, 0, image=self.image, anchor='nw')
        self.afficherCarteInfos()

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

root = Tk()
root.title("Jeu de cartes Pokémon")
root.geometry('1080x720')
frame1 = Frame(root, padx=20, pady=20)
frame1.grid(column=0, row=0, sticky="w")
frame2 = Frame(root, padx=20, pady=20)
frame2.grid(column=0, row=1, sticky="w", columnspan=100)

label_title = Label(frame2, text="Informations joueur 1", font=("Courier", 20))
label2_title = Label(frame2, text="Informations joueur 2", font=("Courier", 20))
label_title.grid(column=0, row=0)
label2_title.grid(column=1, row=0)

frame3 = Frame(root, padx=20, pady=20)
frame3.grid(column=0, row=2, sticky="w")

carte1 = random.choice(cartes)
carte1.afficher(frame1)
carte2 = random.choice(cartes)
carte2.afficher(frame3)

root.mainloop()
