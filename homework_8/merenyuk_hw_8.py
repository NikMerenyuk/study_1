import re

tels = ['9999999999', '999999-999', '99999x9999']
counter = 1
for i in tels:
    match = re.match(r'^[8, 9]\d{9}\b', i, flags=False)
    if match:
        print(f'{counter} номер: все в порядке')
    else:
        print(f'{counter} номер: не подходит')
    counter += 1

