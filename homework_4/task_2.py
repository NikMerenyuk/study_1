start = int(input('Введите начало диапазона: '))
end = int(input('Введите конец диапазона: '))
counter = 0

for i in range(start, end + 1):
    print(i, end=' ')
print()
for j in range(end, start - 1, -1):
    print(j, end=' ')
print()
for k in range(start, end + 1):
    if k % 7 == 0:
        print(k, end=' ')
print()
for n in range(start, end + 1):
    if n % 5 == 0:
        counter += 1
print(counter, end=' ')
