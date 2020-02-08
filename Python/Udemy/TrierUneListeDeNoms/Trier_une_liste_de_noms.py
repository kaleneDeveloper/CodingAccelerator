import os
from glob import glob

while True:
    _list = input("Take your list or create new list: ")
    if not _list:
        print("Insert text.")
    elif os.path.isfile(_list):
         break
    else:print("File no found")

with open(_list, 'r') as f:
    file = f.read().splitlines()

names = []
for line in file:
    names.extend(line.split())

name_final = [name.strip(",. ") for name in names]

if not _list.endswith(".txt"):
    with open(_list + "_out.txt", 'w') as f:
        f.write("\n".join(sorted(name_final)))
elif _list.endswith(".txt"):
    oldext = os.path.splitext(_list)[0]
    _list = oldext
    with open(_list + "_out.txt", 'w') as f:
        f.write("\n".join(sorted(name_final)))
