# import time
#
# for i in range(10):    # имя переменной в цикле: i или num или i_num
#     time.sleep(1)
#     print(i)


# for _ in range(10):    # Если переменная в цикле не используется, то вместо имени ставится _
#     print('Привет')


# for i in 'python':
#     print(i + '*', end='')


# for i in 10:           # Число не итерируется!
#     print(i)


# start = int(input('Введите начало: '))
# end = int(input('Введите конец: '))
#
# for i in range(start, end + 1):
#     if i % 2 == 0:
#         print(f'{i} является четным!')


# start = int(input('Введите начало: '))
# end = int(input('Введите конец: '))
#
# for i in range(end, start - 1, -1):
#     print(i)


# summa = 0
#
# for i in range(1, 201):
#     summa += i
#
# print(f'Сумма равна: {summa}')


# Факториал - произведение чисел до выбранного числа
# 3! = 1 * 2 * 3 = 6


# number = int(input('Введите число: '))
# factorial = 1
#
# for i in range(2, number + 1):
#     factorial *= i
#
# print(f'Факториал числа {number} равен: {factorial}!')


# Таблица умножения

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end='\t')
#     print()


# correct_pin = 1547
#
# for i in range(3):
#     pin = int(input('Введите пин-код: '))
#     if pin == correct_pin:
#         print('Ваш пин-код верный!')
#         break
#     else:
#         print('Повторите попытку!')
# else:
#     print('Вы 3 раза неверно ввели пин-код, ваша карта заблокирована!')


# num_1 = int(input('Введите первое число: '))
# num_2 = int(input('Введите второе число: '))
# summa = 0
# count = 0
# for i in range(num_1, num_2 + 1):
#     summa += i
#     count += 1
# else:
#     print(f'Сумма чисел равна: {summa}')
#     print(f'Средняя арифметическая равна: {summa // count}')


# length = int(input('Введите длину линии: '))
# symb = input('Введите символ для заполнения: ')
# count = 1
# for _ in range(length + 1):
#     print(symb, end='')


# num = int(input('Введите число: '))
#
# for i in range(1, 10):
#     print(f'{num} * {i} = {num * i}')


start = int(input('Введите первый диапазон: '))
end = int(input('Введите второй диапазон: '))
num = int(input('Введите число из диапазона: '))

for i in range(start, end + 1):

    if i == num:
        print(f'!{i}!', end=' ')
        continue
    print(i, end=' ')
