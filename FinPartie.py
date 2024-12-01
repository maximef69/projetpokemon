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


def DeroulementTour(PileJoueur1, PileJoueur2, PileDefausseJoueur1, PileDefausseJoueur2):
    if not PileJoueur1 or not PileJoueur2:
        return False  # Fin de partie si une pile est vide

    # Extraire la première carte de chaque pile
    CarteJoueur1 = PileJoueur1.pop(0)
    CarteJoueur2 = PileJoueur2.pop(0)

    # Afficher les cartes en duel
    print(f"Carte du Joueur 1: {CarteJoueur1}")
    print(f"Carte du Joueur 2: {CarteJoueur2}")

    # Comparer la valeur d'attaque des deux cartes
    if CarteJoueur1.attaque > CarteJoueur2.attaque:
        
        PileDefausseJoueur1.append(CarteJoueur2)
        print(f"Joueur 1 gagne le duel avec {CarteJoueur1.nom}!")
        
    elif CarteJoueur1.attaque < CarteJoueur2.attaque:
        
        PileDefausseJoueur2.append(CarteJoueur1)
        print(f"Joueur 2 gagne le duel avec {CarteJoueur2.nom}!")
    else:
        
        PileJoueur1.append(CarteJoueur1)
        PileJoueur2.append(CarteJoueur2)
        print(f"Égalité entre {CarteJoueur1.nom} et {CarteJoueur2.nom}!")

    print(f"--------- Fin du Tour -------\n")
    return True  # Indique que la partie peut continuer


def FinPartie(nCompteurTour):
    # Générer et mélanger les cartes
    cartes = GenererCartesAleatoires(20)  # Exemple avec 20 cartes générées
    random.shuffle(cartes)

    # Distribuer les cartes entre les deux joueurs
    PileJoueur1 = cartes[:len(cartes)//2]
    PileJoueur2 = cartes[len(cartes)//2:]

    PileDefausseJoueur1 = []
    PileDefausseJoueur2 = []

    # Déroulement des tours
    for tour in range(1, nCompteurTour + 1):
        print(f"--------- Tour n°{tour} ---------")
        if not DeroulementTour(PileJoueur1, PileJoueur2, PileDefausseJoueur1, PileDefausseJoueur2):
            print("Une des piles est vide. Fin de la partie.")
            break

    # Calculer les résultats
    TailleJoueur1 = len(PileDefausseJoueur1)
    TailleJoueur2 = len(PileDefausseJoueur2)

    print("\n*** Résultats finaux ***")
    print(f"Cartes remportées par Joueur 1: {TailleJoueur1}")
    print(f"Cartes remportées par Joueur 2: {TailleJoueur2}")

    # Déterminer le joueur gagnant
    if TailleJoueur1 > TailleJoueur2:
        print("Joueur 1 a gagné la partie!")
    elif TailleJoueur1 < TailleJoueur2:
        print("Joueur 2 a gagné la partie!")
    else:
        print("Il y a égalité entre les joueurs!")


# Lancer une partie 
FinPartie(10)
