# import json
# dict_1 = {'country': 'Russia', 'capital': 'Moscow'}
# with open('db_test.json', 'r', encoding='utf8') as file:
#     list_1 = json.loads(file.read())
# while True:
#     print(f'Текущий список: {list_1}')
#     choice = input('\n1-Добавить.\n'
#                    '2-Сохранить. -> ')
#     match choice:
#         case '1':
#             print('Добавлено.')
#             list_1.append(dict_1)
#             continue
#         case '2':
#             with open('db_test.json', 'w') as file:
#                 file.write(json.dumps(list_1, indent=4))
#             print('Сохранено.')


dict_1 = {'age': 18, 'name': 'Ivan'}

print(dict_1['name'])
