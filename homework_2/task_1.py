try:
    num_1 = int(input('Введите первое число: '))
    num_2 = int(input('Введите второе число: '))
    num_3 = int(input('Введите третье число: '))
    action = input('Числа сложить (1) или умножить (2)? ')

    if action not in ('1', '2'):
        raise ValueError
    elif action == '1':
        print(f'Сумма чисел равна: {num_1 + num_2 + num_3}.')
    elif action == '2':
        print(f'Произведение чисел равно: {num_1 * num_2 * num_3}.')


except ValueError:
    print('Нужно ввести числа и выбрать действие!')
