

# n = int(input("Введите значение n: "))
# powers = [2**i for i in range(1, n+1)] # здесь переберет i от 1 до n которое введено и 2**i заполнит лист
# print("Список степеней числа 2 от 2^1 до 2^{}:".format(n))
# print(powers)

numbers = input("Введите степени через пробел: ")
mylist = numbers.split()

# Преобразование строковых степеней в целые числа и возведение в степень 2
mylist = [2 ** int(i) for i in mylist]
#squares = [x**2 for x in range(1, 11)]
print(mylist)