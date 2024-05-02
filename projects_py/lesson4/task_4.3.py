def fill_dictionary(n):
    data = {}
    for i in range(n + 1):
        name = input(f"Введите имя для элемента {i}: ")
        email = input(f"Введите email для элемента {i}: ")
        data[i] = {"name": name, "email": email}
    return data

n = int(input("Введите значение n: "))
result = fill_dictionary(n)
print("Заполненный словарь:")
for key, value in result.items():
    print(f"{key}: {value}")


print(result.get(0))

# { 0: {'name': 'lala', 'email': 'lala@lala'}
# 1: {'name': 'didi', 'email': 'didi@lala'}
# 2: {'name': 'iiii', 'email': 'ii@lala'}  }
#
#