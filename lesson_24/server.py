import socket


def start_server():
    host = '127.0.0.1'    # local host
    port = 12345

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(1)    # блокирующий сокет
    print(f'Сервер ожидает на {host}:{port}')

    while True:
        conn, address = server_socket.accept()
        print(f'Соединение установлено с {address}')

        while True:
            data = conn.recv(1024).decode()    # блокирующая функция
            if not data:
                break
            print(f'Client {data=}')
            message = input('-> ')
            conn.send(message.encode())

        conn.close()
        print('Connected is closed')


if __name__ == '__main__':
    start_server()
