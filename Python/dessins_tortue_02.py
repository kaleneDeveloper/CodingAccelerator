from dessins_tortue_01 import *

# up()
# goto(5, -5)


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
        goto(5, -30 * i - 5)


 

lignRepeat(10)


a = input()
