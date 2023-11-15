num = int(input('Введите число: '))

while num != 7:
    if num > 0:
        print('Number is positive')
    elif num < 0:
        print('Number is negative')
    else:
        print('Number is equal to zero')
    num = int(input('Введите число: '))
else:
    print('Good bye!')
