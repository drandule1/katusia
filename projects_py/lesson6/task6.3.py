#Код Морзе для представления цифр и букв использует тире и точки. Напишите
#функцию для кодирования текста



morse_code = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',    'E': '.',
    'F': '..-.',   'G': '--.',    'H': '....',   'I': '..',     'J': '.---',
    'K': '-.-',    'L': '.-..',   'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',   'Y': '-.--',
    'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',  '3': '...--',  '4': '....-',
    '5': '.....',  '6': '-....',  '7': '--...',  '8': '---..',  '9': '----.'
}

def morze(text):
    print(text)
    morse_str=""
    for i in text:# разбиваю строки на элементы побуквенно
        print(i)#вывожу эти буквы
        print(morse_code.get(i.upper()))
        morse_str=morse_str+" "+morse_code.get(i.upper(),'')
    print(morse_str)
    return morse_str


text=input("Введите текст только на английском!!!!!   ")

print(morze(text))


