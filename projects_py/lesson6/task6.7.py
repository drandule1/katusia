#Дан список рандомных чисел, необходимо отсортировать его в виде, сначала
#  четные, потом нечётные

def lala(a):
    if a%2!=0:
        return True
    else:
        return False

def lala1(a):
    return len(str(a))




import  random
n=15
spisok=[random.randint(0,100) for i in range(0,n)]

print(spisok)

spisok.sort(key=lala)
print(spisok)



# n=15
# spisok=[random.randint(0,1001) for i in range(0,n)]
#
# print(spisok)
#
# spisok.sort(key=lala1)
# print(spisok)
#
