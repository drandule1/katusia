# global_var = 10  # Глобальная переменная
#
# def my_function():
#     local_var = 5  # Локальная переменная
#     print(global_var)  # Можно обратиться к глобальной переменной из функции
#     print(local_var)
#

# my_function()
# print(local_var)


from random import randint
def Sicle(r):
    P=3.14
    S=P*r*r
    return S # верни  это значение S  из функции

def Volium(a,b,c):
    print(a,b,c,sep="----")
    V=a*b*c
    return V # верни  это значение V  из функции

#vol=Volium(3,4,5)

#print(vol)
summ=0
for y in range(1,11):
    v=Volium(randint(1,10), randint(1,10),randint(1,10))
    print(v)
    summ=summ+v

print(summ)










#
# circle1=Sicle(5)# исполни функцию с таким то параметром
# print(circle1)
#
#
# summ= Sicle(1)+Sicle(2)+Sicle(3)+Sicle(4)+Sicle(5);
# print(summ)
#
# summ=0;
# for x in range(1,6):
#
#     summ=summ+Sicle(x)
#
# print(summ)