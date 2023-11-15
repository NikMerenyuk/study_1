# ОЧЕРЕДЬ
#
# class Queue:
#     """
#     FIFO First In First Out
#     """
#     def __init__(self):
#         self.queue = []
#
#     def add_item(self, item):
#         self.queue.append(item)
#
#     def pop_item(self):
#         if self.queue:
#             self.queue.pop(0)
#
#     def show_queue(self):
#         print('Очередь: ', self.queue)
#         return self.queue
#
#
# queue = Queue()
# queue.add_item('asd')
# queue.add_item(5)
# queue.show_queue()
# queue.pop_item()
# queue.show_queue()


# СТЭК
class Stack:
    """
    LIFO Last In First Out
    """
    def __init__(self):
        self.stack = []

    def add_item(self, item):
        self.stack.append(item)

    def pop_item(self):
        if self.stack:
            self.stack.pop()

    def show_queue(self):
        print('Стэк:', self.stack)
        return self.stack


stack = Stack()
stack.add_item('asd')
stack.add_item(5)
stack.show_queue()
stack.pop_item()
stack.show_queue()


# СВЯЗАННЫЙ СПИСОК
#
# class Node:
#
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
#
#
# class LinkedList:
#
#     def __init__(self, head):
#         self.head = head
#
#     def get_all_nodes(self):
#         current = self.head
#         while current:
#             yield current.value
#             current = current.next
#
#     def remove_node(self, value):
#         current = self.head
#         prev = current
#         while current:
#             if current.value == value:
#                 prev.next = current.next
#                 return
#             prev = current
#             current = current.next
#
#     def get_len_list(self):
#         current = self.head
#         count = 0
#         while current:
#             count += 1
#             current = current.next
#         return count
#
#     def get_middle_value(self):
#         current = self.head
#         for i_value in range(self.get_len_list() // 2 - 1):
#             current = current.next
#         return current.value
#
#     def get_value_node(self, node):
#         current = self.head
#         for i_value in range(node - 1):
#             current = current.next
#         return current.value
#
#     def new_head(self, new_value):
#         node = Node(new_value)
#         node.next = self.head
#         self.head = node
#
#     def reverse_linked_list(self):
#         prev = None
#         current = self.head
#         while current:
#             next = current.next
#             current.next = prev
#             prev = current
#             current = next
#         self.head = prev
#
#
# head = Node(15)    # Головной узел
#
# node_1 = Node(24)
# head.next = node_1
#
# node_2 = Node(78)
# node_1.next = node_2
#
# node_3 = Node(98)
# node_2.next = node_3
#
# node_4 = Node(657)
# node_3.next = node_4
#
# node_5 = Node(22)
# node_4.next = node_5
#
# linked_list = LinkedList(head)
# for i in linked_list.get_all_nodes():
#     print(i)
#
# linked_list.remove_node(22)
# for i in linked_list.get_all_nodes():
#     print(i)

# print(linked_list.get_len_list())
# print(linked_list.get_middle_value())
# print(linked_list.get_value_node(5))

# linked_list.new_head(1234)
#
# for i in linked_list.get_all_nodes():
#     print(i)

# linked_list.reverse_linked_list()
# for i in linked_list.get_all_nodes():
#     print(i)
