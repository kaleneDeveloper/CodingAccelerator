from math import *

print("Pls enter 3 valeurs of triangle", end=" ")
# string = input()
string = [10, 12, 14]
# string = [5.8, 3, 5]

nn = list(eval(str(string)))
print(nn)

BC, AC, AB = nn[0], nn[1], nn[2]
a, b, c = nn[0], nn[1], nn[2]

# Angle A
angle_A = (-a**2 + b**2  + c**2) / (2 * b * c)
angle_A = acos(angle_A)
angle_A = (angle_A * 180)/pi

# Angle B
angle_B = (a**2 - b**2  + c**2) / (2 * c * a)
angle_B = acos(angle_B)
angle_B = (angle_B * 180)/pi

# Angle C
angle_C = (a**2 + b**2  - c**2) / (2 * a * b)
angle_C = acos(angle_C)
angle_C = (angle_C * 180)/pi

allAngles = int(angle_A + angle_B + angle_C)


if allAngles == 180:
    try:
        if a == b and b == c and c == b:
            print("The triangle is a Triangle Isocseles.")
        elif a == b or b == c or c == b:
            print("The triangle is a Triangle Isocseles rectangle.")
        elif 89 <= angle_A <= 91 or 89 <= angle_B <= 91 or 89 <= angle_C <= 91:
            print("The triangle is a Triangle rectangle.")
        else:
            print("The triangle is an unspecified Triangle knowing.")
        
    except:
        print("Oops!  That was no valid number.  Try again...")
else:
    print("Is not a triangle")
