#Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны

slovar={"франция":["париж", "кале", "леон"],
        "беларусь":["минск","могилев","солигорск"],
        "италия":["верона","пиза","рим"]}
gorod=input("введите город ").lower()
for key, value in slovar.items():
    #print(f"{key}: {value}")
    if gorod in value:
        print(f"данный город {gorod} в стране {key}")
        break
else:
    print(f"нет города {gorod}")
