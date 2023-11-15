# r - чтение
# w - запись (перезаписывает сущ.)
# a - дозапись
# r+ - чтение + запись

# file = open('filename.txt', 'r')  # открытие файла
#
# # file.write('Ok')
# # text = file.read()
# # print(text)
# # file.write(f'Привет, я файл!\n')
# # file.write(f'Привет, я файл!\n')
# # for _ in range(5):
# #     file.write(f'Привет, я файл!\n')
# try:
#     text = file.readlines()
#     raise ValueError
#     print(text)
# except ValueError:
#     print('Поймали ошибку!')
# finally:
#     file.close()  # закрытие файла
#     print('Файл закрыт')


# filename_bin = open('file.bin', 'rb')
#
# # filename_bin.write(bytes('Какой-то текст'.encode()))
# print(filename_bin.read().decode())
#
# filename_bin.close()


# КОНТЕКСТНЫЙ МЕНЕДЖЕР (сам закроет файл)

# with open('filename.txt', 'r') as file:
#     print(file.read())


# class CustomFile:
#     def __init__(self, file_name, mode):
#         self.file_name = file_name
#         self.mode = mode
#
#     def __enter__(self):
#         print('Сработал метод __enter__')
#         self.file = open(self.file_name, self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('Сработал метод __exit__')
#         self.file.close()
#         print('Файл закрыт')
#
#
# with CustomFile('filename.txt', 'r') as file:
#     raise ValueError

# import random
#
# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#
#
# def caesar_code(text, shift) -> str:
#     decrypted_list = [(alphabet[(alphabet.index(sym) + shift) % 33]
#                        if sym != ' ' else ' ') for sym in text.lower()]
#     return ''.join(decrypted_list)
#
#
# with open('text.txt', 'w', encoding='utf-8') as file_1:
#     for i in range(5):
#         file_1.write('Привет\n')
#
#
# with open('cipher_text.txt', 'w', encoding='utf-8') as file_2:
#     with open('text.txt', 'r', encoding='utf-8') as file_1:
#         lines = file_1.readlines()
#         shift = random.randint(1, 33)
#         for i_line in lines:
#             ciphered = caesar_code(i_line.strip(), shift)
#             file_2.write(ciphered.capitalize()[:len(ciphered) // 2] + f'({shift})'
#                          + ciphered[len(ciphered) // 2:] + '\n')
#             shift = random.randint(1, 33)


# with open('zen.txt', 'r') as file:
#     text = file.read().lower()
#     # for sym in text:
#     #     if sym.isalpha():
#     #         frequency.setdefault(sym, text.count(sym))
#     frequency = {sym: text.count(sym) for sym in text if sym.isalpha()}
#     # print(frequency)
#
#     alpha_num = len(frequency.keys())
#     total_num = sum(frequency.values())
#     min_alpha = min(frequency.values())
#     file.seek(0)  # Перемещает курсор на символ 0 - в начало
#     lines_num = len(file.readlines())
#     words_num = len(text.split())
#     print(alpha_num, total_num, min_alpha, lines_num, words_num)


# with open('zen.txt', 'r+') as file:
#     lines = file.readlines()
#     file.write(''.join(lines[::-1]))


# with open('bad_words.txt', 'r') as file:
#     with open('text.txt', 'r') as file_2:
#         text = file_2.read()
#         for bad in file.readlines():
#             if bad.strip() in text:
#                 text = text.replace(bad, '')
#     with open('text.txt', 'w') as file_2:
#         file_2.write(text)

import re
with open('text.txt', 'r', encoding='utf-8') as file:
    count = 0
    text = file.read()
    for i in text:
        if re.match(r'\d', i):
            count += 1
    print(count)
