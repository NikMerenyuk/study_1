from typing import Callable, List
import time
import functools


# def timer(func: Callable, *args, **kwargs):     # Функция высшего порядка
#     print('Запускается таймер')
#     start = time.time()
#     res = func(*args, **kwargs)
#     print(f'Функция {func.__name__} выполнялась {time.time() - start}')
#     return res
#
#
# def squares_num(num):
#     nums = [i ** 2 for i in range(num)]
#     return nums
#
#
# def cubes_num():
#     nums = [i ** 3 for i in range(1000000)]
#     return nums
#
#
# res = timer(squares_num, 1000000)
# res = timer(cubes_num)


# def timer(func: Callable) -> Callable:
#     def wrapper(*args, **kwargs):      # Функция обертка
#         start = time.time()     # код для дополнения функционала
#         func(*args, **kwargs)      # Вызов переданной функции
#         print(f'Функция {func.__name__} {func.__doc__} выполнилась за {time.time() - start}')      # код для дополнения функционала
#     return wrapper      # Возвращаем функцию обертку как объект
#
#
# @timer
# def squares_num(num):
#     """
#     Квадраты чисел
#     :param num:
#     :return:
#     """
#     nums = [i ** 2 for i in range(num)]
#     return nums
#
#
# @timer
# def cubes_num():
#     nums = [i ** 3 for i in range(1000000)]
#     return nums
#
#
# squares_num(1000000)
# cubes_num()


# def get_or_post(method):
#     def wrapper_func(func):
#         def wrapper():
#             res = func()
#             print(f'Запрос с  методом {method} на ресурс {res} выполнен')
#         return wrapper
#     return wrapper_func
#
#
# @get_or_post('POST')
# def request():
#     url = 'http://test.com'
#     params = 'ru'
#     request_body = {}
#     return url, params, request_body
#
#
# request()


# def beauty_output(func: Callable) -> Callable:
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         for i in result:
#             print(f'|{i}|')
#     return wrapper
#
#
# @beauty_output
# def name_output(names):
#     return names
#
#
# name_output(['Nikita', 'Ivan', 'Maria'])


# import datetime
#
#
# def logging(func: Callable) -> Callable:
#     def wrapper(*args, **kwargs):
#         try:
#             func(*args, **kwargs)
#             print(f'{func.__name__} {func.__doc__}')
#         except BaseException as error:
#             with open('function_error.log', 'a') as file:
#                 file.write(f'{func.__name__} | {datetime.datetime.now()} | {error.__doc__}\n')
#
#     return wrapper
#
#
# @logging
# def concatenate(a, b):
#     return a + b
#
#
# @logging
# def division(a, b):
#     return a / b
#
#
# concatenate(1, '2')
# division(5, 0)

# def nums(a):
#     def double_func(func: Callable) -> Callable:
#         def wrapper(*args, **kwargs):
#             for _ in range(a):
#                 print(func(*args, **kwargs))
#         return wrapper
#     return double_func
#
#
# @nums(5)
# def division(a, b):
#     return a / b
#
#
# division(5, 2)


# def sleeping(func: Callable) -> Callable:
#     def wrapper(*args, **kwargs):
#         time.sleep(3)
#         func(*args, **kwargs)
#         print(f'Функция {func.__name__} выполнилась с задержкой 3 сек.')
#     return wrapper
#
#
# @sleeping
# def summ(a, b):
#     return a + b
#
#
# summ(2, 5)


# def check_age(func: Callable) -> Callable:
#     def wrapper():
#         age_input = int(input('Введите возраст: '))
#         if age_input >= 18:
#             func()
#         else:
#             print('Вам еще рано сюда!')
#     return wrapper
#
#
# @check_age
# def how_old_are_u():
#     print('Доступ открыт!')
#
#
# how_old_are_u()


# reg = {}
#
#
# def reg_def(func: Callable) -> Callable:
#     def wrapper(*args, **kwargs):
#         reg.setdefault(func.__name__, func.__doc__)
#     return wrapper
#
#
# @reg_def
# def division(a: int, b: int) -> float:
#     """
#     Делит числа
#     :param a: int
#     :param b: int
#     :return: float
#     """
#     return a / b
#
#
# @reg_def
# def multiply(a: int, b: int) -> int:
#     """
#     Умножает числа
#     :param a: int
#     :param b: int
#     :return: int
#     """
#     return a * b
#
#
# division(5, 2)
# multiply(3, 3)
# print(reg)


# def simple_nums(func: Callable) -> Callable:
#     def wrapper():
#         with open('simple_nums.txt', 'a') as file:
#             for i in func():
#                 simple = True
#                 for j in range(2, i):
#                     if i % j == 0:
#                         simple = False
#                 if simple:
#                     file.write(f'{str(i)}\n')
#
#     return wrappers
#
#
# @simple_nums
# def nums() -> List[int]:
#     # list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#     return list(i for i in range(25))
#     # return list_1
#
#
# print(nums())
