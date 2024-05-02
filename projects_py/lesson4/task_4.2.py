def count_letters(text):
    letter_count = {}
    for char in text:
        if char.isalpha():  # Проверяем, является ли символ буквой
            char = char.lower()  # Приводим символ к нижнему регистру
            letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count

user_input = input("Введите текст: ")
result = count_letters(user_input)
print("Количество вхождений каждой буквы:")
for letter, count in result.items():
    print(f"'{letter}': {count}")