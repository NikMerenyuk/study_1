text = input('Введите текст: ')
word = input('Введите зарезервированное слово: ')

print(text.replace(f'{word}', f'{word.upper()}'))
