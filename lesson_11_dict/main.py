# dictionary = {'name': 'Ivan', 'age': 32}
#
# name = dictionary.get('name')
# dictionary['age'] = 33      # Установка нового значения
# dictionary['surname'] = 'Ivanov'
# dictionary.pop('age')       # Удаление ключа
# list_man = ['Ivan', 32, 'Ivanov']
# import sys
# print(sys.getsizeof(dictionary))
# print(sys.getsizeof(list_man))
# print(dictionary.keys())
# print(dictionary.values())
# print(dictionary.items())
#
# dictionary_2 = {'name': 'Petya', 'age': 35}
#
# dictionary.update(dictionary_2)     # Обновляет значения ключей и значений, если ключ/значения нет, то добавляет
#
# dictionary.setdefault('address', '')        # Если такого ключа нет, то добавит со значением, если есть, то оставит неизменным
# print(dictionary)


# Программа для добавления Страны, Города, населения, часового пояса в словарь

# dictionary = {}
#
#
# def set_country(country):
#     dictionary.setdefault(country, [])
#     print('Страна добавлена')
#
#
# def set_city():
#     key = input('Страна: ')
#     country = dictionary.get(key)
#     city_name = input('Введите название города: ')
#     if country or country == []:
#         for i_city in country:
#             if city_name in i_city.keys():
#                 print('Такой город уже есть!')
#                 return
#         population = int(input('Введите население города: '))
#         time_zone = input('Часовой пояс: ')
#         new_city = {city_name: {'population': population, 'time_zone': time_zone}}
#         dictionary[key].append(new_city)
#         print('Город добавлен!')
#     else:
#         print('Такой страны нет!')
#
#
# def get_city_info():
#     country = input('Страна: ')
#     get_country = dictionary.get(country)
#     if get_country:
#         city = input('Введите название города: ')
#         for i_city in get_country:
#             if city in i_city.keys():
#                 city_info = i_city[city]
#                 print(f'Население города: {city_info["population"]}\n'
#                       f'Часовой пояс: {city_info.get("time_zone")}')
#                 return
#             else:
#                 print('Такого города нет!')
#     else:
#         print('Такой страны нет!')
#
#
# def main():
#     while True:
#         choice = input('1 - Добавить страну\n'
#                        '2 - Добавить город\n'
#                        '3 - Получить информацию по городу -> ')
#
#         if choice == '1':
#             country = input('Введите название страны: ')
#             set_country(country)
#         elif choice == '2':
#             set_city()
#         elif choice == '3':
#             get_city_info()
#
#
# main


# Гистограмма частоты
#
# text = input('Введите текст: ')
# frequency_dict = {}
#
# for i_symbol in text:
#     if not i_symbol.isspace():
#         frequency_dict.setdefault(i_symbol, 0)
#         frequency_dict[i_symbol] += 1
#
# for key, value in frequency_dict.items():
#     print(f'{key}: {value}')


# text = input('Введите текст: ')
# frequency_dict = {}
# for i_symbol in text:
#     if not i_symbol.isspace():
#         if i_symbol in frequency_dict.keys():
#             frequency_dict[i_symbol] += 1
#         else:
#             frequency_dict[i_symbol] = 1
#
# for key, value in frequency_dict.items():
#     print(f'{key}: {value}')

# Инвертированный словарь
#
# text = input('Введите текст: ')
# frequency_dict = {}
# # 1 метод
# for i_symbol in text:
#     counter = text.count(i_symbol)
#     if counter in frequency_dict.keys():
#         if i_symbol not in frequency_dict[counter]:
#             frequency_dict[counter].append(i_symbol)
#     else:
#         frequency_dict[counter] = [i_symbol]
#
# # 2 метод
# for i_symbol in text:
#     counter = text.count(i_symbol)
#     frequency_dict.setdefault(counter, [])
#     if i_symbol not in frequency_dict[counter]:
#         frequency_dict[counter].append(i_symbol)
#
# for key, value in frequency_dict.items():
#     print(f'{key}: {value}')


# Пригодится дома!
#
# dict_1 = {
#     'key_1': {
#         'key_2': {
#             'key_3': 125,
#             'key_4': {
#                 'key_5': 'hello'
#             }
#         }
#     }
# }
#
# print(dict_1['key_1']['key_2']['key_3'])


