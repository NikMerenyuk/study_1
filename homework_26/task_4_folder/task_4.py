import os
from threading import Thread

input_directory_path = input(str('Enter a directory path: '))
input_word = input('Enter a word: ')  # stop
united_file_path = input(str('Enter a united file path: '))


def search_words():
    for root, dirs, files in os.walk(input_directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as current_file:
                text = current_file.read()
                print(f'\nCheck: {file}')
                if input_word in text:
                    print(f'Found: {input_word}!')
                    with open(united_file_path, 'a') as united_file:
                        united_file.write(text)
                else:
                    print('Nothing!')


def ban_words():
    with open('banned_word.txt', 'r') as ban_file:
        with open('united_file.txt', 'r') as united_file:
            text = united_file.read()
            for bad in ban_file.readlines():
                if bad.strip() in text:
                    text = text.replace(bad, '')
        with open('united_file.txt', 'w') as united_file:
            united_file.write(text)


search_thread = Thread(target=search_words)
ban_thread = Thread(target=ban_words)


if __name__ == '__main__':
    search_thread.start()
    search_thread.join()

    ban_thread.start()
    ban_thread.join()
