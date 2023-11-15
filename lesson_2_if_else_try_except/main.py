# age = int(input('Введите ваш возраст: '))
#
# if 18 <= age <= 70:
#     print('Вы можете зарегистрироваться.')
# else:
#     print('Вы не можете зарегистрироваться.')


# weekday = int(input('Введите номер дня недели: '))
#
# if weekday == 1:
#     print('Понедельник')
# elif weekday == 2:
#     print('Вторник')
# elif weekday == 3:
#     print('Среда')
# elif weekday == 4:
#     print('Четверг')
# elif weekday == 5:
#     print('Пятница')
# elif weekday == 6:
#     print('Суббота')
# elif weekday == 7:
#     print('Воскресенье')
# else:
#     print('Такого дня недели нет!')


# email_input = input('Введите свой email: ')
# password_input = input('Введите свой пароль: ')
#
# email = 'nikmerenyuk@gmail.com'
# password = '12345nik'
#
# authorization = False
#
# if email == email_input:
#     if password == password_input:
#         authorization = True
#         print('Вы авторизировались!')
#     else:
#         print('Пароль неверный!')
# else:
#     print('Неверный email!')
#
#
# match authorization:
#     case True:
#         print('Пользователь успешно авторизовался')
#
#     case False:
#         print('Пользователь не авторизовался')
#
#     case _:
#         print('Else')


# number = int(input('Введите число: '))
#
# if number % 2 == 0:
#     print('Четное!')
# else:
#     print('Нечетное!')


# from math import sqrt
#
# a = float(input('Введите коэффициент a: '))
# b = float(input('Введите коэффициент b: '))
# c = float(input('Введите коэффициент c: '))
#
# D = b**2 - 4 * a * c
#
# if D < 0:
#     print('Корней нет!')
#
# elif D == 0:
#     x = -b / (2 * a)
#
#     print(f'x={round(x, 2)}')
#
# else:
#     x1 = (-b + sqrt(D)) / (2 * a)
#     x2 = (-b - sqrt(D)) / (2 * a)
#
#     print(f'x1={round(x1, 2)} x2={round(x2, 2)}')


# number_1 = int(input('1-ое число: '))
# number_2 = int(input('2-ое число: '))
#
# try:
#     print(number_1 / number_2)
# except ZeroDivisionError:   # Запускается если возникла ошибка
#     print('На ноль делить нельзя!')
# else:                       # Запускается если ошибки НЕ возникло
#     print('Программа выполнилась без ошибок!')
# finally:                    # Запускается всегда
#     print('Запустился блок finally')

# if number_2 == 0:
#     print('На ноль делить нельзя!')
# else:
#     print(number_1 / number_2)


# BaseException - родительская ошибка


# try:
#     raise ValueError
# except KeyError:
#     print('Обработчик ошибки 1')
#
# except ValueError:
#     print('Обработчик ошибки 2')


# try:
#     year = int(input('Введите год: '))
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         print('Год високосный!')
#     else:
#         print('Год не високосный!')
#     raise TypeError
#
# except (ValueError, TypeError):
#     print('Год должен быть числом!')

# try:
#     number = int(input('Введите число: '))
#
#     if number % 7 == 0:
#         print(number)
#         print('Number is multiple 7')
#     else:
#         print('Number is not multiple 7')
#
# except ValueError:
#     print('Необходимо ввести число!')


# try:
#     num_1 = int(input('Введите первое число: '))
#     num_2 = int(input('Введите второе число: '))
#
#     if num_1 > num_2:
#         print(f'Число {num_1} больше!')
#     else:
#         print(f'Число {num_2} больше!')
#
# except ValueError:
#     print('Необходимо ввести числа!')


# try:
#     num_1 = int(input('Введите первое число: '))
#     num_2 = int(input('Введите второе число: '))
#
#     if num_1 < num_2:
#         print(f'{num_1}, {num_2}')
#     elif num_2 < num_1:
#         print(f'{num_2}, {num_1}')
#     else:
#         print('Числа равны!')
#
# except ValueError:
#     print('Необходимо ввести числа!')


# try:
#     num_1 = int(input('Введите первое число: '))
#     num_2 = int(input('Введите второе число: '))
#     action = input('Выберите действие (+ (сумма), - (разница), u (среднее арифметическое), * (произведение)): ')
#
#     if action not in ('*', '-', '+', 'u'):
#         raise ValueError
#
#     if action == '+':
#         print(num_1 + num_2)
#     elif action == '-':
#         print(num_1 - num_2)
#     elif action == 'u':
#         print((num_1 + num_2) / 2)
#     elif action == '*':
#         print(num_1 * num_2)
#
# except ValueError:
#     print('Необходимо ввести числа и действие из списка!')


# try:
#     sec = int(input('Введите кол-во секунд, прошедшее с 12:00: '))
#     action = input('Рассчитать сколько осталось до полуночи: в секундах (1); в минутах (2); в часах (2): ')
#
#     if action not in ('1', '2', '3'):
#         raise ValueError
#
#     if action == '1':
#         print(f'До полуночи в секундах осталось {43200 - sec}!')
#     elif action == '2':
#         print(f'До полуночи в минутах осталось {round((43200 - sec) / 60, 2)}!')
#     elif action == '3':
#         print(f'До полуночи в минутах осталось {round((43200 - sec) / 3600, 2)}!')
#
# except ValueError:
#     print('Необходимо выбрать число и действие из списка!')


# try:
#     d = int(input('Введите диаметр окружности: '))
#     action = input('Рассчитать: 1 - площадь; 2 - периметр. ')
#
#     if action not in ('1', '2'):
#         raise ValueError
#
#     if action == '1':
#         print(f'Площадь окружности равна: {3.14 * d**2 // 4}.')
#     elif action == '2':
#         print(f'Периметр окружности равен: {3.14 * d}.')
#
# except ValueError:
#     print('Необходимо выбрать число и действие из списка!')


# num = int(input('Введите целое число: '))
#
# if 0 > num or num > 23:
#     print('Ошибка')
# elif 7 <= num <= 10:
#     print('Пора вставать!')
# else:
#     print('Ты проспал!')

#
# result1 = int(input('Введите количество баллов по первому предмету: '))
# result2 = int(input('Введите количество баллов по второму предмету: '))
# result3 = int(input('Введите количество баллов по третьему предмету: '))
#
# sum = result1 + result2 + result3
#
# if sum >= 250:
#     print('Вы поступили на бюджет!')
# else:
#     print('Вы НЕ поступили на бюджет.')


# n = int(input('Введите кол-во минут: '))
#
# print(f'{n // 60} ч, {n % 60} мин')
