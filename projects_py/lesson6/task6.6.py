# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка
spisok=[1,556,57,5,9,4]
lengs=len(spisok)# узнаю длину списка
for i,g in enumerate(spisok):
    print(i,g)
    if i==0:
        print(spisok[1]+spisok[-1])
    elif i==lengs-1:
        print(spisok[-2]+spisok[0])
    else:
        print(spisok[i+1]+spisok[i-1])
