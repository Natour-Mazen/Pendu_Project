from donnees import *
from random import choice
import turtle as tt
import time


def nom_joueur():
    nom=input("Entrez votre nom : \t")
    if len(nom)<3:
        nom=input("Entrez un nom valide svp")
        print("Good luck",nom,"!Try to find the right word to win.")
        return nom_joueur()
    else:
        print("Good luck",nom,"!Try to find the right word to win.")

def lettre_recup():
    lettre_entree = input("Tapez une lettre seulement: ")
    if len(lettre_entree)>1:
        return lettre_entree[0]
    else:
        return lettre_entree

def mot_a_choisir():
    return choice(liste_mot)

def mot_a_cacher(mot_a_chercher,lettre_trouvees):
    mot_cacher=""
    for lettre_entrer in mot_a_chercher:
        if lettre_entrer in lettre_trouvees:
            mot_cacher+= lettre_entrer
        else:
            mot_cacher += "*"
    return mot_cacher

def affiche(nombre_chance):
    try:
        tt.reset()
    except tt.Terminator:
        pass
    tt.hideturtle()
    if nombre_chance<=9 :
     tt.penup()
     tt.goto(-100,-100)
     tt.pendown()
     tt.forward(150)
    if nombre_chance<=8 :
     tt.penup()
     tt.goto(-75,-100)
     tt.pendown()
     tt.goto(-75,100)
    if nombre_chance<=7 :
     tt.pendown()
     tt.goto(-75,100)
     tt.forward(200)
    if nombre_chance<=6 :
     tt.goto(125,80)
    if nombre_chance<=5 :
     tt.penup()
     tt.goto(125,50)
     tt.pendown()
     tt.circle(15)
    if nombre_chance<=4 :
     tt.penup()
     tt.goto(125,50)
     tt.pendown()
     tt.goto(125,-30)
    if nombre_chance<=3 :
     tt.goto(150,-60)
     tt.penup()
     tt.goto(125,-30)
    if nombre_chance<=2:
     tt.pendown()
     tt.goto(100,-60)
     tt.penup()
     tt.goto(125,10)
    if nombre_chance<=1 :
     tt.pendown()
     tt.goto(90,20)
     tt.penup()
     tt.goto(125,10)
    if nombre_chance<=0 :
     tt.pendown()
     tt.goto(160,20)
    time.sleep(3)
    tt.bye()