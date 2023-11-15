# TDD - Test Driving Development


# Pattern Singleton - проверка, единственный объект в классе

# class Singleton:
#     _instance = None
#
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super(Singleton, cls).__new__(cls)
#
#         return cls._instance
#
#
# def test_singleton_identify():
#     singleton1 = Singleton()
#     singleton2 = Singleton()
#
#     assert singleton1 is singleton2, "Singleton instances are not same"
#
#
# def test_singleton_state():
#     singleton1 = Singleton()
#     singleton1.data = "Singleton data"
#     singleton2 = Singleton()
#
#     assert singleton2.data == "Singleton data", "Singleton state is not share"
#
#
# test_singleton_identify()
# test_singleton_state()


# Abstract Factory - фабрика классов;

# class AbstractFactory:
#     def create_product_a(self):
#         return


# Task 3 В гите

# class Logger:
#
#     _isinstance = None
#
#     def __new__(cls, output_type='screen'):
#         if cls._isinstance is None:
#             cls._isinstance = super(Logger, cls).__new__(cls)
#             cls._output_type = output_type
#
#         return cls._isinstance
#
#     def log(self, message):
#         if self._output_type == 'file':
#             with open('log.txt', 'a') as file:
#                 file.write(message + '\n')
#


# Strategy - поведенческий паттерн / суть изменить поведение класса


# Adapter - адаптирует класс, который мы хотим использовать


# Facade -

# Prototype - создание новых объектов, путем копирования существующих
# (deepcopy - полное копирование объекта, а не ссылку на него)
