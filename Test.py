list1 = [-2, 1, 2, 4, 7, 10]
target = 13


def sameNumber():
    for i in list1:
        for j in list1:
            if i + j == target:
                return f"{i} + {j} is equal to {i + j}"
    return 0

print(sameNumber())


def test():
    return [i for i in list1 for j in list1 if i + j == target]

print(test())
###
@@@

