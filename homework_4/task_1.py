start = int(input('Введите начало диапазона: '))
end = int(input('Введите конец диапазона: '))

for i in range(start, end + 1):
    if i % 7 == 0:
        print(i, end=' ')
