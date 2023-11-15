# TASK 1
#
def multiply(*args: int) -> int:
    """
    Возвращает произведение аргументов
    :param args: int
    :return: int
    """
    count = 1
    for i in args:
        count *= i
    return count


print(multiply(2, 3, 4, 5, 6, 7, 8))


# TASK 2
#
# def minimum(*args: int) -> int:
#     """
#     Находит минимальный элемент из аргументов
#     :param args: int
#     :return: int
#     """
#     return min(args)
#
#
# print(minimum(4, 0, 59, 41, -32, -13, 86, 62, 54))


# TASK 3
#
# def prime_nums(*args: int) -> int:
#     counter = 0
#
#     for i in args:
#         prime = True
#         for j in range(2, i // 2):
#             if i % j == 0:
#                 prime = False
#         if prime:
#             counter += 1
#
#     return counter
#
#
# print(prime_nums(2, 3, 5, 7, 85, 234, 99, 34))


# TASK 4
#
# from typing import List
#
#
# def del_nums(nums: List[int]) -> int:
#     """
#     Удаляет из списка целых некоторое заданное число и возвращает кол-во удаленных элементов (сколько раз удалил число из спискаа)
#     :param nums: list
#     :return: int
#     """
#     counter = 0
#     for _ in nums:
#         if _ == 4:
#             nums.remove(4)
#             counter += 1
#
#     return counter
#
#
# print(del_nums([5, 4, 0, 4, 2, 4, 95]))


# TASK 5
#
# def merge(list_1: list, list_2: list) -> list:
#     """
#     Объединяет списки
#     :param list_1: list
#     :param list_3: list
#     :return: list
#     """
#     return [i for i in list_1 + list_2]
#
#
# print(merge([5, '12fs', 95, 'fsdwr'], ['sfwer', '2qwf', 'fsftqgfj', 2345]))


# TASK 6
#
# def degree_list(list_1: list, degree: int) -> list:
#     """
#     Высчитывает степень каждого элемента в списке и возвращает измененный список
#     :param list_1: list
#     :param degree: int
#     :return: list
#     """
#     exp = []
#     for i in list_1:
#         sq = degree ** i
#         exp.append(sq)
#
#     return exp
#
#
# print(degree_list([1, 2, 3, 4, 5], 2))
