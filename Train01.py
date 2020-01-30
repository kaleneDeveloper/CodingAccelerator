a,b,c = 1,7,1

while (a < 20):
    a, b, c = a+1, b, a*7
    print(c, end=" ")


a,b = 1, 1.65

while (b < 16384):
    print(f"{a} euro(s) = {b} dollar(s)") 
    a = a * 2
    b = a * 1.65


a, b = 1, 1

while (a - 1 < 12):
    print(b)
    a, b = a + 1, b * 3