import math
import re

list01 = ['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien', 'Alexandre-Benoît', 'Louise']

for x in list01:
    y = len(x)
    print(x,y)


listN = len(list01)
n = 0

while n < listN :
    string = list(list01[n])
    string = "".join(string)
    y = len(string)
    print(string,y)
    n = n + 1


# def note():
#     listNote = []
#     note = 1
#     total = 0
#     while note != "":
#         try:
#             print("Enter your note :",end=" ")
#             note = input()
#             note = float(note)
#             if note < 0:
#                 exit()
#             if note > 0:
#                 listNote.append(note)
#                 print(f"Number of note(s) entered {len(listNote)}")
#                 total = total + note
#         except:
#             if note != "":
#                 print("Oops!  That was no valid number.  Try again...")

#     noteMax = 0       
#     noteMin = listNote[0]
#     for x in listNote:
#         if x > noteMax:
#             noteMax = x
#         if x < noteMin:
#             noteMin = x

#     index = len(listNote)
#     moyen = total / index
#     print(f"List of notes: {listNote}")
#     print(f"Note minimum {noteMin}, note maximum {noteMax}, pour une moyen de: {moyen}")

# note()

# base = 10
# fin = 20
# def table(base, fin):
#     n = 1 
#     while n < fin + 1:
#         print(n * base,end=" ")
#         n = n + 1
# table(base, fin)


# def cube(w):
#     return w*w*w

# b = cube(9)
# print(b)


def table(base):
    resultat = []
    n = 1
    while n < 11:
        b = n * base
        resultat.append(b)
        # resultat = resultat + [b]
        n = n + 1
    return resultat

ta9 = table(9)
print(ta9)

# def cube(n):
#     return n**3

# def volumeSphere(r):
#     return 4 * math.pi * cube(r)/3

# r = input("Entrer la valeur du rayon : ")

# print("Le volume d'une sphere vaut",volumeSphere(float(r)))



# def surfCercle(R):
#     return math.pi * R**2

# r = input("Entrer la valeur du rayon : ") 
# print("L'air du cercle vaut ",surfCercle(float(r)))


def volBoite(x1, x2, x3):
    return x1 * x2 * x3

print(volBoite(5.2, 7.7, 3.3))

def maximum(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3
       
three = False
while three == False:
    try:
        one = float(input("Insert your number one : "))
        two = float(input("Insert your number two : "))
        three = float(input("Insert your number three : "))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


print("The big number is", maximum(one, two, three))


