# Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
# словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
# имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
# пустая строка)
#
slovar={"1":{"name":"Женя","surname":"Шевцов","pfone": "223344", "email":"llaa@com"},
        "2":{"name":"Виталик","surname":"Шевцов","pfone": "22332884", "email":""},
        "3":{"name":"Катя","surname":"Шевцова","pfone": "22332884"}}


for key, value in slovar.items():
    #print(f"{key}: {value}")
    if value.get("email")==None or value.get("email")=="":
         print(value.get("name"))