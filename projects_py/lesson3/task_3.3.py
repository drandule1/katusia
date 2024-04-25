#Пользователь вводит Имя, Возраст и Город. Сформировать
#приветственное сообщение путем форматирования 3мя способами

name = input("введите имя ")
age = input("введите возраст ")
city = input("введите город ")
print(f"Hello,mister {name},you are {age} and we are happy meeting you in our {city}")


print("Hello,mister %s,you are %s and we are happy meeting you in our %s"%(name,age,city))


print("Hello,mister {},you are {} and we are happy meeting you in our {}".format(name,age,city))