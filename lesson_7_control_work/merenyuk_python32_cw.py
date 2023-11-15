# TASK 1

# number = int(input('Введите число: '))
# summ = 0
#
# while number != 0:
#     number = int(input('Введите число: '))
#     summ += number
#
# print(summ)


# TASK 2

# flag = False
# correct_password = 235
#
# while not flag:
#     password = int(input('Введите пароль: '))
#
#     if password != correct_password:
#         print('Неверный пароль!')
#         continue
#     else:
#         print('Пароль верный! Добро пожаловать.')
#         flag = True


# TASK 3

# flag = False
# target = 500000
#
# while not flag:
#     save = int(input('Сколько отложить денег? -> '))
#
#     if save >= target:
#         print('Вы накопили на машину!')
#         flag = True
#     else:
#         print('Копим дальше!')
#         continue


# TASK 4

# num = '9874315351234'
# num_list = list(map(int, num))
# summa = 0
#
# for i in num_list[::-1]:
#     if i == 5:
#         break
#     summa += i
# print(f'Обнаружен разрыв!\n{summa}')


# TASK 5

# import time
#
# count = 10
#
# while count >= 0:
#     if count == 0:
#         print('Время вышло!')
#     else:
#         print(count)
#         time.sleep(1)
#     count -= 1


# TASK 6

# flag = False
#
# while not flag:
#     answer = int(input('Который час? (Нажмите 0 для окончания работы программы) -> '))
#
#     if answer == 0:
#         print('Программа закончила свою работу!')
#         flag = True
#     elif answer == 1:
#         print('Ку-ку ' * answer)
#     elif answer == 2:
#         print('Ку-ку ' * answer)
#     elif answer == 3:
#         print('Ку-ку ' * answer)
#     elif answer == 4:
#         print('Ку-ку ' * answer)
#     elif answer == 5:
#         print('Ку-ку ' * answer)
#     elif answer == 6:
#         print('Ку-ку ' * answer)
#     elif answer == 7:
#         print('Ку-ку ' * answer)
#     elif answer == 8:
#         print('Ку-ку ' * answer)
#     elif answer == 9:
#         print('Ку-ку ' * answer)
#     elif answer == 10:
#         print('Ку-ку ' * answer)
#     elif answer == 11:
#         print('Ку-ку ' * answer)
#     elif answer == 12:
#         print('Ку-ку ' * answer)
#     else:
#         print('Вы ввели некорректный час!')
#         continue


# TASK 7

# import time
#
# sec = (int(input('Введите кол-во секунд: ')))
#
# for i in range(sec, 0, -1):
#     print(i)
#     time.sleep(1)
#
# print('Я иду искать!')


# TASK 8

# text = input('Введите тескт: ')
#
# print(f'Больших букв Ы: {text.count("Ы")}')
# print(f'Маленьких букв ы: {text.count("ы")}')


# TASK 9

# string = 'Кажется, я забыл выключить утюг.'
#
# print(string.title())


# TASK 10

# import random
#
# summa = 0
# errors = [AttributeError, ArithmeticError, EOFError, NameError, LookupError, OSError, TypeError, ValueError]
#
# while summa < 666:
#     chance = random.randint(1, 13)
#     if chance == 2:
#         raise (random.choice(errors))('Вы не успели!')
#
#     num = int(input('Введите число: '))
#     summa += num


# TASK 11

# string = 'abcdehqwertyhzxcvbnm'
#
# first = string.index('h')
# second = string[::-1].index('h')
#
# print(string[-(second + 1) - 1:first:-1])


