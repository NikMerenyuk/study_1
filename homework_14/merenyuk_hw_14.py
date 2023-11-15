import re

count_vow = 0
count_con = 0
count_nums = 0
vowel = ['а', 'и', 'е', 'ё', 'о', 'у', 'ы', 'э', 'ю', 'я']
consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р',
              'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']

with open('text.txt', 'r', encoding='utf-8') as file_1:
    with open('new_text.txt', 'w', encoding='utf-8') as file_2:
        text = file_1.read()
        for i in text:
            if re.match(r'\d', i):
                count_nums += 1
        for i in text.strip():
            for j in vowel:
                if i == j:
                    count_vow += 1
            for k in consonants:
                if i == k:
                    count_con += 1
        file_2.write(f'Количество символов: {len(text)}\n')
        file_1.seek(0)
        file_2.write(f'Количество строк: {len(file_1.readlines())}\n')
        file_2.write(f'Количество гласных букв: {count_vow}\n')
        file_2.write(f'Количество согласных букв: {count_con}\n')
        file_2.write(f'Количество цифр: {count_nums}\n')
