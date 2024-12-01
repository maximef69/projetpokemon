class Carte:
    def __init__(self, nom, points_de_vie, attaque, energie, type):
        """
        Initialise une carte.
        :param nom: Nom de la carte
        :param points_de_vie: Points de vie de la carte
        :param attaque: Valeur d'attaque
        :param energie: Énergie requise
        :param type: Type de la carte (Feu, Eau, Plante, etc.)

        """
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

# # Exemple de création de cartes
carte1 = Carte("Dragon de Feu", 30, 8, 3, "Feu")
carte2 = Carte("Hydre Aquatique", 25, 6, 2, "Eau")
