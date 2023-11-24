# 1) Добавить выбор: Если число в списке добавлять или нет.

class UserList:

    def __init__(self):
        self.user_list = []

    @staticmethod
    def user_input():
        try:
            num_input = int(input('Enter nums: '))
            return num_input
        except ValueError:
            print('\nInvalid error. Try again.')


    def add_new_num_in_list(num):
        pass


    def del_all_entries_num(num):
        pass


    def get_list():
        pass


    def check_num(num):
        pass


    def change_num(num, new_num):
        pass


def menu():
    user_list = UserList()
    flag = True
    choice = input('\n1-Add new num to the list.'
                   '\n2-Delete all entries num.'
                   '\n3-Get list.'
                   '\n4-Check num in the list.'
                   '\n5-Change num in the list.'
                   '\nq-Exit from program. -> ')

    while flag:
        if choice == '1':
            user_list.add_new_num_in_list()


if __name__ == '__main__':
    menu()
