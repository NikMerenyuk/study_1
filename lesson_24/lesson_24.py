# Конкурентность - борьба за ресурсы
# операционная система решает очередность
# Долгие операции: ввод/вывод, запись

# import threading
#
#
# nums_list = []
#
# while True:
#     user_input = input('Enter some numbers (press "q" to exit): ')
#     if user_input == 'q':
#         break
#     try:
#         nums_list.append(int(user_input))
#     except ValueError:
#         print('Invalid input. Try again.')
#
#
# def list_sum(arr):
#     if arr:
#         print(sum(arr))
#     else:
#         print('List is empty.')
#
#
# def arith_mean(arr):
#     if arr:
#         print(sum(arr) // len(arr))
#     else:
#         print('List is empty.')
#
#
# if __name__ == '__main__':
#     sum_threading = threading.Thread(target=list_sum, args=(nums_list, ))
#     arith_mean_threading = threading.Thread(target=arith_mean, args=(nums_list, ))
#
#     sum_threading.start()
#     arith_mean_threading.start()
#
#     sum_threading.join()
#     arith_mean_threading.join()