# import re
# data = {'2023': 0, '2023/01': 100, '2022': 0, '2022/01': 150}
#
#
# def add_money() -> None:
#     date = input('(yyyy/mm)-> ')
#     if re.match(r'\d{4}/\d{2}', date):
#         money = float(input(f'Ваша прибыль за {date}: '))
#         year, month = date.split('/')
#         data.setdefault(year, 0)
#         data.setdefault(date, 0)
#         data[date] += money
#         data[year] += money
#     else:
#         print('Формат даты неверный!')
#
#
# def get_month_cost() -> None:
#     date = input('(yyyy/mm)-> ')
#     if re.match(r'\d{4}/\d{2}', date):
#         if date in data.keys():
#             print(f'Ваша прибыль за {date} составила: {data[date]}')
#         else:
#             print('Такого месяца нет!')
#     else:
#         print('Формат даты неверный!')
#
#
# def get_year_cost() -> None:
#     year = input('(yyyy) -> ')
#     if re.match(r'\d{4}', year) and year in data.keys():
#         print(f'Ваша прибыль за {year} равна {data[year]}')
#     else:
#         print('Такого года нет!')
#
#
# def main() -> None:
#     while True:
#         choice = input('1-Внести прибыль за период в формате (yyyy/mm): \n'
#                        '2-Получить прибыль за конкретный месяц (yyyy/mm): \n'
#                        '3-Получить прибыль за конкретный год (yyyy): -> ')
#         if choice == '1':
#             add_money()
#         elif choice == '2':
#             get_month_cost()
#         elif choice == '3':
#             get_year_cost()
#         else:
#             print('Такой команды нет!')
#
#
# main()


# ТЕЛЕФОННАЯ КНИГА
#
import re

contacts = {}


def add_cont() -> None:
    name = input('Введите имя: ')
    tel = input('Введите номер телефона (7хххххххххх): ')
    if re.match(r'^7\d{10}', tel):
        contacts.setdefault(tel, name)
        print('Контакт добавлен!')
    else:
        print('Неверный формат номера телефона!')


def del_cont() -> None:
    tel = input('Введите номер телефона (7хххххххххх): ')
    if re.match(r'^7\d{10}',tel):
        if tel in contacts.keys():
            contacts.pop(tel)
            print('Контакт удален!')
        else:
            print('Такого контакта нет!')
    else:
        print('Неверный формат номера телефона!')


def edit_cont():
    tel = input('Введите номер телефона (7хххххххххх): ')
    edit_choice = input('1-Редактировать номер телефона: \n'
                        '2-Редактировать имя: -> ')
    if re.match(r'^7\d{10}', tel):
        if tel in contacts.keys():
            if edit_choice == '1':
                save_name = contacts.pop(tel)
                new_tel = input('Введите новый номер телефона (7хххххххххх): ')
                if re.match(r'^7\d{10}', new_tel):
                    contacts.setdefault(new_tel, save_name)
                else:
                    print('Неверный формат номера телефона!')
            elif edit_choice == '2':
                contacts[tel] = input('Введите новое имя: ')
        else:
            print('Такого контакта нет!')


def show_cont():
    for tel,  name in contacts.items():
        print(f'Имя: {name}\n'
              f'Номер: {tel}')


def main() -> None:
    flag = True
    while flag:
        choice = input('1-Добавить контакт: \n'
                       '2-Удалить контакт: \n'
                       '3-Показать текущие контакты: \n'
                       '4-Редактировать контакты: \n'
                       '5-Закончить работу программы -> ')
        if choice == '1':
            add_cont()
        elif choice == '2':
            del_cont()
        elif choice == '3':
            show_cont()
        elif choice == '4':
            edit_cont()
        elif choice == '5':
            print('Программа закончила свою работу!')
            flag = False
        else:
            print('Такой команды нет!')


main()


# Синтаксический сахар

# def info_man(name, age):
#     print(name, age)
#
#
# data = {'name': 'Ivan', 'age': '22'}
# info_man(**data)        # Чтобы распаковать словарь **название_словаря


# def info_man_2(age, name):
#     print(name, age)
#
#
# list_info = ['Ivan', 18]
# info_man_2(*list_info)      # Чтобы распаковать список *название_списка


# Генератор словаря
#
# names_list = ['Ivan', 'Anna', 'Maria', 'Sasha']
#
# names_dict = {key: [] for key in names_list}
# names_dict_1 = {i + 1: names_list[i] for i in range(len(names_list))}
# names_dict_2 = {i: [j for j in i] for i in names_list}
# print(names_dict)
# print(names_dict_1)
# print(names_dict_2)
