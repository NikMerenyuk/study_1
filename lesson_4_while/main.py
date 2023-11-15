# num = int(input('Введите число: '))
#
# factorial = 1
#
# while num >= 1:
#     factorial *= num
#     num -= 1
#
# print(factorial)

# summa = 0
#
# while True:
#     number = float(input('Введите число или 0 чтобы закончить цикл: '))
#     if number == 0:
#         print(summa)
#         break
#     summa += number


# debt = 1000
# tries = 3
#
# while debt > 0:
#     money = int(input(f'Ваш долг составляет {round(debt, 2)}, сколько вы готовы внести: '))
#
#     if money <= 0:
#         print('Сумма не может быть меньше либо равной нулю!')
#         continue
#     if tries > 0:
#         debt -= money
#     else:
#         print('Теперь начисляются проценты!')
#         debt *= 1.1
#         debt -= money
#     tries -= 1
#
# print('Вы закрыли Долг!')


# import random
#
#
# flag = True
#
#
# print('Программа на проверку знаний таблицы умножения.')
# lvl_choice = int(input('Выберите уровень сложности (1 или 2): '))
#
# while flag:
#     if lvl_choice == '1':
#         number_1 = random.randint(1, 10)
#         number_2 = random.randint(1, 10)
#     else:
#         number_1 = random.randint(5, 12)
#         number_2 = random.randint(5, 12)
#
#     result = number_1 * number_2
#
#     answer = int(input(f'{number_1} * {number_2} = '))
#
#     while answer != result:
#         print('Неверно! Попробуй еще раз.')
#         answer = int(input(f'{number_1} * {number_2} = '))
#
#     if answer == result:
#         print('Верно!')
#     else:
#         print('Неверно! Попробуй еще раз.')
#
#     choice = input('Продолжаем? Да/Нет -> ')
#
#     if choice == 'Нет' or choice == 'нет':
#         flag = False


# import random
#
#
# guess_number = random.randint(1, 500)
# guessed = False
# tries = 7
#
# while not guessed:
#     number = int(input('Угадайте число от 1 до 500: '))
#
#     if tries == 0:
#         print('Вы проиграли!')
#         break
#
#     if number == guess_number:
#         print('Вы угадали!')
#         guessed = True
#     elif number < guess_number:
#         print('Загаданное число больше!')
#     elif number > guess_number:
#         print('Загаданное число меньше!')
#
#     tries -= 1


# x = int(input('Введите x: '))
# y = int(input('Введите y: '))
# s = 1
#
# while y >= 0:
#     s *= x
#     y -= 1
#
# print(s)


amount_1 = 0
amount_2 = 0

for i in range(100, 999 + 1):
    first_num = i // 100
    second_num = i // 10 % 10
    third_num = i % 10

    if first_num != second_num and first_num != third_num and second_num != third_num:
        amount_1 += 1


for j in range(1000, 9999 + 1):
    a = j // 1000
    b = j // 100 % 10
    c = j // 10 % 10
    d = j % 10

    if a != b and a != c and a != d and b != c and b != d and c != d:
        amount_2 += 1

print(amount_1 + amount_2)
