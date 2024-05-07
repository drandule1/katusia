
#Сделать калькулятор: у пользователя
#спрашивается число, потом действие и второе
#число


deystviya="введите одно из  действий \"+\",\"-\", \"*\", \"/\" "
x = float(input("введите число 1 "))
act = input(deystviya)

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
    print(f"такого действия нет, пробуй еще!{deystviya}!")



