import random

def DistributionEtMelangeDesCartes(cartes):
    """
    Mélange les cartes et les distribue entre les deux joueurs : 
    - Joueur 1 reçoit les cartes aux indices pairs.
    - Joueur 2 reçoit les cartes aux indices impairs.
    """
    random.shuffle(cartes)  # fonction qui permet de mélanger les cartes

    PileJoueur1 = [cartes[i] for i in range(len(cartes)) if i % 2 == 0]
    PileJoueur2 = [cartes[i] for i in range(len(cartes)) if i % 2 != 0]
    return PileJoueur1, PileJoueur2

# Début du code
#Test du code
cartes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
PileJoueur1, PileJoueur2 = DistributionEtMelangeDesCartes(cartes)

print(PileJoueur1)
print(PileJoueur2)
