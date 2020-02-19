import sys
# list_ = (sys.argv)
list_ = [1, 4, 1, 1, 3, 4]

list_.sort()
list_.pop(-1)
list1 = "".join(str(list_))
print(list1)


