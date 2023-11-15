import random
from typing import Callable, List

# TASK 1
#
# exception = [BaseException, ArithmeticError, EnvironmentError, RuntimeError,
#              LookupError, SyntaxError, IndexError, KeyError, ZeroDivisionError]
# chance = random.randint(1, 10)
#
#
# def random_exception(func: Callable) -> Callable:
#     def wrapper(*args, **kwargs):
#         if chance == 2:
#             raise random.choice(exception)('Увы')
#         func(*args, **kwargs)
#     return wrapper
#
#
# @random_exception
# def division(a, b):
#     return a / b
#
#
# division(5, 2)


# TASK 2
#
# c_1 = (1, 2, 3, 4, 5)
# c_2 = [1, '2', 3, 4, 'fds']
# c_3 = {'asdf': 'asdfg'}
# c_4 = 1
# c_5 = 1.5
# c_6 = 'Привет'
#
#
# def check_type(func: Callable) -> Callable:
#     def wrapper():
#         print(f'Тип возвращенных данных: {type(func())}')
#     return wrapper
#
#
# @check_type
# def data_type():
#     return c_3
#
#
# data_type()
