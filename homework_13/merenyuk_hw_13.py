# TASK 1
#
tuple_1 = (1, 5, 35, 578, 62, 55, 22, 165, 85, 99)
tuple_2 = (93, 26, 75, 20, 5, 55, 61, 165)
tuple_3 = (82, 52, 60, 5, 96, 55, 89, 165, 995, 423, 54, 29)
print(tuple(i for i in tuple_1 + tuple_2 + tuple_3 if i in tuple_1 and i in tuple_2 and i in tuple_3))
print(tuple(i for i in tuple_1 + tuple_2 + tuple_3 if i not in tuple_1 or i not in tuple_2 or i not in tuple_3))
print(tuple(tuple_1[i] for i in range(min((len(tuple_1), len(tuple_2), len(tuple_3))))
            if tuple_1[i] == tuple_2[i] == tuple_3[i]))
