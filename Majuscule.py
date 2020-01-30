string = "bien le bonjour !"

for i, j in zip(string[::2],string[1::2]):
    newString = (i.lower() + j.upper())
    print(newString,end="")  
        
ret = ""
i = True
for x in string:
    print(i)
    if i:
        ret += x.upper()
    else:
        ret += x.lower()
    if x != " ":
        i = not i
print(ret)


# for i in string:
#     i = not i
#     print(i)
