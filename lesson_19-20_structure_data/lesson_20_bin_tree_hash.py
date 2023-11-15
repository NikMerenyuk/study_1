# class Node:
#
#     def __init__(self, value, right=None, left=None):
#         self.value = value
#         self.right = right
#         self.left = left
#
#
# class BinaryTree:
#
#     def __init__(self, root):
#         self.root = root
#
#     def bfs(self, node):
#         """
#         Breath First Search(BFS) (поиск в ширину)
#         :param node:
#         :return:
#         """
#         if node is None:
#             return
#
#         queue = [node]
#         while queue:
#             new_level = []
#             for i_node in queue:
#                 print(i_node.value)
#                 if i_node.left:
#                     new_level.append(i_node.left)
#                 if i_node.right:
#                     new_level.append(i_node.right)
#             queue = new_level
#
#     def dfs(self, node):
#         """
#         Depth First Seatch (DFS) (обход в глубину)
#         :param node:
#         :return:
#         """
#         if node is None:
#             return
#         self.dfs(node.right)
#         print(node.value)
#         self.dfs(node.left)
#
#     def min_depth(self):
#         if self.root is None:
#             return 0
#         queue = [self.root]
#         cur_lvl = 0
#         while queue:
#             cur_lvl += 1
#             for i_node in range(len(queue)):
#                 cur_node = queue.pop(0)
#                 if cur_node.left or cur_node.right:
#                     if cur_node.left:
#                         queue.append(cur_node.left)
#                     elif cur_node.right:
#                         queue.append(cur_node.right)
#                 else:
#                     return cur_lvl
#         return cur_lvl
#
#
# root = Node(10)
# node_1 = Node(5)
# root.left = node_1
# node_2 = Node(7)
# node_1.right = node_2
# node_3 = Node(16)
# root.right = node_3
# node_4 = Node(13)
# node_3.left = node_4
# node_5 = Node(2)
# node_1.left = node_5
# node_6 = Node(20)
# node_3.right = node_6
#
# # print(root.value, root.right.value, root.left.value)
# # print(node_1.value, node_1.right.value, node_1.left.value)
#
# b_tree = BinaryTree(root)
# # b_tree.bfs(root)
# # b_tree.dfs(root)
# # print(b_tree.min_depth())


# ХЕШИРОВАНИЕ

import hashlib
import json

# correct_hash = 'dd679c0b9fd408a04148aa7d30c9df393f67b7227f65693fffe0ed6d0f0ade59'
#
# hash_function = hashlib.sha256()
# string = 'Привет'
# hash_function.update(string.encode())
# hashed_string = hash_function.hexdigest()
# print(hashed_string == correct_hash)


# correct_password = '920d9ec4b054155d18ef6e03016f208ba7ce5b0016c6e4191f2a48a36d6d5bbe'
#
#
# def hash_password(password):
#     hash_function = hashlib.sha256()
#     hash_function.update(password.encode())
#     hashed_password = hash_function.hexdigest()
#     return hashed_password
#
#
# password = input('Введите пароль: ')
#
# if hash_password(password) == correct_password:
#     print('Пароль верный')
# else:
#     print('Пароль неверный')


# import requests
# import json
#
# response = requests.get('https://swapi.dev/api/people/1/')
# data = json.loads(response.text)
# print


def welcome():
    choice = input('1-Регистрация\n'
                   '2-Авторизация -> ')
    if choice == '1':
        registration()
    elif choice == '2':
        get_user_by_email()


def hash_password(password):
    hash_function = hashlib.sha256()
    hash_function.update(password.encode())
    hashed_password = hash_function.hexdigest()
    return hashed_password


def registration():
    reg_q = input('Введите email и пароль через пробел: ')
    email, password = reg_q.split(' ')
    user = set_user_data(email, password)
    add_new_user_to_file(user)


def set_user_data(email, password):
    user_data = {'email': email, 'password': hash_password(password)}
    return user_data


def add_new_user_to_file(user):
    with open('users.json', 'r') as file:
        users_list = json.loads(file.read())
        users_list.append(user)
    with open('users.json', 'w') as file:
        file.write(json.dumps(users_list, indent=4))


def get_user_by_email():
    email = input('Введите email: ')
    with open('users.json', 'r') as file:
        users_list = json.loads(file.read())
        for i_user in users_list:
            if i_user['email'] == email:
                password = input('Введите пароль: ')
                if hash_password(password) == i_user['password']:
                    print('Вы авторизовались!')
                    return
                else:
                    print('Пароль неверный!')
                    return
            else:
                print('Вас нет в пользователях!')
                return


# user = set_user_data('test@gmail.com', '12345')
# add_new_user_to_file(user)
#
# user_2 = set_user_data('test_2@gmail.com', '54321')
# add_new_user_to_file(user_2)

# get_user_by_email('test@gmail.com')

welcome()
