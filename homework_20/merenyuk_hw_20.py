# Task 1
#
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def add_nodes(self, values):
        for value in values:
            self.add_node(value)

    def remove_node(self, value):
        prev = None
        current = self.head
        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next
        else:
            print('Узла с таким значением нет!')

    def check_value(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def get_all_nodes(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def change_node(self, value, new_value):
        current = self.head
        while current:
            if current.value == value:
                current.value = new_value
                print('Значение обновлено!')
                return
            current = current.next
        else:
            print(f'Значения {value} нет в связном списке.')


def menu():
    list_1 = LinkedList()
    nums = map(int, input('Введите набор чисел через пробел: ').split(' '))
    list_1.add_nodes(nums)
    flag = True
    while flag:
        change = input('\n1-Добавить элемент в список.\n'
                       '2-Удалить элемент из списка.\n'
                       '3-Показать содержимое списка.\n'
                       '4-Проверить есть ли значение в списке.\n'
                       '5-Заменить значение в списке.\n'
                       '0-Выход из программы. -> ')
        print()
        if change == '1':
            new_node = int(input('Введите значение нового узла: '))
            list_1.add_node(new_node)

        elif change == '2':
            rem_node = int(input('Введите значение удаляемого узла: '))
            list_1.remove_node(rem_node)

        elif change == '3':
            list_1.get_all_nodes()

        elif change == '4':
            check_val = int(input('Введите значение проверяемого узла: '))
            list_1.check_value(check_val)
            if list_1.check_value(check_val) is True:
                print(f'Узел со значением {check_val} есть в списке')
            else:
                print(f'Узла со значением {check_val} нет в списке')

        elif change == '5':
            change_val = int(input('Введите значение узла, который хотите заменить: '))
            list_1.check_value(change_val)
            if list_1.check_value(change_val) is True:
                new_value = int(input('Введите новое значение: '))
                list_1.change_node(change_val, new_value)
            else:
                print(f'Узла со значением {change_val} нет в списке')

        elif change == '0':
            print('Программа закончила свою работу.')
            flag = False

        else:
            continue


menu()


# TASK 2
#
# class Node:
#
#     def __init__(self, value=None):
#         self.value = value
#         self.next = None
#         self.prev = None
#
#
# class LinkedList:
#
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def add_node(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#             return
#         tail = self.head
#         while tail.next:
#             tail = tail.next
#         tail.next = new_node
#         new_node.prev = tail
#
#     def add_nodes(self, values):
#         for value in values:
#             self.add_node(value)
#
#     def get_left_right_values(self, value):
#         current_node = self.head
#         while current_node:
#             if current_node.value == value:
#                 if current_node.prev is None:
#                     print(None)
#                     print(current_node.next.value)
#                 elif current_node.next is None:
#                     print(current_node.prev.value)
#                     print(None)
#                 else:
#                     print(current_node.prev.value)
#                     print(current_node.next.value)
#                 return
#             else:
#                 current_node = current_node.next
#
#     def remove_node(self, value):
#         if self.head is None:
#             return
#         current_node = self.head
#         while current_node:
#             if current_node.value == value:
#                 if current_node.prev is None and current_node.next is None:
#                     self.head = None
#                 elif current_node.prev is None:
#                     current_node.next.prev = current_node.prev
#                     self.head = current_node.next
#                 elif current_node.next is None:
#                     current_node.prev.next = current_node.next
#                 else:
#                     current_node.prev.next = current_node.next
#                     current_node.next.prev = current_node.prev
#                 return
#             current_node = current_node.next
#
#     def get_all_nodes(self):
#         current_node = self.head
#         while current_node:
#             if current_node is None:
#                 print('Список пуст.')
#             else:
#                 print(current_node.value)
#                 current_node = current_node.next
#         return
#
#     def check_value(self, value):
#         current_node = self.head
#         while current_node:
#             if current_node.value == value:
#                 return True
#             current_node = current_node.next
#         return False
#
#     def change_node(self, value, new_value):
#         current_node = self.head
#         while current_node:
#             if current_node.value == value:
#                 current_node.value = new_value
#                 return
#             current_node = current_node.next
#         else:
#             print(f'Значения {value} нет в связном списке.')
#
#
# def menu():
#     list_1 = LinkedList()
#     strings = input('Введите набор строк через пробел: ').split(' ')
#     list_1.add_nodes(strings)
#     flag = True
#     while flag:
#         change = input('\n1-Добавить элемент в список.\n'
#                        '2-Удалить элемент из списка.\n'
#                        '3-Показать содержимое списка.\n'
#                        '4-Проверить есть ли значение в списке.\n'
#                        '5-Заменить значение в списке.\n'
#                        '6-Показать соседние значения узла.\n'
#                        '0-Выход из программы. -> ')
#
#         if change == '1':
#             new_node = input('\nВведите значение нового узла: ')
#             list_1.add_node(new_node)
#             print('Узел добавлен.')
#         elif change == '2':
#             rem_node = input('\nВведите значение удаляемого узла: ')
#             if list_1.check_value(rem_node) is True:
#                 list_1.remove_node(rem_node)
#                 print('Узел удален.')
#             else:
#                 print('Узла с таким значением нет.')
#         elif change == '3':
#             print()
#             list_1.get_all_nodes()
#
#         elif change == '4':
#             che_value = input('\nВведите значение проверяемого узла: ')
#             if list_1.check_value(che_value) is True:
#                 print(f'Узел со значением "{che_value}" есть в списке.')
#             else:
#                 print(f'Узла со значением "{che_value}" нет в списке.')
#
#         elif change == '5':
#             cha_value = input('\nВведите значение заменяемого узла: ')
#             if list_1.check_value(cha_value) is True:
#                 new_value = input('Введите новое значение: ')
#                 list_1.change_node(cha_value, new_value)
#                 print(f'Значение "{cha_value}" изменено на "{new_value}".')
#             else:
#                 print(f'Узла со значением "{cha_value}" нет в списке.')
#
#         elif change == '6':
#             get_value = input('\nВведите значение узла: ')
#             if list_1.check_value(get_value) is True:
#                 list_1.get_left_right_values(get_value)
#             else:
#                 print(f'Узла со значением "{get_value}" нет в списке.')
#
#         elif change == '0':
#             print('\nПрограмма закончила свою работу.')
#             flag = False
#
#
# menu()


# TASK 3
#
# class Stack:
#     def __init__(self):
#         self.limit = 5
#         self.stack = []
#
#     def add_item(self, item: int) -> str:
#         if len(self.stack) < self.limit:
#             self.stack.append(item)
#             return 'Значение добавлено.'
#         else:
#             return 'Стек заполен.'
#
#     def push(self, item) -> None:
#         self.stack.pop()
#         self.stack.append(int(item))
#
#     def counting(self) -> str:
#         return f'\nКол-во целых чисел: {len(self.stack)}'
#
#     def check_empty_stack(self) -> bool:
#         if len(self.stack) == 0:
#             return True
#         else:
#             return False
#
#     def check_full_stack(self) -> bool:
#         if len(self.stack) == self.limit:
#             return True
#         else:
#             return False
#
#     def clearing_stack(self) -> None:
#         while self.stack:
#             self.stack.pop()
#
#     def get_upper_value(self) -> str | int:
#         if len(self.stack) == 0:
#             return 'В стеке нет значений.'
#         else:
#             return self.stack[-1]
#
#
# def menu():
#     stack = Stack()
#     flag = True
#
#     while flag:
#         choice = input('\n1-Помещение целого значения в стек.\n'
#                        '2-Выталкивание целого значения из стека.\n'
#                        '3-Подсчет количеста целых в стеке.\n'
#                        '4-Проверить пустой ли стек.\n'
#                        '5-Проверить полный ли стек.\n'
#                        '6-Очистить стек.\n'
#                        '7-Получение значения без выталкивания верхнего целого в стеке.\n'
#                        '0-Выход из программы. -> ')
#         match choice:
#             case '1':
#                 print(stack.add_item(int(input('\nВведите значение: '))))
#             case '2':
#                 stack.push(int(input('\nВведите значение: ')))
#                 print('\nЗначение изменено.')
#             case '3':
#                 print(stack.counting())
#             case '4':
#                 if stack.check_empty_stack() is True:
#                     print('\nСтек пустой.')
#                 else:
#                     print('\nВ стеке есть значения.')
#             case '5':
#                 if stack.check_full_stack() is True:
#                     print('\nСтек полный.')
#                 else:
#                     print('\nСтек не полный')
#             case '6':
#                 stack.clearing_stack()
#                 print('\nСтек очищен.')
#             case '7':
#                 print()
#                 print(stack.get_upper_value())
#             case '0':
#                 print('\nПрограмма завершила свою работу.')
#                 flag = False
#             case _:
#                 print('\nНеверный формат ввода.')


# TASK 4
#
# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def add_item(self, item: int) -> str:
#         if len(self.stack):
#             self.stack.append(item)
#             return 'Значение добавлено.'
#         else:
#             return 'Стек заполен.'
#
#     def push(self, item) -> None:
#         self.stack.pop()
#         self.stack.append(int(item))
#
#     def counting(self) -> str:
#         return f'\nКол-во целых чисел: {len(self.stack)}'
#
#     def check_empty_stack(self) -> bool:
#         if len(self.stack) == 0:
#             return True
#         else:
#             return False
#
#     def clearing_stack(self) -> None:
#         while self.stack:
#             self.stack.pop()
#
#     def get_upper_value(self) -> str | int:
#         if len(self.stack) == 0:
#             return 'В стеке нет значений.'
#         else:
#             return self.stack[-1]
#
#
# def menu():
#     stack = Stack()
#     flag = True
#
#     while flag:
#         choice = input('\n1-Помещение целого значения в стек.\n'
#                        '2-Выталкивание целого значения из стека.\n'
#                        '3-Подсчет количеста целых в стеке.\n'
#                        '4-Проверить пустой ли стек.\n'
#                        '5-Очистить стек.\n'
#                        '6-Получение значения без выталкивания верхнего целого в стеке.\n'
#                        '0-Выход из программы. -> ')
#         match choice:
#             case '1':
#                 print(stack.add_item(int(input('\nВведите значение: '))))
#             case '2':
#                 stack.push(int(input('\nВведите значение: ')))
#                 print('\nЗначение изменено.')
#             case '3':
#                 print(stack.counting())
#             case '4':
#                 if stack.check_empty_stack() is True:
#                     print('\nСтек пустой.')
#                 else:
#                     print('\nВ стеке есть значения.')
#             case '5':
#                 stack.clearing_stack()
#                 print('\nСтек очищен.')
#             case '6':
#                 print()
#                 print(stack.get_upper_value())
#             case '0':
#                 print('\nПрограмма завершила свою работу.')
#                 flag = False
#             case _:
#                 print('\nНеверный формат ввода.')


if __name__ == '__main__':
    menu()
