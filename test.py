from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


root = Tk()
root.title("Jeu de cartes Pokemon")
root.geometry('1000x1000')

canvas = Canvas(root)
canvas.grid(column=0, row=0, sticky=(N, W, E, S))
img = Image.open("./Cartes/Aquariel.jpg")
img = img.resize((200, 200))
myimg = ImageTk.PhotoImage(img)
canvas.create_image(10, 10, image=myimg, anchor='nw')

canvas2 = Canvas(root)
canvas2.grid(column=0, row=200, sticky=(N, W, E, S))
img2 = Image.open("./Cartes/Cryovore.jpg")
img2 = img2.resize((200, 200))
myimg2 = ImageTk.PhotoImage(img2)
canvas2.create_image(10, 10, image=myimg2, anchor='nw')






root.mainloop()