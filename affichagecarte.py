from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

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

root = Tk()
root.title("Jeu de cartes Pokémon")
root.geometry('1080x720')

frame1 = Frame(root, padx=20, pady=20)
frame1.grid(column=0, row=0, sticky="w")

canvas_carte1 = Canvas(frame1, width=200, height=200, bg='blue')
canvas_carte1.grid(column=0, row=0)

img1 = Image.open("./Cartes/Aquariel.jpg")
img1 =img1.resize((200, 200)) 
myimg1 = ImageTk.PhotoImage(img1)
canvas_carte1.create_image(0, 0, image=myimg1, anchor='nw')

label_infos = Label(
    frame1,
    text="Nom: Cryovore PV: 90  Attaque: 60\nÉnergie: 4  Type: Glace",
    font=("Arial", 10),
    justify="left",
)
label_infos.grid(column=0, row=1, pady=5)

button1 = Button(frame1, text="Choisir", font=("Courier", 10))
button1.grid(column=0, row=2, pady=10)

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

label_infos = Label(
    frame3,
    text="Nom: Aquariel PV: 80  Attaque: 50\nÉnergie: 3  Type: Eau",
    font=("Arial", 10),
    justify="left",
)
label_infos.grid(column=0, row=1, pady=5)

button2 = Button(frame3, text="Choisir", font=("Courier", 10))
button2.grid(column=0, row=2, pady=10)

carte1 = Carte("Aquariel", 80, 50, 3, "Eau", "./Cartes/Aquariel.jpg")
carte2 = Carte("Cryovore", 90, 60, 4, "Glace", "./Cartes/Cryovore.jpg")

root.mainloop()
