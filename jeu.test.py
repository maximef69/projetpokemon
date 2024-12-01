import tkinter as tk
from tkinter import messagebox
import random

class Carte:
    def __init__(self, nom, points_de_vie, attaque, energie, type):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.attaque = attaque
        self.energie = energie
        self.type = type

    def __str__(self):
        return (
            f"{self.nom} - PV: {self.points_de_vie}, "
            f"Attaque: {self.attaque}, Énergie: {self.energie}, Type: {self.type}"
        )


def GenererCartesAleatoires(nombre_cartes):
    types_cartes = ["Feu", "Eau", "Air", "Terre", "Électrique", "Ténèbres", "Lumière"]
    cartes = []

    for i in range(1, nombre_cartes + 1):
        nom = f"Carte-{i}"
        points_de_vie = random.randint(20, 50)
        attaque = random.randint(5, 15)
        energie = random.randint(1, 10)
        type_carte = random.choice(types_cartes)
        cartes.append(Carte(nom, points_de_vie, attaque, energie, type_carte))

    return cartes


class JeuDeCartesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu de Cartes")

        # Variables pour le jeu
        self.PileJoueur1 = []
        self.PileJoueur2 = []
        self.PileDefausseJoueur1 = []
        self.PileDefausseJoueur2 = []
        self.nombre_tours = 0
        self.tour_actuel = 0

        # Interface utilisateur
        self.label_titre = tk.Label(root, text="Jeu de Cartes", font=("Arial", 16))
        self.label_titre.pack(pady=10)

        self.label_info = tk.Label(root, text="Nombre de tours :")
        self.label_info.pack()

        self.entry_tours = tk.Entry(root)
        self.entry_tours.pack()

        self.bouton_lancer = tk.Button(root, text="Lancer la Partie", command=self.lancer_partie)
        self.bouton_lancer.pack(pady=5)

        self.label_tour = tk.Label(root, text="", font=("Arial", 14))
        self.label_tour.pack(pady=5)

        self.bouton_tour = tk.Button(root, text="Prochain Tour", command=self.prochain_tour, state="disabled")
        self.bouton_tour.pack(pady=5)

        self.text_resultats = tk.Text(root, width=60, height=15, state="disabled")
        self.text_resultats.pack(pady=10)

    def afficher_message(self, message):
        self.text_resultats.config(state="normal")
        self.text_resultats.insert(tk.END, message + "\n")
        self.text_resultats.config(state="disabled")

    def lancer_partie(self):
        try:
            self.nombre_tours = int(self.entry_tours.get())
            if self.nombre_tours <= 0:
                raise ValueError("Le nombre de tours doit être positif.")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre de tours valide.")
            return

        # Initialisation des piles
        cartes = GenererCartesAleatoires(20)
        random.shuffle(cartes)
        self.PileJoueur1 = cartes[:len(cartes)//2]
        self.PileJoueur2 = cartes[len(cartes)//2:]
        self.PileDefausseJoueur1 = []
        self.PileDefausseJoueur2 = []
        self.tour_actuel = 0

        # Mise à jour de l'interface
        self.label_tour.config(text=f"Tour 0 / {self.nombre_tours}")
        self.text_resultats.config(state="normal")
        self.text_resultats.delete(1.0, tk.END)
        self.text_resultats.config(state="disabled")
        self.bouton_tour.config(state="normal")
        self.afficher_message("La partie commence !")

    def prochain_tour(self):
        if self.tour_actuel >= self.nombre_tours or not self.PileJoueur1 or not self.PileJoueur2:
            self.fin_partie()
            return

        self.tour_actuel += 1
        self.label_tour.config(text=f"Tour {self.tour_actuel} / {self.nombre_tours}")

        # Extraire les cartes
        CarteJoueur1 = self.PileJoueur1.pop(0)
        CarteJoueur2 = self.PileJoueur2.pop(0)

        # Résultat du duel
        self.afficher_message(f"Tour {self.tour_actuel}:")
        self.afficher_message(f"  Joueur 1: {CarteJoueur1}")
        self.afficher_message(f"  Joueur 2: {CarteJoueur2}")

        if CarteJoueur1.attaque > CarteJoueur2.attaque:
            self.PileDefausseJoueur1.append(CarteJoueur2)
            self.afficher_message(f"  Joueur 1 gagne le duel avec {CarteJoueur1.nom} !")
        elif CarteJoueur1.attaque < CarteJoueur2.attaque:
            self.PileDefausseJoueur2.append(CarteJoueur1)
            self.afficher_message(f"  Joueur 2 gagne le duel avec {CarteJoueur2.nom} !")
        else:
            self.PileJoueur1.append(CarteJoueur1)
            self.PileJoueur2.append(CarteJoueur2)
            self.afficher_message(f"  Égalité entre {CarteJoueur1.nom} et {CarteJoueur2.nom} !")

        self.afficher_message("")

        # Vérifier si la partie est terminée
        if not self.PileJoueur1 or not self.PileJoueur2:
            self.fin_partie()

    def fin_partie(self):
        self.bouton_tour.config(state="disabled")

        TailleJoueur1 = len(self.PileDefausseJoueur1)
        TailleJoueur2 = len(self.PileDefausseJoueur2)

        self.afficher_message("\n*** Résultats finaux ***")
        self.afficher_message(f"Cartes remportées par Joueur 1: {TailleJoueur1}")
        self.afficher_message(f"Cartes remportées par Joueur 2: {TailleJoueur2}")

        if TailleJoueur1 > TailleJoueur2:
            self.afficher_message("Joueur 1 a gagné la partie!")
        elif TailleJoueur1 < TailleJoueur2:
            self.afficher_message("Joueur 2 a gagné la partie!")
        else:
            self.afficher_message("Il y a égalité entre les joueurs!")

        messagebox.showinfo("Partie terminée", "La partie est terminée !")


# Lancer l'application
root = tk.Tk()
app = JeuDeCartesApp(root)
root.mainloop()
