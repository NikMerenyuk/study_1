start = int(input('Введите начало диапазона: '))
end = int(input('Введите конец диапазона: '))

even = 0
odd = 0
mult = 0
count_even = 0
count_odd = 0
count_mult = 0

for i in range(start, end + 1):
    if i % 2 == 0:
        even += i
        count_even += 1
        if i % 9 == 0:
            mult += i
            count_mult += 1
    elif i % 2 != 0:
        odd += i
        count_odd += 1
        if i % 9 == 0:
            mult += i
            count_mult += 1

else:
    print()
    print(f'Сумма четных чисел равна: {even}')
    print(f'Средняя арифметическая четных чисел равна: {even / count_even}')
    print(f'Сумма нечетных чисел равна: {odd}')
    print(f'Средняя арифметическая нечетных чисел равна: {odd / count_odd}')
    if count_mult != 0:
        print(f'Сумма чисел кратных 9 равна: {mult}')
        print(f'Средняя арифметическая чисел кратных 9 равна: {mult / count_mult}')
    else:
        print(f'Невозможно произвести расчеты с числами кратными 9, т.к. конец диапазона меньше 9!')
