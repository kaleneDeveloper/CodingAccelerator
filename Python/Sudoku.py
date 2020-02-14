import re
import ast
import numpy as np


with open("s.txt", 'r') as f:
    list_sudoku = f.read().splitlines()


def sudoku():
    store_list_sudoku = []
    try:
        with open("s.txt", 'r') as f:
            list_sudoku = f.read().splitlines()
    except FileNotFoundError:
        return False
    
    for x in list_sudoku:
        list_sudoku = re.sub('[^0-9\_\[\\]]', '', x)
        list_sudoku = str(list_sudoku).replace("_", "0")
        if not re.match(r'^\s*$', list_sudoku):
            list_sudoku = [int(x) for x in list_sudoku]
            store_list_sudoku.append(list_sudoku)
    
    print(store_list_sudoku)

sudoku()






# print(sudoku01[0:1])


# for x in test:
#     a = re.sub('[^0-9\_\[\\]]', '', x)
#     a = str(a).replace("_", "0")
#     if not re.match(r'^\s*$', a):
#         a = [int(x) for x in a]
#         print(a)



# a = (str(a))
# a = re.sub('[^0-9\_\[\\]]', '', a)
# a = str(a).replace("_", "0")




# a = '%s,' % ",".join(map(str,a))


# if a != "[]":
#     a = '%s,' % ",".join(map(str,a))
#     print(a)

# test = {[x] for x in a.contents1()}
# print(test)

# def sudoku():
#     try:
#         with open("s.txt", 'r') as f:
#             contents1 = f.read().splitlines()
#     except FileNotFoundError:
#         return False
#     for x in contents1:
#         test = re.sub('[^0-9\_]', '', x)
#         test = '[%s],' % ", ".join(map(str,test))
#         test = test.replace("_", "0")
#         if test != "[],":
#             print(test)

# sudoku()
 
#     print(contents1)
# for x in contents1:
#     contents1 = re.sub('[^0-9\_]', '', str(x))
#     print([contents1])

# colors = ["red", "green", "blue", "purple"]

# i = 0
# while i < len(contents1):
    
#     print(contents1[i])
#     i += 1


# f = lambda x: [[y for j, y in enumerate(set(x)) if (i >> j) & 1] for i in range(2**len(set(x)))]

# print(f([10]))

# f = lambda x: [[x for x in enumerate((contents1))] for i in range(len(set(x)))]

# print(f([str(contents1)]))


