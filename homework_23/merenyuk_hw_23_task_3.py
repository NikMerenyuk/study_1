class Stack:

    def __init__(self):
        self.stack = []

    @staticmethod
    def user_input():
        input_str = str(input('\nEnter string: '))
        return input_str

    def push(self, item):
        self.stack.append(item)
        return

    def pop(self):
        if self.stack:
            upper_value = self.stack.pop()
            self.push(self.user_input())
            print(f'Popped string: {upper_value}.')
            return True
        else:
            return False

    def counting(self):
        return f'Number of str\'s in the stack: {len(self.stack)}'

    def check_empty_stack(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def clear_stack(self):
        self.stack.clear()

    def get_upper_value_without_pop(self):
        return f'\nUpper str: {self.stack[-1]}'

    def get_stack(self):
        return f'\nStack: {self.stack}'


def menu():
    stack = Stack()
    flag = True
    while flag:
        try:
            choice = int(input('\n1-Enter str in the stack.\n'
                               '2-Pop str from the stack.\n'
                               '3-Counting str\'s in the stack.\n'
                               '4-Checking empty stack.\n'
                               '5-Clearing stack.\n'
                               '6-Get upper str.\n'
                               '7-Get stack.\n'
                               '0-Exit from program. -> '))

            if choice == 1:
                stack.push(stack.user_input())
                print('String appended.')

            elif choice == 2:
                if not stack.pop():
                    print('\nStack is empty.')

            elif choice == 3:
                print(f'\n{stack.counting()}')

            elif choice == 4:
                if stack.check_empty_stack():
                    print('\nStack is empty.')
                else:
                    print('\nStack isn\'t empty.')

            elif choice == 5:
                stack.clear_stack()
                print('\nStack clear.')

            elif choice == 6:
                if stack.check_empty_stack():
                    print('\nStack is empty.')
                else:
                    print(stack.get_upper_value_without_pop())

            elif choice == 7:
                print(stack.get_stack())

            elif choice == 0:
                print('\nThe program has finished work.')
                flag = False

        except ValueError:
            print('\nInvalid input. Try again.')


if __name__ == '__main__':
    menu()
