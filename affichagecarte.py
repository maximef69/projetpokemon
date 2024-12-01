from tkinter import *
from PIL import Image, ImageTk
 
main = Tk()
main.geometry("1080x720+100+100")
main.title("Insérer une image")
im = Image.open("C:\\Users\\Max\\OneDrive\\24-25\\ort\\td_dev\\projets\\projet_1\\Cartes\\Aquariel.jpg")
 
photo = ImageTk.PhotoImage(im, master = main)
fond = Label(main, image =photo )
fond.place(x=0,y=0, relwidth = 1, relheight=1)