# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""


from labyrinthe import Labyrinthe as lab

class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""


    def __init__(self, nom, chaine):
        self.nom = nom
        self.labyrinthe = lab.creer_labyrinthe_depuis_chaine(self,chaine)


    def __repr__(self):
        return "<Carte {}>".format(self.nom)



