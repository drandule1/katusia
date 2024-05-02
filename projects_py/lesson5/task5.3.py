#**Вывести четные числа от 2 до N по 5 в строку


n=int(input("введите число N "))
num=0
for i in range(2,n+1,2):
    if num<4:
        print(i, end=" ")
        num+=1
    else:
        print(i)
        num = 0


