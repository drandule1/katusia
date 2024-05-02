# from task1 import summirovanie
# print(summirovanie(1, 3))

import random

# from random import randint
# x=randint(2,9)
# print(x)

#
# x = {"name" : "John", "age" : 36}
#
#
# d=" ".join(x)
# print(d)

# x = frozenset({"apple", "banana", "cherry"})
#
# #display x:
# print(x)
#
# #display the data type of x:
# print(type(x))


numbers = tuple(i for i in range(2,10))
print(numbers)  # Вывод: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers[0]=9


for i in range(2,10):
    print(i)


i=10

if i> 4:
    print("Да больше 4")
if i> 6:
    print("Да больше 6")