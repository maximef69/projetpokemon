##----- Importation des Modules -----##
from tkinter import *



##----- Création de la fenêtre -----##
fen = Tk()
fen.title('Mouvements de la souris')

##----- Création des boutons -----##
bouton_quitter = Button(fen, text='Quitter', command=fen.destroy)
bouton_quitter.grid(row=2, column=1, padx=3, pady=3, sticky=S+W+E)

##---- Création des zones de texte -----##
message = Label(fen, text='Ici du texte.')
message.grid(row=0, column=0, columnspan=2, padx=3, pady=3, sticky=W+E)

##----- Création du canevas -----##
dessin=Canvas(fen, bg="white", width=501, height=501)
dessin.grid(row = 1, column = 0, columnspan = 2, padx=5, pady=5)

##----- Programme principal -----##

fen.mainloop() 