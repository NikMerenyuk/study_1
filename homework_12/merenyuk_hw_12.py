# TASK 3
# Петров Петр Петрович, petrov@gmail.com, junior python developer, 4, petrovpp
import re
firm = {'71111111111': ['Ivanov Ivan Ivanovich', 'ivanov@gmail.com', 'engineer', '3', 'ivanovii']}


def add_data() -> None:
    tel = input('Введите номер телефона сотрудника (7хххххххххх): ')
    if re.match(r'^7\d{10}$', tel):
        if tel in firm.keys():
            print('Сотрудник с таким номером телефона уже есть.\n')
        else:
            person = input('Введите данные сотрудника через запятую (ФИО, рабочий email, '
                           'название должности, номер кабинета, skype): ').split(', ')
            firm.setdefault(tel, person)
            print('Данные сотрудника добавлены.\n')
    else:
        print('Неверный формат номера телефона.\n')


def del_data() -> None:
    tel = input('Введите номер телефона сотрудника (7хххххххххх): ')
    if re.match(r'^7\d{10}$', tel):
        if tel in firm.keys():
            firm.pop(tel)
            print('Данные сотрудника удалены.\n')
        else:
            print('Сотрудника с таким номером телефона нет.\n')
    else:
        print('Неверный формат номера телефона.\n')


def search_data() -> None:
    tel = input('Введите номер телефона сотрудника (7хххххххххх): ')
    if re.match(r'^7\d{10}$', tel):
        if tel in firm.keys():
            print(f'ФИО: {firm[tel][0]}\n'
                  f'Рабочий email: {firm[tel][1]}\n'
                  f'Название должности: {firm[tel][2]}\n'
                  f'Номер кабинета: {firm[tel][3]}\n'
                  f'Skype: {firm[tel][4]}\n')
        else:
            print('Сотрудника с таким номером телефона нет.\n')
    else:
        print('Неверный формат номера телефона.\n')


def edit_data() -> None:
    tel = input('Введите номер телефона сотрудника (7хххххххххх): ')
    if re.match(r'^7\d{10}$', tel):
        if tel in firm.keys():
            edit_choice = input('Отредактировать:\n'
                                '1-Номер телефона\n'
                                '2-ФИО\n'
                                '3-Рабочий email\n'
                                '4-Название должности\n'
                                '5-Номер кабинета\n'
                                '6-Skype\n'
                                '0-Назад -> ')
            if edit_choice == '1':
                new_tel = input('Введите новый номер телефона (7xxxxxxxxxx): ')
                if re.match(r'^7\d{10}$', new_tel):
                    if new_tel in firm.keys():
                        print('Сотрудник с таким номером телефона уже есть.\n')
                    else:
                        s_value = firm.pop(tel)
                        firm.setdefault(new_tel, s_value)
                        print('Номер телефона сотрудника изменен.\n')
                else:
                    print('Неверный формат номера телефона.\n')
            elif edit_choice == '2':
                new_full_name = input('Введите новые ФИО: ')
                firm[tel][0] = new_full_name
                print('ФИО сотрудника изменены.\n')
            elif edit_choice == '3':
                new_email = input('Введите новый email: ')
                firm[tel][1] = new_email
                print('Email сотрудника изменен.\n')
            elif edit_choice == '4':
                new_post = input('Введите новую должность: ')
                firm[tel][2] = new_post
                print('Должность сотрудника изменена.\n')
            elif edit_choice == '5':
                new_cab_num = input('Введите новый номер кабинета: ')
                firm[tel][3] = new_cab_num
                print('Номер кабинета сотрудника изменен.\n')
            elif edit_choice == '6':
                new_skype = input('Введите новый skype: ')
                firm[tel][2] = new_skype
                print('Skype сотрудника измен.\n')
            elif edit_choice == '0':
                print()
                return
        else:
            print('Сотрудника с таким номером телефона нет.\n')
    else:
        print('Неверный формат номера телефона.\n')


def main() -> None:
    while True:
        choice = input('1-Добавление данных сотрудника\n'
                       '2-Удаление данных сотрудника\n'
                       '3-Поиск данных сотрудника\n'
                       '4-Редактирование данных сотрудника\n'
                       '0-Закончить работу программы -> ')
        print()
        if choice == '1':
            add_data()
        elif choice == '2':
            del_data()
        elif choice == '3':
            search_data()
        elif choice == '4':
            edit_data()
        elif choice == '0':
            print('Программа закончила свою работу')
            return


main()
