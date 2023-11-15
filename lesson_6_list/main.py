# Список ИЗМЕНЯЕМЫЙ тип данных!

# my_list_1 = []  # пустой список
# my_list_1 = ['Moscow', 'Ekaterinburg', 'Samara', 'Novosibirsk', ]  # запятая в конце ставится, если позже будет еще пополнятся
# my_list_2 = list(())   # пустой список
# my_list_2 = list(('Moscow', 'Ekaterinburg', 'Samara', 'Novosibirsk', ))
#
# print(my_list_1)
# print(my_list_2)
# print(sys.getsizeof(my_list_1))
# print(sys.getsizeof(my_list_2))


# my_list_1 = ['Moscow', 'Samara', 'Novosibirsk', 'Yekaterinburg', 'Yekaterinburg']

# print(my_list_1[0])
# print(my_list_1[1:])
# print(my_list_1[::2])
# print(my_list_1[::-1])

# my_list_1.append('Vladivostok')         # Добавляет в конец списка
# my_list_1.append('Vladivostok')
# my_list_1.remove('Vladivostok')         # Удаляет элемент списка по значению (только первое вхождение)
# del_city = my_list_1.pop(0)             # Удаляет по индексу (по умолчанию -1) (возвращает удаленный элемент, если задать переменную)
# my_list_1.insert(0, 'Chelyabinsk')      # Вставляет элемент по указанном индексу
# print(my_list_1.index('Ekaterinburg'))  # Возвращает индекс элемента (первое вхождение)
# print(my_list_1.count('Ekaterinburg'))  # Возвращает кол-во конкретного элемента
# my_list_1[3] = 'Vladivostok'            # Замена элемента в списке
# my_list_1.reverse()

# print(my_list_1)


# my_list_1 = ['Moscow', 'Samara', 'Novosibirsk', 'Yekaterinburg', ]


# for i_city in my_list_1:
#     print(f'Город: {i_city}')

# for index in range(len(my_list_1)):
#     print(f'{index + 1} Город: {my_list_1[index]}')


# start = int(input('Введите начало диапазона: '))
# end = int(input('Введите конец диапазона: '))
# my_list = []
#
# for i in range(start, end + 1):
#     if i % 2 != 0:
#         my_list.append(i)
#
# print(my_list)


# basket_1 = ['Bayern', 'Man Utd', 'Juventus', 'Barcelona']
# basket_2 = ['Real Madrid', 'Man City', 'Milan', 'Porto']
#
# for index in range(len(basket_1)):
#     if index % 2 != 0:
#         print(f'{basket_1[index]} - {basket_2[index - 1]}')
#         print(f'{basket_1[index - 1]} - {basket_2[index]}')


# numbers = [15, 4, 8, 17, 79, 5, 1, 4]
# numbers.sort(reverse=True)             # Сортирует список (reverse=True - отсортирует по убыванию)
# numbers_sorted = sorted(numbers)       # Создается копия списка
# print(numbers)


# string = 'hello*python*java*ruby'
# print(string.split('*'))


# numbers = input('Введите числа через пробел: ').split()

# for i_num in numbers:
#     numbers[numbers.index(i_num)] = int(i_num)

# for index, value in enumerate(numbers):
#     numbers[index] = int(value)

# numbers_int = list(map(int, input('Введите числа через пробел: ').split()))
#
# print(numbers_int)


# films = ['Побег из Шоушенка', 'Зеленая миля', 'Поймай меня если сможешь',
#          'Волк с Уолл-Срит',
#          ]
# liked_films = []
#
# while True:
#     choice = input('1-Посмотреть список избранных фильмов\n'
#                    '2-Добавить фильм в избранное\n'
#                    '3-Удалить фильм из избранного -> ')
#
#     if choice == '1':
#         print(f'Ваш список фильмов: ', *liked_films)
#     elif choice == '2':
#         film = input('Введите название фильма: ')
#         if film in films:
#             if film not in liked_films:
#                 liked_films.append(film)
#                 print('Ваш фильм добавлен!')
#             else:
#                 print('Такой фильм у Вас уже есть!')
#         else:
#             print('Такого фильма в нашей библиотеке нет, добавим его позже...')
#
#     elif choice == '3':
#         film = input('Введите название фильма: ')
#         if film in liked_films:
#             liked_films.remove(film)
#             print('Фильм удален из ваших избранных!')
#         else:
#             print('Такого фильма у Вас нет!')
#     else:
#         print('До новых встреч!')
#         break


