
# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int



#Перевод 2-10
dvoich=input("введите двоичное число ")
chislo=0
for i,g in enumerate(dvoich[::-1]):
    #print(i,g)
    if g=="1":
        chislo+=2**i
    else:
        pass
print(chislo)
#Перевод 10-2
p=[]
finish=''
desyatich=int(input("введите десятичное число "))
while desyatich!=0:
    ost=desyatich%2
    desyatich=desyatich//2
    finish=finish+(str(ost))
    print(desyatich,ost)

print(finish[::-1])