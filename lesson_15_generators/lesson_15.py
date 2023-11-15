# Множества - неупорядоченные

# a = set()    # Создать пустое множество
# a.add('apple')    # Добавить в множество
# a.add('banana')
# print('banana' in a)

# a.remove('apple')     # Если элемента нет, то ошибка KeyError
# a.discard('apple')    # Ошибки не будет
# a.pop()    # Удаляет любой элемент (неизвестно какой)
# b = {'orange', 'watermelon', 'apple'}

# print(a.intersection(b))    # Пересечение множеств
# print(a.difference(b))    # Разница множеств
# c = a.union(b))    # Объединение множеств (создает новое множество)
# a.clear()    # Удаляет все элементы
# a.update(b)    # Обновляет сущ. множество
# print('*'.join(a))

# set_1 = {'Name', 18.6, 'key', 'value', 5}    # Могут храниться только простые типы данных (int, float, str)
# print(set_1)

# import sys
#
# list_1 = ['apple', 'orange']
# set_1 = {'apple', 'orange'}
#
# print(sys.getsizeof(list_1))
# print(sys.getsizeof(set_1))
# print(set_1.update(list_1))


# a = set()
#
# with open('text.txt', 'r') as file:
#     for i in file:
#         a.add(i)
#     print(len(i))


# data = {}
#
# with open('voyna-i-mir.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#     set_text = set(text)
#     for symbol in set_text:
#         if symbol.isalpha():
#             data.setdefault(symbol, text.count(symbol))
#     sorted_dict = sorted(data, key=lambda x: data[x], reverse=True)
#     print(data['о'])
#
# print(sorted_dict)


# Проверка, может ли строка быть палиндромом
#
# str_1 = 'aabbaabaa'
#
#
# def check(str_1):
#     data = {}
#     for i in str_1:
#         data.setdefault(i, 0)
#         data[i] += 1
#
#     count = 0
#     for j in data.values():
#         if j % 2 != 0:
#             count += 1
#
#     if count <= 1:
#         print('Может')
#     else:
#         print('Не может')
#
#
# check(str_1)


# ГЕНЕРАТОРЫ

import sys

# list_1 = [i for i in range(100)]
# generation = (i for i in range(100))    # Генераторное выражение (в данный момент времени хранит только текущий элемент)

# print(sys.getsizeof(list_1))
# print(sys.getsizeof(generation))


# def custom_range(start, end):   # Генераторная функция за счет yield
#     for i in range(start, end):
#         yield i
#
#
# for i in custom_range(10, 20):
#     print(i)


class Generator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.cur = start

    def __iter__(self):
        print('__iter__')
        return self

    def __next__(self):
        print('__next__')
        if self.cur == self.end:
            raise StopIteration
        self.cur += 1
        return self.cur


for i in Generator(10, 20):
    print(i)


# with open('random_words.txt', 'r', encoding='utf-8') as file:
#     words = (i_word for i_word in file.readlines())
#
# for i in words:
#     print(i.strip())


# def gen_func():
#     with open('random_words.txt', 'r', encoding='utf-8') as file:
#         for i_words in file.readlines():
#             yield i_words
#
#
# for i in gen_func():
#     print(i.strip())

# import time
#
#
# def inf_nums():
#     nums = 0
#
#     while True:
#         nums += 1
#         time.sleep(0.5)
#         yield nums
#
#
# for i in inf_nums():
#     print(i)


# names = ['Alina', 'Petr', 'Stanislav', 'Nikita', 'Ivan', 'Igor', 'Olga']
#
# names_a = (i.lower() for i in names if 'a' not in i)
#
# for name in names_a:
#     print(name.capitalize())


# text = 'abcdefg'
#
#
# def alone_words():
#     for word in text:
#         yield word
#
#
# for i in alone_words():
#     print(i)


# types_list = ['Привет', 13, ('qewr', 34, 'fsd'), {'key': 'value'}]
#
#
# def types():
#     for i_types in types_list:
#         if isinstance(i_types, tuple):
#             raise BaseException
#         yield type(i_types)
#
#
# for i in types():
#     print(i)



