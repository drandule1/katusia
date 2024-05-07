
# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы остались только строки, использование дополнительного списка
# незаконно


spisok=['lll',556,5.7,{1,4},9,4,"katya",(7,9)]

i=0
while i<len(spisok):
    if type(spisok[i])==str:
        i+=1
    else:
        del spisok[i]

print(spisok)

#
# print(spisok)
# print(spisok[::-1])# срез дает нов список
# spisok=spisok[::-1]

#spisok.reverse()#сам список развернулся
#print(spisok)