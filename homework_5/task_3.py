text = input('Введите текст: ')

print(f'Количество предложений в тексте: {text.count(".") + text.count("!") + text.count("?")}.')
