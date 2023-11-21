import json


def input_data():
    data_input = str(input('\nEnter the country and capital separated by a space: '))
    country, capital = data_input.split(' ')
    return country, capital


def add_new_data_in_file(data):
    with open('db.json', 'r') as file:
        db_data_dict = json.loads(file.read())
        country, capital = data[0], data[1]
        if country in db_data_dict.keys() and capital in db_data_dict.values():
            print('This country and capital is alreadt in the db.')
            return
        elif country in db_data_dict.keys():
            print('This country is already in the db.')
            return
        elif capital in db_data_dict.values():
            print('This capital is already in the db.')
            return
        else:
            db_data_dict.setdefault(country, capital)
            print('Item added.')
    with open('db.json', 'w') as file:
        file.write(json.dumps(db_data_dict, indent=4))


def db_list_in_file():
    with open('db.json', 'r') as file:
        db_data_dict = json.loads(file.read())
    return db_data_dict


def check_data(data):
    db_data_dict = db_list_in_file()
    country, capital = data[0], data[1]
    for _ in db_data_dict:
        if country in db_data_dict.keys() and capital in db_data_dict.values():
            return True
    else:
        return False


def remove_data(data):
    db_data_dict = db_list_in_file()
    country, capital = data[0], data[1]
    if check_data(data):
        db_data_dict.pop(country)
        with open('db.json', 'w', encoding='utf8') as file:
            file.write(json.dumps(db_data_dict, indent=4))
        return True
    else:
        return False


def search_data(data):
    country, capital = data[0], data[1]
    if check_data(data):
        return f'Item: {country}:{capital} has in the db'
    else:
        return f'Item: {country}:{capital} hasn\'t in the db'


def edit_country(data):
    db_data_dict = db_list_in_file()
    country, capital = data[0], data[1]
    if check_data(data):
        input_new_country = str(input('Enter new country: '))
        if input_new_country in db_data_dict.keys():
            print('This country is already in the db.')
            return
        capital_of_old_country = db_data_dict.pop(country)
        db_data_dict.setdefault(input_new_country, capital_of_old_country)
        with open('db.json', 'w', encoding='utf8') as file:
            file.write(json.dumps(db_data_dict, indent=4))
        return 'Country changed.'
    else:
        return 'The item is not in db.'


def edit_capital(data):
    db_data_dict = db_list_in_file()
    country, capital = data[0], data[1]
    if check_data(data):
        input_new_capital = str(input('Enter new capital: '))
        if input_new_capital in db_data_dict.values():
            print('This capital is already in the db.')
            return
        db_data_dict[country] = input_new_capital
        with open('db.json', 'w', encoding='utf8') as file:
            file.write(json.dumps(db_data_dict, indent=4))
        return 'Capital changed.'
    else:
        return 'The item is not in db.'


def save_db():
    with open('db.json', 'r') as db_file:
        with open('saved_db.json', 'w') as saved_db:
            lines = db_file.readlines()
            for i_lines in lines:
                saved_db.write(i_lines)
            return


def load_db():
    with open('saved_db.json', 'r') as saved_db:
        with open('db.json', 'w') as db:
            lines = saved_db.readlines()
            for i_lines in lines:
                db.write(i_lines)
            return


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
                add_new_data_in_file(input_data())

            elif choice == 2:
                if remove_data(input_data()):
                    print('Item removed.')
                else:
                    print('The item is not in db.')

            elif choice == 3:
                print(search_data(input_data()))

            elif choice == 4:
                edit_choice = int(input('\n1-Edit country.\n'
                                        '2-Edit capital.\n'
                                        '0-Back. -> '))
                if edit_choice == 1:
                    edit_country(input_data())
                elif edit_choice == 2:
                    edit_capital(input_data())
                elif edit_choice == 0:
                    continue
                else:
                    print('Invalid input. Try again.')

            elif choice == 5:
                save_db()
                print('db been saved.')

            elif choice == 6:
                load_db()
                print('db been loaded')

            elif choice == 0:
                print('\nThe program has finished work.')
                flag = False
            else:
                print('\nInvalid input. Try again.')

        except ValueError:
            print('\nInvalid input.Try again.')


if __name__ == '__main__':
    menu()
