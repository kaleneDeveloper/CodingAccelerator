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

base = 10
fin = 20
def table(base, fin):
    n = 1 
    while n < fin + 1:
        print(n * base,end=" ")
        n = n + 1
table(base, fin)

