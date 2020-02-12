from dessins_tortue_01 import *

# up()
# goto(5, -5)
speed(10)
pensize(2)
shapesize(0.50,0.50)

def ligneCarre():
    i = 0
    while i < 10:
        down()
        carre(25, "red")
        up()
        forward(30)
        i = i + 1

def lignRepeat(n):
    i = 0
    while i < n:
        ligneCarre()
        up()
        i = i + 1
        goto(0, -30 * i)


 

lignRepeat(10)


a = input()
