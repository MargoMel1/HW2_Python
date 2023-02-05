''' Задание 5. Пользователь вводит строку из нескольких слов,
разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если слово длинное,
выводить только первые 10 букв в слове. '''

sentence = input("Введите строку из нескольких слов, которые разделены пробелами: ")
sentence1 = []
number = 1
for element in range(sentence.count(' ') + 1):
    sentence1 = sentence.split()
    if len(str(sentence1)) <= 10:
        print(f'{number}.{sentence1[element]}')
        number += 1
    else:
        print(f'{number}.{sentence1 [element][0:10]}')
        number += 1