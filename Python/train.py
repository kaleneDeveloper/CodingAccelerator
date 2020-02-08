import math
from math import *
from turtle import *

a,b,c = 1, 7, 1

while (a < 20):
    a, b, c = a + 1, b, a*b
    print(c, end=" ")

# Convert euros to Canadian dollars 

a,b = 1, 1.65

while (b < 16384):
    print(f"{a} euro(s) = {b} dollar(s)") 
    a = a * 2
    b = a * 1.65


a, b = 1, 1
# Multiple numbers time 3

while (a - 1 < 12):
    print(b)
    a, b = a + 1, b * 3


# Calculate volume parallelepiped

width = 4
heigh = 20
deph = 3

volume = width * heigh * deph
print(f"{volume} cm³")

# Converte seconds to year, month, day, hour, minute and second
number = 36005000

minute = number // 60
seconde = number % 60

heure = minute // 60
minute = minute % 60

jour = heure // 24
heure = heure % 24

mois = jour // 30
jour = jour % 30

année = mois // 12
mois = mois % 12

print(année,"année(s)",mois,"mois",jour,"jour(s)",heure,"heure(s)",minute,"minute(s)",seconde,"seconde(s)")

# Take the multiple of 3
a,b,c = 1, 7, 1

while (a < 20):
    a, b, c = a + 1, b, a*b
    if c % 3 == 0:
        print(c, "*", end=" ")
    else:
        print(c, end=" ")

a, b, c = 1, 13, 1

while (a < 50):
    a, b, c = a + 1, b, a*b
    if c % 7 == 0:
        print(c, end=" ")

number = 10
a = 0
while (a < number):
    a = a + 1
    print(a * "*")

a ,b ,c = 1. ,2. ,1

while c < 18:
    a, b, c, = b, a*b, c +1
    print(b)

deg, min, sec = 32, 13, 49

fm = sec/60
fd = (min + fm)/60
ang = deg + fd

rad = 180/math.pi
arad = ang / rad
arad = ang * math.pi/180
print(deg,min,sec,"=",arad)



degretCelsius = 30
fahrenhei = 45

fahrenheitToCelsius = degretCelsius * 9/5 + 32
print(fahrenheitToCelsius)

celsiusToFahrenheit = (fahrenhei - 32) * 9/5
print(celsiusToFahrenheit)

while c < 18:
    a, b, c, = b, a*b, c +1
    print(b)


years = 20
euros = 100
interet = 4.3
def test(n,euro,interet):
    for x in range(1,n+1):
        euro = euro * interet / 100 + euro
        
        print(f"{x} an(s) = {int(euro)} € (interet: {int(euro - euros)} €)")

test(years, euros, interet)


case = 64
def grainOfRice(n):
    y = 1
    for x in range(1,n+1):
        print("case n",x,"grain of rice :",y)
        y = y * 2
                  
grainOfRice(case)

n = 1
g = 1

while n < 65:
    print(n,g)
    n, g = n+1, g*2

# Detecte a letter

string = "Je suis kaaaaalene"
i = 0

for x in string:
    if x == "a":
        i = i + 1
print(f"There is {i} 'a'.")

# Add * after every letter

ret = ""       
for x in string:
    if x != " ":
        ret += x + "*"
    elif x == " ":
        ret += x
    else: print("Error")

print(ret)
# Reverse string

string = "zorglup"
srtingReversed = ""
index = len(string)
while index > 0:
    srtingReversed += string[ index - 1 ]
    index -= 1
print(srtingReversed)

# Compare if string is palindrome

string = "radar"
srtingReversed = ""
index = len(string)
while index > 0:
    srtingReversed += string[ index - 1 ]
    index -= 1
if srtingReversed == string:
    print("It is a palindrome")
else: print("Is not a palindrome")

# List sorted
t1 = [31, 28, 31, 30 , 31, 30, 31, 31, 30, 31, 30 ,31]
t2 = ['Junuary', 'February', 'March', 'April', 'May', 'Jun', 'July', 'August', 'September', 'October', 'November', 'December']

index = len(t1)
x = - 1
while index -1 > x:
    x = x + 1
    y = x % 12
    print(t1[y], t2[y])

x = - 1
while index -1 > x:
    x = x + 1
    y = x % 12 
    print(t2[y],end=' ')


list01 = [32, 5, 12, 8, 3, 75, 2, 15]
maxNumber = 0
for x in range(len(list01)):
    x = list01[x]
    if x > maxNumber:
        maxNumber = x
print(f"The big number is {maxNumber}.")


list01 = [32, 5, 12, 8, 3, 75, 2, 15]
index = len(list01)
pair = []
odd = []
x = - 1
while index - 1 > x:
    x = x + 1
    y = list01[x]
    if y % 2 == 0:
        pair.append(y)
    elif y % 2 != 0:
        odd.append(y)

print(pair,odd)

list01 = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']

index = len(list01)
x = - 1
a = []
b = []
while index -1 > x:
    x = x +1
    y = list01[x]
    if len(y) < 6:
        a.append(y)
    elif len(y) >= 6:
        b.append(y)
print(a, b)


number = 121 
angle = pi/6

print(sqrt(number), sin(angle))


# MilesHour = input("Enter your valeurs: ")

MilesHour = float(1)

MeterHour = MilesHour * 1609

MeterHourToMeterSeond = MeterHour / 3600

MeterHourToKilometerHour = MeterHour / 1000


print(f"{MilesHour} miles/h is equal {MeterHourToMeterSeond} m/s and {MeterHourToKilometerHour} km/h.")

mps = (MilesHour * 1609)/3600

kmph = (MilesHour * 1609)/1000

print(f"{MilesHour} miles/h is equal {mps} m/s and {kmph} km/h.")

a, b, c = 3, 4, 5 

P = a + b + c

p = P/2
S = sqrt(p*(p - a)*(p - b)*(p - c))

print(S,"cm2")


# l = 30 #cm
# T = 2 * pi * sqrt(1/g)

# print(g)



list_ = []
# number = "start"
while number != "":
    try:
        number = input("Enter your number :")
        if number != "":
            list_.append(float(number))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

if not list_:
    print("List is empty")
else: print(list_)
        



