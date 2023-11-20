import json


def input_data():
    data_input = str(input('\nEnter the country and capital separated by a space: '))
    country, capital = data_input.split(' ')
    return country, capital


def db_list_in_file():
    with open('db.json', 'r') as file:
        data_list = json.loads(file.read())
    return data_list


def check_data(data):
    country, capital = data[0], data[1]
    for i_data in db_list_in_file():
        if country in i_data.keys() and capital in i_data.values():
            return True


def add_data(data):
    country, capital = data[0], data[1]
    data_dictionary = {country: capital}
    add_data_to_file(data_dictionary)


def add_data_to_file(data_dict):
    with open('db.json', 'r') as file:
        data_list = json.loads(file.read())
        data_list.append(data_dict)

    with open('db.json', 'w') as file:
        file.write(json.dumps(data_list, indent=4))


def del_data(data):
    db_list = db_list_in_file()
    counter = 0
    country, capital = data[0], data[1]
    for i_data in db_list:
        if country in i_data.keys() and capital in i_data.values():
            del db_list[counter]
            with open('db.json', 'w', encoding='utf8') as file:
                file.write(json.dumps(db_list, indent=4))
            return True
        else:
            counter += 1
    else:
        return False


def search_data(data):
    if check_data(data):
        pass


def edit_data(data):
    db_list = db_list_in_file()
    country, capital = data[0], data[1]
    for i_data in db_list:
        if country in i_data.keys() and capital in i_data.values():
            with open('db.json', 'w', encoding='utf8') as file:
                file.write(json.dumps(db_list, indent=4))
            return True
    else:
        return False


def edit_country(data):
    db_list = db_list_in_file()
    country, capital = data[0], data[1]
    for i_data in db_list:
        if country in i_data.keys() and capital in i_data.values():
            with open('db.json', 'w', encoding='utf8') as file:
                file.write(json.dumps(db_list, indent=4))
            return True
    else:
        return False


def menu():
    flag = True
    while flag:
        try:
            choice = int(input("\n1-Add data.\n"
                               "2-Remove data.\n"
                               "3-Search data.\n"
                               "4-Edit data.\n"
                               "5-Save data.\n"
                               "6-Load data.\n"
                               "0-Exit from program. -> "))
            if choice == 1:
                add_data(input_data())
                print('Item added.')
            elif choice == 2:
                if del_data(input_data()):
                    print('Item removed.')
                else:
                    print('The item is not in db.')
            elif choice == 3:
                if check_data(input_data()):
                    print('The item is in db.')
                else:
                    print('The item is not in db.')
            elif choice == 4:
                if search_data(input_data()):
                    print('Item changed.')
                else:
                    print('The item is not in db.')
            elif choice == 0:
                print('\nThe program has finished work.')
                flag = False
            else:
                print('\nInvalid input. Try again.')

        except ValueError:
            print('\nInvalid input.Try again.')


if __name__ == '__main__':
    menu()
