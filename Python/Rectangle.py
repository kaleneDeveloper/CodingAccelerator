import sys
import re

# with open(sys.argv[1], 'r') as f:
#     contents1 = f.read()

# with open(sys.argv[2], 'r') as f:
#     contents2 = f.read()

# with open("c1.txt", 'r') as f:
#     contents1 = f.read().splitlines()

with open("c2.txt",'r') as f:
    contents2 = f.read().splitlines()
for x in contents2:
        print([x],"")
        print(type(x))

# for x in contents1:
#     for y in contents2:
#         p = re.compile(x)
#         match = p.search(y)
#         if match:
#             print(match)

# test = [x for x in contents1]
# print(test)


# for i, line in enumerate(open('c2.txt')):
#     for match in re.finditer(pattern, line):
#         print('Found on line %s: %s' % (i+1, match.group()))

# p = re.compile(contents1); print(p)
# match = p.search(contents2); print(contents2)


# a = '123'
# b = '091230'
# result = re.findall(a, b)
# if result:
#   print(result)
# else:
#   print("Search unsuccessful.")

# p = re.compile(a)
# match = p.search(b); print(match)

# p = re.compile('[a-z]+')
# m = p.search('::: message'); print(m)
