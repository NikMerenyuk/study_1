try:
    num_1 = int(input('Введите первое число: '))
    num_2 = int(input('Введите второе число: '))
    num_3 = int(input('Введите третье число: '))
    action = input('Вывести максимум из трех чисел (1); Вывести минимум из трех чисел (2); '
                   'Вывести среднеарифметическое из трех чисел (3) ')

    if action not in ('1', '2', '3'):
        raise ValueError
    elif action == '1':
        if num_1 == num_2 == num_3:
            print(f'Все числа равны.')
        elif num_2 < num_1 > num_3 or num_1 == num_2 > num_3 or num_1 == num_3 > num_2:
            print(f'Наибольшее число: {num_1}.')
        elif num_1 < num_2 > num_3 or num_2 == num_3 > num_1:
            print(f'Наибольшее число: {num_2}.')
        elif num_1 < num_3 > num_2:
            print(f'Наибольшее число: {num_3}.')
    elif action == '2':
        if num_1 == num_2 == num_3:
            print(f'Все числа равны.')
        elif num_2 > num_1 < num_3 or num_1 == num_2 < num_3 or num_1 == num_3 < num_2:
            print(f'Наименьшее число: {num_1}.')
        elif num_1 > num_2 < num_3 or num_2 == num_3 < num_1:
            print(f'Наименьшее число: {num_2}.')
        elif num_1 > num_3 < num_2:
            print(f'Наименьшее число: {num_3}.')
    elif action == '3':
        print(f'Срденеарифметическое из трех чисел: {round((num_1 + num_2 + num_3) / 3, 2)}.')

except ValueError:
    print('Нужно ввести числа и выбрать действие!')
