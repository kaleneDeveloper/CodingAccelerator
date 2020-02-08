# argument = sys.argv[1]
argument = 10
def pyramid(n): 
    for i in range(n,0,-1):
        j = n -i + 1
        print(" " * i + "#" * j )
pyramid(argument)