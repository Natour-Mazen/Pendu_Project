from donnees import *
from fonctions import *


MESSAGE_GAGNE = "BRAVO, vous avez trouvé le mot !!! Vous avez remporté la partie !"
MESSAGE_PERDU = "DOMMAGE, vous n'avez pas trouvé le mot... Vous avez perdu la partie."

def jouer_partie():
    mot_a_chercher = mot_a_choisir()
    lettres_trouvees = []
    mot_trouve = False
    nombre_chance = 10

    while not mot_trouve and nombre_chance > 0:
        print("\n----------------------------------------------------\n")
        print("Mot à trouver:", mot_a_cacher(mot_a_chercher, lettres_trouvees))
        lettre = lettre_recup()
        if lettre in mot_a_chercher:
            lettres_trouvees.append(lettre)
            print("BRAVO, vous avez trouvé une lettre, il vous reste", nombre_chance, "chance(s)")
        else:
            nombre_chance -= 1
            print("NON, cette lettre n’appartient pas au mot, il vous reste", nombre_chance, "chance(s)")
            print("Regardez la fênetre Turtle (fênetre plume), pour voir l'état de votre pendu ;), attendez 8s pour continuer!!")
            affiche(nombre_chance)
        mot_trouve = mot_a_chercher == mot_a_cacher(mot_a_chercher, lettres_trouvees)
    if mot_trouve:
        print(MESSAGE_GAGNE)
    else:
        print(MESSAGE_PERDU)

def jouer():
    jouer_encore = True
    utilisateur = nom_joueur()
    while jouer_encore:
        jouer_partie()
        jouer_encore = input("Voulez-vous rejouer (oui/non)?").lower() == "oui"

jouer()
