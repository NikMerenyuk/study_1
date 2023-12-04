class UserList:

    def __init__(self):
        self.user_list = []

    @staticmethod
    def user_input():
        try:
            num_input = int(input('\nEnter num: '))
            return num_input
        except ValueError:
            return False

    def check_empty_list(self):
        if len(self.user_list) == 0:
            return True

    def check_num_in_list(self, num):
        if num in self.user_list:
            return True

    def add_new_num_in_list(self, num):
        self.user_list.append(num)
        return True

    def del_all_entries_num(self, num):
        if self.check_num_in_list(num):
            while num in self.user_list:
                for i_num in self.user_list:
                    if i_num == num:
                        self.user_list.remove(num)
                        continue
        else:
            return False

    def get_list(self):
        return self.user_list

    def change_all_entries_num(self, num, new_num):
        count = 0
        if self.check_num_in_list(num):
            while num in self.user_list:
                for i_num in self.user_list:
                    count += 1
                    if i_num == num:
                        self.user_list[count - 1] = new_num
                        continue
        else:
            return False

    def change_first_entries_num(self, num, new_num):
        count = 0
        if self.check_num_in_list(num):
            while num in self.user_list:
                for i_num in self.user_list:
                    count += 1
                    if i_num == num:
                        self.user_list[count - 1] = new_num
                        return True
        else:
            return False


def menu():
    user_list = UserList()
    flag = True

    while flag:
        choice = input('\n1-Add new num to the list.'
                       '\n2-Delete all entries num.'
                       '\n3-Get list.'
                       '\n4-Check num in the list.'
                       '\n5-Change num in the list.'
                       '\nq-Exit from program. -> ')

        if choice == '1':
            num = (user_list.user_input())
            if not num:
                print('Invalid input. Try again.')
            else:
                if user_list.check_num_in_list(num):
                    add_or_not = input(f'\nNum {num} is already in the list:'
                                       '\n1-Add this num.'
                                       '\n2-Don\'t add this num. -> ')
                    if add_or_not == '1':
                        user_list.add_new_num_in_list(num)
                        print('Num appended.')
                    elif add_or_not == '2':
                        print(f'\nThe num {num} won\'t be added to the list.')
                        continue
                    else:
                        print('Invalid input. Try again.')
                else:
                    user_list.add_new_num_in_list(num)
                    print('Num appended.')

        elif choice == '2':
            if user_list.check_empty_list():
                print('\nList is empty.')
                continue
            else:
                num = user_list.user_input()
                if user_list.del_all_entries_num(num):
                    print(f'All entries num {num} been deleted.')
                else:
                    print(f'Number is not in the list.')

        elif choice == '3':
            print(f'\nYour list: {user_list.get_list()}')

        elif choice == '4':
            if user_list.check_empty_list():
                print('\nList is empty.')
                continue
            else:
                if user_list.check_num_in_list(user_list.user_input()):
                    print('Num is in the list.')
                else:
                    print('Num isn\'t in the list.')

        elif choice == '5':
            if user_list.check_empty_list():
                print('\nList is empty.')
                continue
            else:
                print('\nEnter num in the list.')
                num = user_list.user_input()
                print('\nEnter new num.')
                new_num = user_list.user_input()
                choice = input(f'\n1-Change all entries.'
                               '\n2-Change first entries. -> ')
                if choice == '1':
                    if not user_list.change_all_entries_num(num, new_num):
                        print(f'\nAll entries num {num} changed to {new_num}.')
                elif choice == '2':
                    if user_list.change_first_entries_num(num, new_num):
                        print(f'\nFirst entries num {num} changed to {new_num}.')

                else:
                    print('Invalid input. Try again.')

        elif choice == 'q':
            print('\nThe program has finished work.')
            flag = False
        else:
            print('\nInvalid input. Try again.')


if __name__ == '__main__':
    menu()
