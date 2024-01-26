import shutil
from threading import Thread


def file_migration():
    file_path = input(str('Enter file path: '))
    new_directory = input(str('Enter new directory: '))
    shutil.move(file_path, new_directory)


migr_thread = Thread(target=file_migration)

if __name__ == '__main__':
    migr_thread.start()
    migr_thread.join()
