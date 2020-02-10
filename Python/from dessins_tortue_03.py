from turtle import *

def carre(taille, couleur):
    color(couleur)
    c = 0
    while c < 4:
        forward(taille)
        right(90)
        c = c + 1

def triangle(taille, couleur):
    color(couleur)
    c = 0
    while c < 3:
        forward(taille)
        right(120)
        c = c + 1

def etoile5(taille, couleur):
    color(couleur)
    c = 0
    while c < 3:
        forward(taille)
        right(120)
        c = c + 1
etoile5(30, "green")

up()
goto(-500, 0)


def ligne(n):
    i = 0
    size = 1
    while i < 10:
        down()
        carre(40 * size, "red")
        up()
        forward(45 * size)

        down()
        triangle(40 * size, "blue")
        up()
        forward(45 * size)
        i = i + 1
        
        size = size + 0.2


ligne(10)

def essai():
    "This function is well documented but does almost nothing"
    print("Nothing to report")
essai()
print(essai.__doc__)

a = input()
