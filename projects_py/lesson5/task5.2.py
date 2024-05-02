




x = float(input("введите число 1 "))
act = input("введите одно из  действий \"+\",\"-\", \"*\", \"/\" ")

y = float(input("введите число 2 "))

if act == "+":
    resalt=x+y
    print(resalt)
elif act == "-":
    resalt = x-y
    print (resalt)
elif act == "*":
    resalt = x*y
    print (resalt)
elif act == "/":
    try:
        resalt = x/y
        print(resalt)
    except ZeroDivisionError as e:
        print("деление на ноль!!!!!")
else:
    print("такого действия нет, пробуй еще!!")



