# TASK 1

primer = '23+12'

if '+' in primer:
    print(sum(list(map(int, primer.split('+')))))
elif '-' in primer:
    mylist1 = list(map(int, primer.split('-')))
    print(mylist1[0] - mylist1[1])
elif '*' in primer:
    mylist1 = list(map(int, primer.split('*')))
    print(mylist1[0] * mylist1[1])
elif '/' in primer:
    mylist1 = list(map(int, primer.split('/')))
    print(mylist1[0] / mylist1[1])


# TASK 2

# numbers = [3, -31, 50, 29, 0, -64, 51, 30, 68, -76, 52, 0]
# count_negative = 0
# count_positive = 0
# count_zero = 0
#
# print(f'Минимальное число: {min(numbers)}')
# print(f'Максимальное число: {max(numbers)}')
# for i in numbers:
#     if i == 0:
#         count_zero += 1
#     elif i > 0:
#         count_positive += 1
#     else:
#         count_negative += 1
# print(f'Кол-во отрицательных элементов: {count_negative}')
# print(f'Кол-во положительных элементов: {count_positive}')
# print(f'Кол-во нулей: {count_zero}')

