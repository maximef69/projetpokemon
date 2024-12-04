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

    def __str__(self):
        return (
            f"Nom : {self.nom} - PV: {self.points_de_vie}, "
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

root = Tk()
root.title("Jeu de cartes Pokémon")
root.geometry('1080x720')

frame1 = Frame(root, padx=20, pady=20)
frame1.grid(column=0, row=0, sticky="w")

canvas_carte1 = Canvas(frame1, width=200, height=200, bg='blue')
canvas_carte1.grid(column=0, row=0)

img1 = Image.open("./Cartes/Aquariel.jpg")
img1 = img1.resize((200, 200))  # Redimensionne l'image
myimg1 = ImageTk.PhotoImage(img1)
canvas_carte1.create_image(0, 0, image=myimg1, anchor='nw')

button1 = Button(frame1, text="Choisir", font=("Courier", 10))
button1.grid(column=0, row=1, pady=10)

frame2 = Frame(root, padx=20, pady=20)
frame2.grid(column=0, row=1, sticky="w")

label_title = Label(frame2, text="Information joueur 1", font=("Courier", 20), anchor="w")
label_title.pack()

frame3 = Frame(root, padx=20, pady=20)
frame3.grid(column=0, row=2, sticky="w")

canvas_carte2 = Canvas(frame3, width=200, height=200, bg='blue')
canvas_carte2.grid(column=0, row=0)

img2 = Image.open("./Cartes/Cryovore.jpg")
img2 = img2.resize((200, 200))  
myimg2 = ImageTk.PhotoImage(img2)
canvas_carte2.create_image(0, 0, image=myimg2, anchor='nw')
label_nom = Label(frame3, text=f"PV: {carte2.points_de_vie} | Attaque: {self.attaque}\n"
                 f"Énergie: {self.energie} | Type: {self.type}",)

button2 = Button(frame3, text="Choisir", font=("Courier", 10))
button2.grid(column=0, row=1, pady=10)


carte1 = Carte("Aquariel", 80, 50, 3, "Eau", "./Cartes/Aquariel.jpg")
carte2 = Carte("Cryovore", 90, 60, 4, "Glace", "./Cartes/Cryovore.jpg")



root.mainloop()
