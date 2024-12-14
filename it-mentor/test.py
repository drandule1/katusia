#Сделать калькулятор: у пользователя
#спрашивается число, потом действие и второе
#число
#Создай консольное приложение “Калькулятор”. Приложение должно читать из консоли введенные пользователем строки, числа, арифметические операции проводимые между ними и выводить в консоль результат их выполнения.
#Реализуй функцию main(input: str). Метод должен принимать строку с арифметическим выражением между двумя числами и возвращать строку с результатом их выполнения. Ты можешь добавлять свои импорты, классы и методы.


def main(input: str) -> str:
    try:
        result = input.split(" ")

        if len(result)!=3:
            #return None
            raise ValueError("throws Exception")

        x=int(result[0])
        sign=result[1]
        y=int(result[2])

        if (x < 1  or  x > 10) or (y < 1 or y > 10):
            #return None
            raise ValueError("throws Exception")

        if sign == "+":
            act = x + y

        elif sign == "-":
            act = x - y

        elif sign == "*":
            act = x * y

        elif sign == "/":
            act = x // y
        else:
            #print(f"такого действия нет!")
            #act = None
            raise ValueError("throws Exception")

        return str(act)
    except Exception:
        return "throws Exception"


if __name__ == "__main__":
    result=input("Input : \n")
    print("Output:", main(result) , sep="\n")
