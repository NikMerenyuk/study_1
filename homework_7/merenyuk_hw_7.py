list_1 = [3, -31, 50, 29, 0, -64, 51, 30, 68, -76, 52, 0, 48]
list_2 = [0, 87, 90, -13, 48, -7, 0, 36, -75, 6, 0, 88, -38]
list_3 = [i for i in list_1 + list_2]
list_4 = [i for i in list_1 + list_2 if not i in list_1 or not i in list_2]
list_5 = [i for i in list_1 + list_2 if i in list_1 and i in list_2]
list_6 = [i for i in list_1 + list_2 if not i in list_1 or not i in list_2]  # unique
list_7 = []  # min max каждого из списков

print(f'Элементы обоих списков: {list_3}')
print(f'Элементы обоих списков без повторений: {list_4}')
print(f'Элементы содержащиеся в обоих списках: {list_5}')
print(f'Уникальные элементы: {list_6}')
print(f'Минимальное число первого списка: {min(list_1)}\n'
      f'Максимальное число первого списка: {max(list_1)}\n'
      f'Минимальное число второго списка: {min(list_2)}\n'
      f'Максимальное число второго списка: {max(list_2)}')
