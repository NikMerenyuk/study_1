# print("Hello World!")

# \t - табуляция
# \n - переход на новую строку

# print('Hello', 'Nikita', '!', sep='\t', )

# print('Hello Python!', end=' ')
# print('Hello Ruby!', end=' ')
# print('Hello Java!')

# number_1 = 50
# number_2 = 75

# print(number_1 + number_2)
#
# print(number_1 * number_2)

# print(number_2 // number_1)  # Целочисленное деление
#
# print(number_2 % number_1) # Остаток от деления


# value_1 = '41'
# value_2 = '56'
# # Конкатенция - сложение строк
# print(value_1 * value_2)

# value_1 = 41
# value_2 = 56
#
# value_1 = 10
# print(value_1)


# number = int(5.6)
#
# print(number)

# print(8e+6)

# print(type(str(45)))


# Boolean -> bool()

# print(bool(1))
# print(bool(0))  # False
# print(bool(-2))
# print(bool(''))  # False
# print(bool('asdfqa'))

# print(round(1.1 + 2.2, 1) == 3.3)  # round - округляет число, второй атрибут - кол-во симв после точки

# print(15 > 22)
# print(15 < 22)
# print(15 >= 22)
# print(15 <= 22)
# print(15 != 22)
# print('a' > 'v') # Сравнивается по таблице ASCII

# name = str(input('Введите имя: '))
# age = int(input('Введите возраст: '))

# print('Привет, ' + name + '!' + ' Тебе уже ' + str(age) + ' лет!')

# print('Привет, {val_1}! Тебе уже {val_2} лет!'.format(val_1=name, val_2=age))  # Старый метод!!

# print('Привет, {0}! Тебе уже {1} лет!'.format(name, age))  # Старый метод!!

# print(f'Привет, {name}! Тебе уже {age} лет!')  # Новый метод!! Работает быстрее чем ^


# number = int(input('Введите трехзначное число: '))
#
# first_num = number // 100
# second_num = number // 10 % 10
# third_num = number % 10
#
# print(f'{first_num}\n{second_num}\n{third_num}\n{first_num + second_num + third_num}')


# import time
#
# print(time.time() // 3600 // 24 // 365)  # Кол-во годов с 1970 г.


# num_1 = input('Введите первое число: ')
# num_2 = input('Введите второе число: ')
#
# print(f'{num_1 + num_2}')


# temp_с = int(input('Введите температуру по шкале Цельсия: '))
#
# print(f'По шкале Фаренгейта эта температура равна: {1.8 * temp_с + 32}')


num = int(input('Введите четырехзначное число: '))

first_num = num // 1000
second_num = num // 100 % 10
third_num = num // 10 % 10
fourth_num = num % 10

print(first_num)
print(second_num)
print(third_num)
print(fourth_num)

print(f'{first_num * second_num * third_num * fourth_num}')

# print(f'{fourth_num}{third_num}{second_num}{first_num}')


# num = int(input('Введите число от 1 до 100: '))
#
# if num % 3 and num % 5 == 0:
#     print('Fizz Buzz')
# elif num % 3 == 0:
#     print('Fizz')
# elif num % 5 == 0:
#     print('Buzz')
# elif num % 3 and num % 5 != 0:
#     print(num)









