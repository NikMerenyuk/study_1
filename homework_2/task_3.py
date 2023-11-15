try:
    m = int(input('Введите метры: '))
    action = input('Перевести метры в мили (1); перевести метры в дюймы (2); перевести метры в ярды (3): ')

    if action not in ('1', '2', '3'):
        raise ValueError
    elif action == '1':
        print(f'При переводе в мили получается: {round(m / 1609, 9)}.')
    elif action == '2':
        print(f'При переводе в дюймы получаеся: {m * 39.37}')
    elif action == '3':
        print(f'При переводе в ярды получается: {m * 1.094}')

except ValueError:
    print('Нужно ввести числа и выбрать действие!')
