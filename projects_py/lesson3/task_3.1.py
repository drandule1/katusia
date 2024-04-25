#Пользователь вводит предложение,
#заменить все пробелы в нем на "-" 2мя способами

text=input("введите текст\n")
print(text)
text=text.replace(" ","-")
print(text)



text=input("введите текст\n")
print(text)
myTuple=text.split(" ")
print(myTuple)
text="-".join(myTuple)
print(text)




#my_string = "Это строка с пробелами"
# translation_table = str.maketrans(" ", "-")
# my_string_with_dashes = my_string.translate(translation_table)
# print(my_string_with_dashes)


text=input("введите текст\n")
print(text)
translation_table=str.maketrans(" ", "-")
text=text.translate(translation_table)
print(text)
