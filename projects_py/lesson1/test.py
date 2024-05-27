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


# numbers = tuple(i for i in range(2,10))
# print(numbers)  # Вывод: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# numbers[0]=9
#
#
# for i in range(2,10):
#     print(i)
#

# i=10
#
# if i> 4:
#     print("Да больше 4")
# if i> 6:
#     print("Да больше 6")

# def summa(*args):
#
#     total = 1
#     for i in args:
#         total = total*i
#     return total
#
# print(summa(1,8,9))  # Вызов с разным количеством аргументов

# def info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#
#
# info(имя="Алекс", возраст=30, город="Москва",пол="нет")
#
#

# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно


# spisok=['lll',556,5.7,{1,4},9,4,"katya",(7,9)]
#
# i=0
# while i<len(spisok):
#     if type(spisok[i])==str:
#         i+=1
#     else:
# #         del spisok[i]
# #
# # print(spisok)
#
#
# # print(spisok)
# # print(spisok[::-1])# срез дает нов список
# # spisok=spisok[::-1]
# #
# # #spisok.reverse()#сам список развернулся
# # print(spisok)
# #
# #
#
#
#


# #
#
#
#
#
#
# #


# Перевод 2-10
# dvoich='011111001'
# chislo=0
# for i,g in enumerate(dvoich[::-1]):
#     #print(i,g)
#     if g=="1":
#         chislo+=2**i
#     else:
#         pass
# print(chislo)
# Перевод 10-2
# p=[]


# strana=input("какая страна тебя поразила? ")
# print(strana+" это отличнейшее место для отдыха")
#
# x=int(input("введите число "))
# y=int(input("введите число "))
# z=int(input("введите число "))
# c=(x**2)*(2*y+5*z)
# print(c)

# import random
# list=[random.randint(1,100) for _ in range(1,10)]
# print(list)
# print(max(list))

# spisok=[56,1,5,5,6,7,8,44,33,]
# spisok1=sorted(spisok)
# print(spisok1)
# spisok2=spisok1[::-1]
# print(spisok2)
# print(sum(spisok2))

#
# class ManClass:
#     age: int
#     hight: int
#     name: str
#
#     def __init__(self, name, age, hight):
#         self.name = name
#         self.age = age
#         self.hight = hight
#
#     def getname(self):
#         return self.name
#
#     def getage(self):
#         return self.age
#
#     def gethight(self):
#         return self.hight
#
#     def setname(self,name):
#         self.name = name
#
#     def __str__(self):
#         return f"Данные об обьекте имя {self.name} , возраст {self.age}"
#
#
# vasia = ManClass("Vasia", 33, 183)
# petia = ManClass("petia", 35, 180)
#
#
#
# print(vasia.getname(),vasia.getage(),vasia.gethight())
#
# vasia.setname("pol")
#
# print(vasia.getname(),vasia.getage(),vasia.gethight())
#
# print(vasia)
# print(petia)


# 1. Написать класс Car
# Конструктор класса принимает атрибуты:
# color: str (цвет)
# count_passenger_seats: int (количество пассажирских мест)
# is_baby_seat: bool (наличие десткого кресла)
# is_busy: bool (определяется внутри конструктора со значением False, не принимается на
# вход)
# 1.1 Написать магический метод __str__ выводящий форматированную строку с информацией
# об автомобиле

#
# class car:
#     color: str
#     count_passenger_seats: int
#     is_baby_seat: bool
#     is_busy : bool
#
#     def  __init__(self, color, count_passenger_seats, is_baby_seat):
#         self.color=color
#         self.count_passenger_seats=count_passenger_seats
#         self.is_baby_seat=is_baby_seat
#         self.is_busy = False
#
#     def __str__(self):
#         baby=""
#         if self.is_baby_seat:
#             baby="детские места есть"
#         else:
#             baby = "детские места нет"
#         busy = ""
#         if self.is_busy:
#             busy= "машина занята"
#         else:
#             busy= "машина свободна"
#
#         return f"Данные о машине цвет {self.color} , количество мест {self.count_passenger_seats},{baby},{busy}"
#
#
# class taxi:
#     cars: list
#
#     def  __init__(self,cars):
#         self.cars=cars
#
#     def find_car(self,count_passengers,is_baby):
#         for mycar in self.cars:
#             #print(mycar)
#             if mycar.is_busy == False  and  is_baby==False:
#                 if mycar.is_baby_seat and mycar.count_passenger_seats-1 >= count_passengers:
#                     print(mycar)
#                     mycar.is_busy=True
#                     return mycar
#                 elif mycar.is_baby_seat == False  and mycar.count_passenger_seats >= count_passengers:
#                     print(mycar)
#                     mycar.is_busy = True
#                     return mycar
#             elif mycar.is_busy == False  and  is_baby==True:
#                 if mycar.is_baby_seat and mycar.count_passenger_seats >= count_passengers:
#                     print(mycar)
#                     mycar.is_busy = True
#                     return mycar
#                 elif mycar.is_baby_seat == False:
#                     continue
#         else:
#             print("машин нет")
#             return None
#
#
#
#
#
#
#
#
# car1=car("car1", 4, True)
# car2=car("car2", 5, False)
# car3=car("cat3", 4, False)
# car4=car("car4", 2, True)
# car5=car("car5", 6, True)
#
# listcar=[car1,car2,car3,car4,car5]
#
# mytaxi=taxi(listcar)
# mytaxi.find_car(5,True)



