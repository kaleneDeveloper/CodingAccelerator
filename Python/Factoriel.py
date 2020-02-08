import sys
# number = sys.argv[1]
number = 3

def fact(n):
    x=1
    for i in range(1,n+1):
        print(n)
        x = x * i 
    print("Factorial of",number,"is",x,)

fact(number)


def factorial(n): 
    return 1 if (n==1 or n==0) else n * factorial(n - 1); 

print("Factorial of",number,"is", factorial(number))



