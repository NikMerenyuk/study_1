import json


def input_data():
    data_input = str(input('Enter the country and capital separated by a space: '))
    country, capital = data_input.split(' ')
    return country, capital


def add_data(data):
    country, capital = data[0], data[1]
    data_dictionary = {country: capital}
    add_data_to_file(data_dictionary)


def add_data_to_file(data):
    with open('db.json', 'r') as file:
        data_list = json.loads(file.read())
        data_list.append(data)

    with open('db.json', 'w') as file:
        file.write(json.dumps(data_list, indent=4))


def data_list_in_file():
    with open('db.json', 'r') as file:
        data_list = json.loads(file.read())
    return data_list


def del_data(country, capital):
    for i_data in data_list_in_file():
        if country in i_data.keys() and capital in i_data.values():
            print('yes')


# add_data(input_data())
del_data('gfd', 'abc')
