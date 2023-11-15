text = input('Введите текст или слово: ')

if text.lower().replace(' ', '') == text.lower().replace(' ', '')[::-1]:
    print('Это палиндром!')
else:
    print('Это не палиндром.')