#
# 2.  Написать класс Taxi
# Конструктор класса принимает атрибуты:
# cars: list[Car] (список экземпляров класса Car)
# 2.1 Реализовать метод find_car
# На вход метода поступают атрибуты: count_passengers, is_baby (количество пассажиров,
# наличие ребенка, примечание: количество пассажиров с учетом ребенка если он есть)
# На основании данных, вернуть объект Car из атрибута cars подходящий по параметрам и
# свободный (is_busy = False), у автомобиля сменить атрибут is_busy на значение True, если
# подходящего автомобиля нет, метод должен возвращать None



################################################################################################################

#
# 3. Реализовать класс Category
# Создать атрибут класса categories
# 3.1 Написать метод класса add принимающий на вход название категории, если такой
# категории в атрибуте класса categories нет, добавить данную категорию в список и вернуть
# индекс вхождения новой категории в списке. Если такая категория уже есть, вызвать
# исключение ValueError
# 3.2 Написать метод класса get принимающий индекс и возвращающий категорию из списка
# категорий на этом индексе, если нет элемента на таком индексе, вызвать исключение
# IndexError
# 3.3 Написать метод класса delete принимающий индекс категории в списке категорий и
# удаляющий элемент из списка категорий на этом индексе, если нет элемента на таком
# индексе, ничего не делать, метод ничего возвращать не должен
# 3.4 Написать метод класса update принимающий индекс категорий и новое название
# категории, если нет элемента на таком индексе, то новая категория должна добавляться с
# учетом того, что имена категорий уникальны, если новое имя категории нарушает
# уникальность в списке категорий, вызвать исключение ValueError


# class Category:
#
#     categories: list
#
#     def __init__(self):
#         self.categories=[]
#
#     def add(self,title:str):
#         title=title.lower()
#         if title in self.categories:
#             print("такая категория есть")
#             raise ValueError
#         else:
#             print(" такой категории нет, добавим")
#             self.categories.append(title)
#             return self.categories.index(title)
#     def get(self,indexx):
#
#         if len(self.categories) > indexx:
#             return self.categories[indexx]
#         else:
#             raise IndexError
#
#
#     def delete(self,indexx):
#         if len(self.categories) > indexx:
#             del self.categories[indexx]
#         else:
#             pass
#
#     def update(self,indexx,title:str):
#         title = title.lower()
#         if title in self.categories:
#             raise ValueError
#         else:
#             if len(self.categories) > indexx:
#                 self.categories[indexx]=title
#             else:
#                 self.categories.append(title)
#
#     def __str__(self):
#         return self.categories.__str__()
#
# books=Category()
#
# print(books.add("horror"))
# print(books.add("comedy"))
# print(books.add("sexx"))
#
# print(books)
#
# print(books.update(9,"sexx"))
# print(books)

####################################################################################################################
# 4. Изменить класс выше, список категорий должен содержать не просто имена категорий, а
# словари с данными о каждой категории (name: str, is_published: bool), а так же изменить
# методы add, get, delete, update для работы с списком словарей
# 4.1 Добавить метод make_published принимающий индекс категории и меняющий значение
# ключа is_published на True, если такого индекса нет, вызвать исключение IndexError
# 4.2 Добавить метод make_unpublished принимающий индекс категории и меняющий
# значение  ключа is_published на False, если такого индекса нет, вызвать исключение
# IndexError

class Category:

    categories: list

    def __init__(self):
        self.categories=[]

    def add(self,title:dict):
        name=title.get('name')
        for book in self.categories:
            if book.get('name')==name:
                print("такая категория есть")
                raise ValueError

        else:
            print(" такой категории нет, добавим")
            self.categories.append(title)
            return self.categories.index(title)

    def get(self,indexx):

        if len(self.categories) > indexx:
            return self.categories[indexx]
        else:
            raise IndexError


    def delete(self,indexx):
        if len(self.categories) > indexx:
            del self.categories[indexx]
        else:
            pass

    def update(self,indexx,title:dict):
        name = title.get('name')
        for book in self.categories:
            if book.get('name') == name:
                raise ValueError
        else:
            if len(self.categories) > indexx:
                self.categories[indexx]=title
            else:
                self.categories.append(title)

    def make_published(self, indexx):
        if len(self.categories) > indexx:
            self.categories[indexx]['is_published']=True
        else:
            raise IndexError
    def make_unpublished(self, indexx):
        if len(self.categories) > indexx:
            self.categories[indexx]['is_published']=False
        else:
            raise IndexError

    def __str__(self):
        return self.categories.__str__()

books=Category()

print(books.add({"name":"horror","is_published":False}))
print(books.add({"name":"comedy","is_published":False}))
print(books.add({"name":"detectiv","is_published":False}))

print(books)
#print(books.get(2))
#print(books.update(2,{"name":"sex","is_published":False}))
#print(books.delete(8))
print(books.make_published(1))
print(books)
print(books.make_unpublished(1))
print(books)