# string = 'Hello'
#
# encode_string = string.encode(encoding='utf8')
# print(encode_string)
# decoded_string = encode_string.decode(encoding='utf8')
# print(decoded_string)

# string = 'abcdefg'                  # строка НЕИЗМЕНЯЕМЫЙ тип данных!
# print(len(string))                  # длина  строки
#
# print(string[0])                    # получение символа из строки по индексу
#
# print(string[-1])                   # последний символ
# print(string[len(string) - 1])      # последний символ
#
# print(string[0:3])                  # срез
# print(string[3:])                   # срез
#
# print(string[0:5:2])                # с шагом
# print(string[-1:-4:-1])
#
# print(string[::-1])                   # переворачивает строку


# example = '0123456789'
#
# print(example[0:3])
# print(example[3:6])
# print(example[-1:-3:-1])
# print(example[::2])
# print(example[::-1])
# print(example[5:2:-1])
# print(example[-2:3:-2])
# print(example[4:0:-1])
# print(example[4:2:-1] + example[1:3])


# text = 'pytHon is a prOgrAmming LanGuage'
#
# print(text.capitalize())            # Первый символ в верхний регистр, а остальные в нижний
# print(text.title())                 # Каждый первый символ нового слова с большой буквы
# print(text.count('p'))              # Считает сколько раз встречается (то, что в скобках) в строке
# print(text.lower())                 # Приводит все к нижнему регистру
# print(text.upper())                 # Приводит все к верхнему регистру
# print(text.replace('p', 't'))       # Замена символа в строке на новый
# print(text.index('n'))              # Узнать индекс символа, но только до первого нахождения
#                                                     #(если символа нет, то вернет ValueError)
# print(text.find('ж'))               # То же самое, но не выкинет ошибку, если символа нет в строке, то вернет -1
# print(text.index('LanG'))           # Если ввести несколько символов - то укажет с какого индекса начинается
# print(len(text))
# print(len(text.strip()))            # Убирает пробелы по бокам (lstrip - убирает пробел слева;
#                                                               # rstrip - убирает пробел справа)
# print(text.swapcase())              # Все большие становятся маленькими, а маленькие - большими


# БУЛЕВЫЕ МЕТОДЫ

# string_2 = 'python123ruby78'
#
# print(string_2.isalnum())           # Если есть какие-то символы кроме БУКВ или ЦИФР - False, иначе - True
# print(string_2.isalpha())           # Если только БУКВЫ - True, иначе - False
# print(string_2.isdigit())           # Если только ЦИФРЫ - True, иначе - False
# print(string_2.islower())           # Проверка на нижний регистр
# print(string_2.isupper())           # Проверка на верхний регистр
# print(string_2.isascii())           # Проверка наличия символов в таблице ASCII
# print(string_2.isdecimal())         # Целое ли число
# print(string_2.isnumeric())         # То же самое
# print(string_2.isspace())           # Проверяет стоит ли строка только из пробелов


# string_2 = '+7python123r@uby78.ru'
#
# print(string_2.startswith('+7p'))       # Проверяет с чего начинается строка
# print(string_2.endswith('y78.ru'))      # Проверяет на что заканчивается строка
# print('@' in string_2)                  # Проверка вхождения (есть ли этот символ в строке)


# string_3 = 'python+ruby+js'
#
# print(string_3.split('+'))                 # Делит список по указанным параметрам


# text = input('Введите тескт: ')
#
# print(f'Больших букв Ы: {text.count("Ы")}')
# print(f'Маленьких букв ы: {text.count("ы")}')


# ПРОГРАММА ДЛЯ РЕГИСТРАЦИИ

# registration = False
#
# while not registration:
#     email = input('Введите свой Email: ')
#
#     if ('@' in email) and (email.endswith('.com')) or (email.endswith('.ru')):
#         password1 = input('Введите пароль: ')
#         password2 = input('Подтвердите пароль: ')
#
#         if password1 == password2:
#             if len(password1) == 8 and password1.isalnum() and not password1.isalpha() and not password1.isdigit():
#                 print('Вы зарегистрированы!')
#                 registration = True
#             else:
#                 print('Пароль должен быть длиной 8 символов и т.д.')
#
#         else:
#             print('Пароли должны совпадать!')
#     else:
#         print('Email должен содержать @ и заканчиваться на .com или .ru')


# РЕГИСТРАЦИЯ ПО НОМЕРУ ТЕЛЕФОНА


# registration = False
#
# while not registration:
#     tel = input('Введите номер телефона в формате +79ххххххххх: ')
#
#     if tel.startswith('+79') and len(tel) == 12 and tel[1:].isdigit():
#         name = input('Введите ваше имя: ')
#         surname = input('Введите вашу фамилию: ')
#
#         if name.isalpha() and surname.isalpha():
#             print(f'Ваше имя: {name.capitalize()}\n'
#                   f'Ваша фамилия: {surname.capitalize()}\n'
#                   f'Номер телефона: {tel}')
#             registration = True
#         else:
#             print('Невалидные имя или фамилия!')
#     else:
#         print('Невалидный номер телефона!')


# text = input('Введите текст: ')
# print(text[::-1])


# text = input()
# num = 0
# letter = 0
#
# for i in text:
#     if i.isdigit():
#         num += 1
#     elif i.isalpha():
#         letter += 1
# print(num)
# print(letter)


# text = input('Введите текст: ')
# symb = input('Введите искомый символ: ')
#
# print(text.count(symb))


# text = input('Введите текст: ')
# word = input('Введите искомое слово: ')
#
# print(text.count(word))


# text = input('Введите текст: ')
# word = input('Введите заменяемое слово: ')
# word_rep = input('Введите слово на замену: ')
#
# print(f'{text.replace(word, word_rep)}')


# st = input()
# subst = input()
#
# if subst.lower() in st.lower():
#     print('Есть контакт!')
# else:
#     print('Мимо!')



