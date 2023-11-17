# TASK 1
#
import json


def add_data():
    data_input = str(input("\nВведите название страны и столицы через пробел: "))
    country, capital = data_input.split(" ")
    dict_data = {country: capital}
    add_new_data_to_file(dict_data)


def add_new_data_to_file(data):
    with open("db.json", "r", encoding="utf8") as file:
        data_list = json.loads(file.read())
        data_list.append(data)
    with open("db.json", "w") as file:
        file.write(json.dumps(data_list, indent=4))


def edit_defs(choice):
    with open("db.json", "r", encoding="utf8") as file:
        dict_ = json.loads(file.read())
        del_data_input = str(input("\nВведите название страны и столицы через пробел: "))
        country, capital = del_data_input.split(" ")

        match choice:
            case "del_data":
                count = 0
                for i_data in dict_:
                    if country in i_data.keys() and capital in i_data.values():
                        del dict_[count]
                        with open("db.json", "w", encoding="utf8") as file:
                            json.dump(dict_, file, indent=4)
                        return True
                    else:
                        count += 1
                else:
                    return False

            case "search_data":
                for i_data in dict_:
                    if country in i_data.keys() and capital in i_data.values():
                        print(f"Страна: {country} и столица: {capital} есть в базе.")
                        return
                else:
                    print(f"Страны: {country} и столицы: {capital} нет в базе.")
                    return

            case "edit_data":
                for i_data in dict_:
                    if country in i_data.keys() and capital in i_data.values():
                        edit_choice = int(input("\n1-Изменить страну.\n"
                                                "2-Изменить столицу. -> "))
                        match edit_choice:
                            case 1:
                                new_country = str(input("Введите новое название страны: "))
                                old_value = i_data.pop(country)
                                dict_.setdefault(new_country, old_value)
                                return
                            case 2:
                                new_capital = str(input("Введите новое название столицы: "))
                                i_data[capital] = new_capital
                                return
                            case _:
                                print('Неверный формат ввода.')
                else:
                    print(f"Страны: {country} и столицы: {capital} нет в базе.")
                    return



def serialization():
    pass


def deserialization():
    pass


def menu():
    flag = True
    while flag:
        choice = int(input(
                "\n1-Добавление данных.\n"
                "2-Удаление данных.\n"
                "3-Поиск данных.\n"
                "4-Редактирование данных.\n"
                "5-Сохранение данных.\n"
                "6-Загрузка данных.\n"
                "0-Выход из программы. -> "))

        match choice:
            case 1:
                add_data()
                print("\nДанные добавлены.")
            case 2:
                if edit_defs("del_data") is True:
                    print("Данные удалены.")
                else:
                    print("Таких значений нет в базе.")

            case 3:
                edit_defs("search_data")
            case 4:
                edit_defs("edit_data")
            case 5:
                serialization()
            case 6:
                deserialization()
            case 0:
                print("\nПрограмма закончила свою работу.")
                flag = False
            case _:
                print("\nНеверный формат ввода")


if __name__ == "__main__":
    menu()
