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


def sudoku():
    try:
        with open("s.txt", 'r') as f:
            contents1 = f.read().splitlines()
    except FileNotFoundError:
        return False
    for x in contents1:
        test = re.sub('[^0-9\_]', '', x)
        # test = '[%s],' % ", ".join(map(str,test))
        test = test.replace("_", "0")
        
        print(test).splitlines()

        # if test != "[],":
        #     print(test)

# sudoku()






sudoku01 = [
[1,9,5,7,8,4,2,0,0],
[3,0,6,5,2,9,1,4,7],
[4,7,2,1,0,3,9,8,5],
[6,3,7,8,5,2,4,1,9],
[8,5,9,6,0,1,7,3,2],
[2,1,4,3,9,7,6,5,8],
[9,2,0,4,1,8,5,7,6],
[5,0,8,9,7,6,3,2,1],
[7,6,1,2,3,5,8,0,4]
]


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

def sudoku():
    try:
        with open("s.txt", 'r') as f:
            contents1 = f.read().splitlines()
    except FileNotFoundError:
        return False
    for x in contents1:
        test = re.sub('[^0-9\_]', '', x)
        test = '[%s],' % ", ".join(map(str,test))
        test = test.replace("_", "0")
        if test != "[],":
            print(test)

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


