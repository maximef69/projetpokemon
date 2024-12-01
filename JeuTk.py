import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class GUIJeu:
    def __init__(self, root, jeu):
        self.root = root
        self.jeu = jeu
        self.setup_ui()
        self.jeu.DistributionEtMelangeDesCartes(cartes)
        self.jeu.LancerPartie()
        self.update_ui()

    def setup_ui(self):
        # Configuration de la fenêtre principale
        self.root.title("Jeu de Cartes")
        self.root.geometry("800x600")

        # Sections pour les deux joueurs
        self.frame_joueur1 = tk.Frame(self.root, bg="lightblue", width=300, height=500)
        self.frame_joueur1.grid(row=0, column=0, sticky="nsew")

        self.frame_centre = tk.Frame(self.root, bg="white", width=200, height=500)
        self.frame_centre.grid(row=0, column=1, sticky="nsew")

        self.frame_joueur2 = tk.Frame(self.root, bg="lightgreen", width=300, height=500)
        self.frame_joueur2.grid(row=0, column=2, sticky="nsew")

        # Ajout des noms des joueurs
        self.label_joueur1 = tk.Label(self.frame_joueur1, text="Joueur 1", bg="lightblue", font=("Arial", 14))
        self.label_joueur1.pack(pady=10)
        
        self.label_joueur2 = tk.Label(self.frame_joueur2, text="Joueur 2", bg="lightgreen", font=("Arial", 14))
        self.label_joueur2.pack(pady=10)

        # Zone pour afficher les cartes
        self.carte_joueur1 = tk.Label(self.frame_joueur1, text="Carte Joueur 1", bg="lightblue", font=("Arial", 12))
        self.carte_joueur1.pack(pady=20)

        self.carte_joueur2 = tk.Label(self.frame_joueur2, text="Carte Joueur 2", bg="lightgreen", font=("Arial", 12))
        self.carte_joueur2.pack(pady=20)

        # Boutons d'interaction
        self.bouton_jouer = tk.Button(self.frame_centre, text="Jouer", command=self.jouer_tour)
        self.bouton_jouer.pack(pady=10)

        self.bouton_passer = tk.Button(self.frame_centre, text="Passer", command=self.passer_tour)
        self.bouton_passer.pack(pady=10)

        # Zone d'information
        self.zone_info = tk.Text(self.frame_centre, height=20, width=40)
        self.zone_info.pack(pady=10)

    def update_ui(self):
        # Mise à jour des informations sur l'interface
        self.label_joueur1.config(text=f"{self.jeu.Joueur1.nom} (Énergie: {self.jeu.Joueur1.mana})")
        self.label_joueur2.config(text=f"{self.jeu.Joueur2.nom} (Énergie: {self.jeu.Joueur2.mana})")
        self.afficher_cartes()

    def afficher_cartes(self):
        # Met à jour les cartes dans l'interface
        self.zone_info.delete("1.0", tk.END)
        self.zone_info.insert(tk.END, f"Cartes Joueur 1: {[carte.nom for carte in self.jeu.Joueur1.pile]}\n")
        self.zone_info.insert(tk.END, f"Cartes Joueur 2: {[carte.nom for carte in self.jeu.Joueur2.pile]}\n")

    def jouer_tour(self):
        # Gestion du tour : Demander les cartes et résoudre le duel
        if not self.jeu.Joueur1.pile or not self.jeu.Joueur2.pile:
            messagebox.showinfo("Fin du jeu", "Un des joueurs n'a plus de cartes.")
            self.jeu.FinPartie()
            return

        carte_j1 = self.jeu.ChoisirCarte(self.jeu.Joueur1)
        carte_j2 = self.jeu.ChoisirCarte(self.jeu.Joueur2)
        self.jeu.ResoudreDuel(carte_j1, carte_j2)
        self.update_ui()

    def passer_tour(self):
        # Gestion du passage de tour
        self.jeu.ResoudreDuel(None, None)
        self.update_ui()

# Initialisation du jeu
if __name__ == "__main__":
    jeu = Jeu()
    root = tk.Tk()
    app = GUIJeu(root, jeu)
    root.mainloop()
