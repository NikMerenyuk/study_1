# TASK 4
#
def min_num(a: int, b: int, c: int, d: int, e: int) -> int:
    """
    Возвращает минимальное из пяти чисел
    :param a: int
    :param b: int
    :param c: int
    :param d: int
    :param e: int
    :return: int
    """
    list_1 = [a, b, c, d, e]
    return min(list_1)


print(min_num(4, 8, -13, 85, 0))


# TASK 5

# def mult(start: int, end: int) -> int:
#     """
#     Возвращает произведение чисел в указанном диапазоне
#     :param start: int
#     :param end: int
#     :return: int
#     """
#     mult_num = 1
#     if start > end:
#         for i in range(start, end - 1, -1):
#             mult_num *= i
#     else:
#         for i in range(start, end + 1):
#             mult_num *= i
#
#     return mult_num
#
#
# print(mult(5, 1))


# TASK 6

# def len_num(a: int) -> int:
#     """
#     Возвращает кол-во цифр
#     :param a: int
#     :return: int
#     """
#     return len(str(a))
#
#
# print(len_num(123466666))


# TASK 7

# def palindrom(num: str) -> bool:
#     """
#     Проверяет является ли число палиндромом
#     :param num: str
#     :return: bool
#     """
#     if num == num[::-1]:
#         return True
#     else:
#         return False
#
#
# print(palindrom('123321'))
