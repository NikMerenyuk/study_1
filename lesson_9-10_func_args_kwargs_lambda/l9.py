# ПОЗИЦИОННЫЕ АРГУМЕНТЫ

# def summa(a, b, c):
#     return a + b + c
#
#
# print(summa(10, 10, 14))

# def print(string):
#     return
#
#
# print('Hello')

# value_1 = 10
#
#
# def my_function():  # Если нет return в функции, то она называется ПРОЦЕДУРОЙ
#     global value_1
#     value_1 = 0
#     print(value_1)
#
#
# my_function()
# print(value_1)


# val_1 = 1
#
#
# def func_1():
#     val_2 = 2
#
#     def func_2():       # Последняя вложенная функция называется ЗАМЫКАЮЩЕЙ ФУНКЦИЕЙ
#         val_3 = 3
#         print(val_3)
#
#     print(val_2)
#     func_2()
#
#
# print(val_1)
# func_1()


# def check_is_happy_num(number: str) -> bool:
#     """
#     Проверяет является ли число счастливым
#     :param number: str
#     :return: bool
#     """
#     left: int = int(number[0]) + int(number[1]) + int(number[2])
#     right: int = int(number[3]) + int(number[4]) + int(number[5])
#
#     if left == right:
#         return True
#
#     return False
#
#
# print(check_is_happy_num('123420'))


# from typing import List
#
#
# def average_age(people: List[list]) -> float:     # List[any] - внутри списка может находится любой тип данных
#     """
#     Функция среднего возраста
#     :param people: List[list]
#     :return: float
#     """
#     average: int = sum([i_human[1] for i_human in people])
#     return round(average / len(people), 1)
#
#
# people_list = [
#     ['Ivan', 35],
#     ['Petr', 27],
#     ['Anna', 18],
# ]
#
# print(average_age(people_list))


# def odd_nums(a: int, b: int) -> int:
#     """
#     Функция отображает все нечетные числа между числами параметров
#     :param a: int
#     :param b: int
#     :return: int
#     """
#
#     for i in range(a, b + 1):
#         if i % 2 != 0:
#             print(i)
#
#
# print(odd_nums(3, 15))


# def line(length: int, direction: bool, symbol: str) -> str:
#     """
#     Функция отображает вертикальную или горизонтальную линию из некоторого символа
#     :param length: int
#     :param direction: bool
#     :param symbol: str
#     :return: str
#     """
#     if direction:
#         print(length * symbol)
#     else:
#         for _ in range(length):
#             print(symbol)
#
#
# line(5, False, '*')
# line(5, True, '/')


# def prime_nums(start: int, end: int) -> int:
#     for i in range(start, end):
#         prime = True
#         for j in range(2, i // 2):
#             if i % j == 0:
#                 prime = False
#         if prime:
#             print(i)
#
#
# prime_nums(10, 100)


# НЕИМЕНОВАННЫЕ АРГУМЕНТЫ

# def function_1(a, b, *args):
#     print(a, b, args)
#
#
# function_1(1, 2, 4, 5, 6, 8)


# def summa(*args):
#     # counter = 0
#     # for i_arg in args:
#     #     counter += i_arg
#     # return counter
#
#     return sum(args)
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8))


# ИМЕНОВАННЫЕ АРГУМЕНТЫ

# def get_form(**kwargs):     # kwargs - именованные аргументы (key words args)
#     print(kwargs['name'])
#
#
# get_form(name='Ivanov', email='ivanov@mail.ru')


# def get(request, *args, **kwargs):
#     print(f'Сделан запрос на {request}')
#     print(f'Параметры запроса: {kwargs["cache_control"]}')
#     print(f'Относительный путь: {args[0]}')
#
#
# get('http://test.ru', '/page_1', cache_control='no-cache', content_type='text/html')


# def function_1(*args, **kwargs):
#     print(f'Номер группы: {kwargs["num_group"]}. Степень: {kwargs["degree"]}. '
#           f'Год выпуска: {kwargs["year"]}.')
#     counter = 1
#     for i_student in args:
#         print(counter, i_student)
#         counter += 1
#
#
# function_1('Ivanov Petr', 'Petrov Ivan', num_group='32', degree='бакалавриат', year='2025')


# def try_to_get_value(value, data):
#     try:
#         print(data[value])
#     except KeyError:
#         return
#
#
# def get_form_data(**kwargs):
#
#     try:
#         print(kwargs['email'], kwargs['phone'])
#     except KeyError:
#         print('Email и телефон обязательны для заполнения!')
#         return
#
#     try_to_get_value('name', kwargs)
#     try_to_get_value('surname', kwargs)
#
#
# get_form_data(email='nikita@gmail.com', phone='89923573936',
#               name='Nikita', surname='Merenyuk')


# АНОНИМНЫЕ ФУНКЦИИ (lambda)

# square = lambda x, y: x ** y
#
# print(square(5, 2))


# import time
#
#
# class Iterator:
#
#     def __init__(self, n):
#         self._n = n
#
#     def __iter__(self):
#         print('__iter__')
#         return
#
#     def __next__(self):
#         print('__next__')
#         time.sleep(1)
#         self.n += 1
#         print(self._n)
#
#
# for i in Iterator(0):
#     pass


# nums_list = [1, 2, 3, 4, 5, 6, 7, 8]
#
# square_nums_list = [i ** 2 for i in nums_list]
# print(square_nums_list)
#
# square_nums_list_2 = list(map(lambda x: x ** 2, nums_list))       # Изменяет список в соотв. с условиями
# print(square_nums_list_2)
#
# filtered_list = list(filter(lambda x: x > 4, nums_list))        # Убирает из списка элементы, которые не подходят под условие
# print(filtered_list)


# name_list = ['Ivan', 'Petya', 'Irina']
#
# filtered_list = list(filter(lambda x: (x[0].lower() == 'i' and len(x) <= 4), name_list))
# print(filtered_list)


# nums = [125, 14575, 35, 8, 147, 489]
#
# # filtred_list = list(filter(lambda x: len(str(x)) == 3, nums))
# # filtred_list_0 = list(filter(lambda x: 99 < x < 1000, nums))
# # filtred_list_1 = list(map(lambda x: str(x), nums))
# # filtred_list_2 = list(filter(lambda x: len(x) == 3, filtred_list_1))
# # filtred_list_3 = list(map(int, filtred_list_2))
# filtred_list_4 = list(map(int, filter(lambda x: len(x) == 3, (map(lambda x: str(x), nums)))))
#
# # print(filtred_list)
# # print(filtred_list_0)
# # print(filtred_list_2)
# # print(filtred_list_3)
# print(filtred_list_4)


# students = [
#     ['Student 1', 4.8],
#     ['Student 2', 4.7],
#     ['Student 9', 4.9],
#     ['Student 4', 4.8],
#     ['Student 10', 4.1],
#     ['Student 6', 3.8],
#     ['Student 7', 4.4],
# ]
#
# sorted_list = sorted(students, key=lambda x: x[1])
# print(sorted_list)
#
# sorted_list_2 = sorted(students, key=lambda x: int(x[0].split()[1]), reverse=True)
# print(sorted_list_2)
