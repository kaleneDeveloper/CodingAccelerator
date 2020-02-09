from turtle import *

def carre(taille, couleur):
    color(couleur)
    c = 0
    while c < 4:
        forward(taille)
        right(90)
        c = c + 1
carre(305, "blue")

def essai():
    "This function is well documented but does almost nothing"
    print("Nothing to report")
essai()
print(essai.__doc__)

