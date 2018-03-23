# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""


class Labyrinthe:
    """Classe représentant un labyrinthe."""

    def __init__(self, robot, obstacles):
        self.robot = robot
        self.grille = {}

    def robot_position(self, chaine):

        pos = 0

        for ele in chaine:
            if ele == "X":
                break
            else:
                pos += 1

    return pos


def creer_labyrinthe_depuis_chaine(self, chaine):
    self.robot_position(chaine)

    labyrinthe = Labyrinthe("X", "O")

    return labyrinthe