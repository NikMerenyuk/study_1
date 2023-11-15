# TASK 1
#
# start = int(input('Введите начало диапазона: '))
# end = int(input('Введите конец диапазона: '))
#
# gen_expr = (i ** 2 for i in range(start, end + 1))
#
# print(*gen_expr)


# TASK 2
#
def simple_gen(start, end):
    for i_nums in range(start, end):
        simple = True
        for j in range(2, i_nums // 2):
            if i_nums % j == 0:
                simple = False
        if simple:
            yield i_nums


for i in simple_gen(1, 25):
    print(i)


# TASK 3
#
# class Even_nums:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         self.ev = start - 1
#
#     def __iter__(self):
#         print('__iter__')
#         return self
#
#     def __next__(self):
#         print('__next__')
#         if self.ev == self.end:
#             raise StopIteration
#         self.ev += 1
#         if self.ev % 2 == 0:
#             return self.ev
#         else:
#             return
#
#
# for i in Even_nums(10, 20):
#     print(i)
