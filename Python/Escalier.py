# argument = sys.argv[1]
argument = 5
def pyramid(n): 
    for i in range(n,0,-1):
        argument = n -i + 1
        print(" " * i + "#" * argument)
pyramid(argument)

def pyramid(n): 
    for i in range(n+1):
        j = n -i 
        print(" " * j + "#" * i)
pyramid(argument)