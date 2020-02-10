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
    for i in range(5):
        forward(taille)
        right(144)

def etoile5(taille, couleur):
    color(couleur)
    for i in range(5):
        forward(taille)
        right(144)

def etoile6(taille, couleur):
    color(couleur)
    for i in range(3):
        forward(taille)
        right(120)
etoile6(100, "red")

up()
goto(-200, 200)

def ligneEtoile(n):
    i = 0
    size = 1
    while i < n:
        down()
        etoile5((1 * 60) * size, "green")
        up()
        forward(70 * size)
        i = i + 1
        if i <= n/2:
            size = size + 0.2
        if i > n/2:
            size = size - 0.2 

# ligneEtoile(9)


def ligneTriangleCarre(n):
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

# ligneTriangleCarre(10)

def ligneCarreEtoile(n):
    i = 0
    size = 1
    while i < n:
        down()
        carre(40 * size, "red")
        up()
        forward(45 * size)

        down()
        etoile5((1 * 60) * size, "green")
        up()
        forward(65 * size)
        i = i + 1
        if i <= n/2:
            size = size + 0.4
        if i > n/2:
            size = size - 0.4

# ligneCarreEtoile(8)

def polygone(taille, couleur,n):
    color(couleur)
    c = 0
    i = 0
    size = 1
    while c < 6:
        down()
        carre(50,"red")
        up()
        forward(60)

        down()
        etoile6(50, "blue")
        up()
        forward(60)

        forward(taille)
        right(60)

        c = c + 1
        i = i + 1
        if i <= n/2:
            size = size + 0.4
        if i > n/2:
            size = size - 0.4

polygone(10, "red",2)


def essai():
    "This function is well documented but does almost nothing"
    print("Nothing to report")
essai()
print(essai.__doc__)

a = input()
