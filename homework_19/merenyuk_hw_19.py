# TASK 3
#
class Airplane:

    def __init__(self, airplane_type, current_passangers, max_passangers):
        self.airplane_type = airplane_type
        self.current_passangers = current_passangers
        self.max_passangers = max_passangers

    def __add__(self, other):
        if isinstance(other, Airplane):
            self.current_passangers += other.current_passangers
            return self
        else:
            return 'Сложение невозможно!'

    def __sub__(self, other):
        if isinstance(other, Airplane):
            self.current_passangers -= other.current_passangers
            return self
        else:
            return 'Вычитание невозможно!'

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.airplane_type == other.airplane_type
        else:
            return 'Сравнение невозможно!'

    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passangers < other.max_passangers

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passangers > other.max_passangers

    def __le__(self, other):
        if isinstance(other, Airplane):
            return self.max_passangers <= other.max_passangers

    def __ge__(self, other):
        if isinstance(other, Airplane):
            return self.max_passangers >= other.max_passangers

    def __str__(self):
        return f'Тип: {self.airplane_type}\n' \
               f'Текущее кол-во пассажиров: {self.current_passangers}\n' \
               f'Максимальное кол-во пассажиров: {self.max_passangers}\n'


airplane_1 = Airplane('DASSAULT FALCON 900EX', 0, 12)
print(airplane_1)
airplane_1.current_passangers += 10
airplane_1.current_passangers -= 5
print(airplane_1)

airplane_2 = Airplane('AIRBUS A319', 105, 150)
print(airplane_2)
airplane_2.current_passangers += 32
airplane_2.current_passangers -= 2
print(airplane_2)

print(airplane_1 == airplane_2)
print(airplane_1 > airplane_2)
print(airplane_1 < airplane_2)
print(airplane_1 >= airplane_2)
print(airplane_1 <= airplane_2)


# TASK 4
#
# class Flat:
#
#     def __init__(self, area, price):
#         self.area = area
#         self.price = price
#
#     def __eq__(self, other):
#         if isinstance(other, Flat):
#             return self.area == other.area
#
#     def __ne__(self, other):
#         if isinstance(other, Flat):
#             return self.area != other.area
#
#     def __lt__(self, other):
#         if isinstance(other, Flat):
#             return self.price < other.price
#
#     def __gt__(self, other):
#         if isinstance(other, Flat):
#             return self.price > other.price
#
#     def __le__(self, other):
#         if isinstance(other, Flat):
#             return self.price <= other.price
#
#     def __ge__(self, other):
#         if isinstance(other, Flat):
#             return self.price >= other.price
#
#
# flat_1 = Flat(62, 90000)
# flat_2 = Flat(34, 150000)
#
# print(flat_1 == flat_2)
# print(flat_1 != flat_2)
# print(flat_1 < flat_2)
# print(flat_1 > flat_2)
# print(flat_1 <= flat_2)
# print(flat_1 >= flat_2)
