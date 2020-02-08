import sys
# word = sys.argv[1]
word = ["arbre"]
list1 = ["amour", "arbre", "balade", "barre", "beau"]

# # Programme 01
# x = "".join(word)
# for y in list1:
#     if len(x) == len(y):
#         if sorted(x) == sorted(y):
#             print([y],end="")

# # Programme 02
# x = "".join(word)
# y = "".join(list1)
# def check(x, y): 
#     for y in list1:
#         if(sorted(x)== sorted(y)): 
#             print([y],end="") 
           
# check(x, y) 

# Programme 03
x = "".join(word)
y = "".join(list1)
def isAnagram(x, y):
    return [y for y in list1 if len(x) == len(y) if sorted(x) == sorted(y)]

print(isAnagram(x,y))

