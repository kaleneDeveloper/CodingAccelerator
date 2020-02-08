import math
from math import *
from turtle import *

accord = ["oui", "non"] 
print(accord[0])
print(accord[1])

# ch = input("test :")
# n = int(ch)
# if n % 2:
#     print("impair")
# else:
#     print("pair")

# print("This sript searches for the largest of the three numbers")
# print("Please enter your number split with a comma: ")
# string = input()

# nn = list(eval(string))

# max, index = nn[0], "first"

# if nn[1] > max:
#     max = nn[1]
#     index = "second"
# if nn[2] > max:
#     max = nn[2]
#     index = "third"

# print("The largest number is",max)
# print("This number is", index,"in your list.")


# a = True
# while a:
#     try:
#         sring = print('Choose your number at 1 to 3 (or 0 for close):', end=" ")
#         a = input()
#         if a == "":
#             continue
#         a = int(a)
#         if a == 1:
#             print(f"You are choose the number 1 :")
#         elif a == 2:
#             print(f"you are choose the number 2 :")
#         elif a == 3:
#             print(f"you are choose the number 3 :")
#         else:
#             print(f"Please choose number between 1 to 3.")
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")      

# print("Your are choose the number 0 ")


# a = True

# while a:
#     try:
#         string = print("Enter your number: ", end=" ")
#         a = input()
#         if a == "":
#             exit()
#         a = int(a)
#         if a == 3:
#             print("Pls a moment ...")
#         elif a != 2:
#             print("You are lose !")
#         else:
#             print("You win !")
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")   


# print("1",end=' ')
# a = eval(input())
# print("2",end=' ')
# b = eval(input())
# s = 0
# list1 = ""
# n = a

# while n <= b:
#     if n % 3 == 0 or n % 5 == 0:
#         s = s + n
#         list1 = list1 + str(n) + " + "
#     n = n + 1

# list1 = list(list1)
# list1 = list1[:-2]
# list1 = "".join(list1)
# print(list1,"=",s)

a = 700

if a % 4 == 0 or a % 400 == 0:
    bs = 1
else:
    bs = 0
if a % 400 != 0 and a % 100 == 0:
    bs = 0

if bs == 0:
    print("No leap year")
else:
    print("Leap year")



print("Please enter your name :",end=" ")
name = input()
print("And enter your sex now :",end=" ")
sex = input()
while sex != "" or name != "":
    try:
        if sex == "M" or sex == "m":
            print(f"Dir sir {name}")
        elif sex == "F" or sex == "f":
            print(f"Dir madam {name}")
        else:
            print('Enter "m" or "f"')
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


