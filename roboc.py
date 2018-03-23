# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""
import os
from carte import Carte
from labyrinthe import Labyrinthe

# On charge les cartes existantes
cartes = []



for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:

            contenu = fichier.read()
            cartes.append(Carte(nom_carte,contenu))  # ajouter  à la list cartes  deux objects
                                                   # 1  nom : facile
                                                   # 2  nom : prison

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
        print("  {} - {}".format(i + 1, carte.nom))

# Si il y a une partie sauvegardée, on l'affiche, à compléter


# ... Complétez le programme ...


" Choix de la carte "
num=int(input("Entrez un numéro de labyrinthe pour commencer à jouer :"))
print(cartes[num-1].labyrinthe)
# remplire la grille de la class labyrinthe


#app = list(map(lambda x,palce=0:x=='X' place++,cartes[num-1].labyrinthe))
