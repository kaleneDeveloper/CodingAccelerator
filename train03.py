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

listNote = []
note = 1
while note != "":
    try:
        print("Enter your note :")
        note = input()
        note = float(note)
        if note < 0:
            exit()
        if note > 0:
            listNote.append(note)
    except:
        if note != "":
            print("Oops!  That was no valid number.  Try again...")

print(f"List of note: {listNote}")