# numbers = [1, 25, 78, 7, 4, -9]
#
# print(len(numbers))
# print(sum(numbers))
# print(max(numbers))
# print(min(numbers))


# numbers_list = list(map(str, input('Введите числа через пробел: ').split()))
# number = (input('Введите число, которое нужно посчитать: '))
# count = 0
# #
# # print(f'Число {number} встретилось {numbers_list.count(number)}!')
#
# for number in numbers_list:
#     count += 1
#
# print(count)


# numbers_list = list(map(int, input('Введите числа через пробел: ').split()))
# count = 0
# summa = 0
#
# # print(f'Сумма всех элементов: {sum(numbers_list)}\n'
# #       f'Среднеарифметическая всех элементов: {sum(numbers_list) / len(numbers_list)}')
#
# for i_num in numbers_list:
#     count += 1
#     summa += i_num
#
# print(f'Сумма всех элементов: {summa}\n'
#       f'Среднеарифметическая всех элементов: {summa / count}')


# text = 'hello. bye. hello world.'
#
# sentences = text.split('.')
# new_sentences = []
#
# for i in sentences[:-1]:
#     new_sentences.append(i.lstrip().capitalize() + '. ')
#
# new_text = ''
#
# print(new_text.join(new_sentences))


# list_1 = [1, 2, 3, 4]
# list_2 = [5, 6, 7, 8]

# print(list_1 + list_2)  # Объединение списков
# print(list_1 * 2)       # Дублирование элементов списка
# list_1.extend(list_2)   # Расширение списка элементами второго списка
# print(list_1)

# list_1 = ['1', '2', '3', '4']
#
# string = ' '
# # new_string = string.join(list_1)
# for i in list_1:
#     string += f'{i} '
# print(string)


# List comprehensions  Автоматическое заполнение списка

# import sys
#
# list_1 = [i for i in range(1, 10)]
# list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print(sys.getsizeof(list_1))
# print(sys.getsizeof(list_2))

# print(list_1)


# list_1 = [i for i in range(1, 10) if i % 2 == 0]
# list_1 = [i ** 2 for i in range(1, 10) if i % 2 != 0]
#
# print(list_1)


# list_2 = [i for i in range(1, 5) for _ in range(5)]
# list_3 = [i * j for i in range(1, 5) for j in range(1, 5)]
#
# print(list_3)


# list_4 = [35, 7, 4, 87, 65]
# list_5 = [num for num in list_4 if num % 7 == 0]
#
# print(list_5)


# import string
#
# letters = string.ascii_letters
#
# input_text = 'hell@o m#y na!me is Ni$kita'
#
# letters_list = [letter for letter in input_text if (letter in letters or letter.isspace())]
#
# print(''.join(letters_list).upper())


# import string
#
# digits = string.digits
#
# input_text = 'fasdfh9234rdfsf 89f2j2dsafasd74'
# count = 0
# digits_list = [digit for digit in input_text if digit in digits]
#
# print(''.join(digits_list), len(digits_list))


# students = [
#     ['Петров', 4.5],
#     ['Иванов', 4.2],
#     ['Сидоров', 4.1],
#     ['Иванова', 3.5],
#     ['Петрова', 4.9],
# ]

# students_2 = [student for student in students if student[1] >= 4.5]
#
# print(students_2)


# nums = [1, 7, 3, 6, 5, 6]
# # nums = [2, 1, -1]
# pivot = -1
#
# for i in range(len(nums)):
#     if len(nums[:i]) == len(nums[i + 1:]):
#         pivot = i
#         break
# print(pivot)

# list_1 = [i for i in range(1, 5) for j in range(1, 4)]
#
# print(list_1)

lost_1 = ['5', '4', '0', '4', '2', '4', '95']

for i in lost_1:
    lost_1.remove('4')

print(lost_1)
