# Класс называется всегда с большой буквы

import time
import random
from typing import List


# class Vehicle:
#
#     def __init__(self, name: str, weight: float, hp: int, max_speed: int):    # Метод инициализации класса (конструктор)
#         self.name = name
#         self.weight = weight
#         self.hp = hp
#         self.max_speed = max_speed
#         self.wheel_count = 4    # Константный параметр, который будет назначен всем объектам
#         self.__wheel_count = 4    # __ - категорически нельзя изменять значение (locker), _ - нежелательно изменять
#                                   # но доступ внутри класса имеется
#         self.const_litres = 50
#         self.__possible_failures = ['Дерево', 'Столб', 'Обрыв']
#
#     # def output_info(self):                                   # Метод класса
#     #     print(f'Информация о машине: \n'
#     #           f'Название: {self.name}\n'
#     #           f'Масса: {self.weight}\n'
#     #           f'Hp: {self.hp}')
#
#     # @staticmethod
#     # def refuel(litres: float):                            # Статичный метод, который не использует атрибуты self.
#     #     print(f'Машина заправлена на {litres} литров')
#
#     def refuel(self, litres: float):
#         self.const_litres += litres
#         print(f'Изначальное количество бензина: {self.const_litres} литров\n'
#               f'Заправили на {litres} литров\n'
#               f'Сейчас {self.const_litres} литров')
#
#     def drive(self, km: float):
#         self.const_litres -= (km // 10)
#         if self.const_litres <= 0:
#             print(f'Машина дальше не поедет! Кончилось топливо.')
#         else:
#             print(f'В машине осталось {self.const_litres} литров')
#
#     def acceleration(self):
#         cur_time = 0
#         for i in range(0, self.max_speed, 20):
#             if random.randint(1, 10) == 5:
#                 print(f'Вы встретили препятствие {random.choice(self.__possible_failures)} при разгоне')
#                 return
#             cur_time += 0.5
#             time.sleep(0.5)
#             print(f'Текущая скорость: {i} км/ч')
#         print(f'Машина {self.name} достигла максимальной скорости за {cur_time}')
#
#     def __str__(self):                                         # Выводит в консоль только строку
#         return (f'Информация о машине: \n'
#                 f'Название: {self.name}\n'
#                 f'Масса: {self.weight}\n'
#                 f'Hp: {self.hp}\n'
#                 f'Wheel count: {self.__wheel_count}')

    # Обычные методы нужно вызывать, а магические срабатывают при взаимодействии с объектом


# vehicle_1 = Vehicle('audi', 2000, 500, 180)                      # Экземпляр/объект
# # print(vehicle_1.output_info())
# print(vehicle_1)

# vehicle_2 = Vehicle(name='bmw', weight=1800.2, hp=620, max_speed = 200)    # Экземпляр/объект
# print(vehicle_2)

# vehicle_1.max_speed_1 = 100
# print(vehicle_1.max_speed_1)                                # Можно назначать новые атрибуты вне класса
# print(vehicle_2.max_speed_1)                                # Не будет распространяться на другие объекты
# print(vehicle_1.wheel_count)

# vehicle_1.refuel(25.55)
# print(vehicle_1.const_litres)

# vehicle_1.drive(2500)
# print(vehicle_1.const_litres)

# vehicle_1.acceleration()


# class Human:
#
#     def __init__(self, full_name: str, birth_date: str, tel: str, city: str, country: str):
#         self.full_name = full_name
#         self.birth_date = birth_date
#         self.tel = tel
#         self.city = city
#         self.country = country
#
#     def set_full_name(self, value):
#         self.full_name = value
#
#     def get_full_name(self):
#         return self.full_name
#
#
# human = Human(full_name='Ivan', birth_date='11.04.2006', tel='+79999999999', city='Ekb', country='Russia')
# print(human.get_full_name())
# human.set_full_name('Petr')
# print(human.get_full_name())


# class Students:
#
#     def __init__(self, full_name: str, group_num: str, mark_list: List[int]):
#         self.full_name = full_name
#         self.group_num = group_num
#         self.mark_list = mark_list
#
#     def get_avg_mark(self) -> float:
#         return sum(self.mark_list) / len(self.mark_list)
#
#     def __str__(self):
#         return f'{self.full_name} {self.group_num} {self.get_avg_mark()}'
#
#
# students = [
#     Students('Ivan', 'P-1', [random.randint(1, 5) for _ in range(5)]),
#     Students('Petr', 'P-2', [random.randint(1, 5) for _ in range(5)]),
#     Students('Vasya', 'P-3', [random.randint(1, 5) for _ in range(5)]),
#     Students('Lena', 'P-2', [random.randint(1, 5) for _ in range(5)]),
#     Students('Katya', 'P-4', [random.randint(1, 5) for _ in range(5)]),
#     Students('Nikita', 'P-3', [random.randint(1, 5) for _ in range(5)]),
#     Students('Kamil', 'P-1', [random.randint(1, 5) for _ in range(5)]),
#     Students('Sema', 'P-2', [random.randint(1, 5) for _ in range(5)]),
#     Students('Sasha', 'P-4', [random.randint(1, 5) for _ in range(5)]),
#     Students('Kostya', 'P-4', [random.randint(1, 5) for _ in range(5)])
# ]
#
# # sorted_students = sorted(students, key=lambda x: x.full_name[0])
# sorted_students = sorted(students, key=lambda x: x.get_avg_mark())
#
# for i_student in sorted_students:
#     print(i_student)


# class Point:
#
#     MIN_COORD = 0
#     MAX_COORD = 100    # Константы
#
#     def __init__(self, x, y):
#         self.set_coordinates(x, y)
#
#     @classmethod
#     def set_square(cls, left, right):
#         cls.MIN_COORD = left
#         cls.MAX_COORD = right
#
#     def set_coordinates(self, x, y):
#         if Point.MIN_COORD <= x <= Point.MAX_COORD and Point.MIN_COORD <= y <= Point.MAX_COORD:
#             self.x = x
#             self.y = y
#         else:
#             print('Точка лежит вне области')
#
#     def __setattr__(self, key, value):    # Срабатывает когда присваивают значения
#         print('Сработал __setatr__')
#         if key == 'w':
#             raise ValueError('Недоустимые значения атрибута')
#         object.__setattr__(self, key, value)
#
#     def __getattribute__(self, item):    # Срабатывает при получении атрибута
#         print('Сработал  методом __getattribute__')
#         if item == 'x':
#             raise ValueError('У вас нет доступа к значению этого атрибута!')
#         return object.__getattribute__(self, item)
#
#     def __str__(self):
#         return f'Координаты точки: x={self.x}, y={self.y}'
#
#
# point = Point(1, 2)
# print(point.x)
