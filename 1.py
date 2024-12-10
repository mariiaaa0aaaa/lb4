import socket
import sys


# Функція для запуску серверної частини
def run_server():
    HOST = '127.0.0.1'  # Локальний хост
    PORT = 8001  # Порт сервера

    # Створюємо сокет для серверної частини
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Налаштовуємо сервер на можливість повторного використання адреси
        server_socket.bind((HOST, PORT))  # Прив'язуємо сокет до адреси і порту
        server_socket.listen(1)  # Слухаємо запити на підключення (максимум 1 клієнт)

        print(f"Підключення до сервера {HOST}:{PORT}...")

        # Приймаємо підключення від клієнта
        conn, addr = server_socket.accept()
        with conn:
            print(f"З'єднано за допомогою {addr}")

            # Отримуємо дані від клієнта в циклі
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Отримано: {data.decode('utf-8')}")
                conn.sendall(data)


# Функція для запуску клієнтської частини
def run_client():
    HOST = '127.0.0.1'  # IP-адреса сервера
    PORT = 8001  # Порт сервера

    # Створюємо сокет для клієнтської частини
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        message = input("Введіть повідомлення для відправки на сервер: ")
        client_socket.sendall(message.encode('utf-8'))
        data = client_socket.recv(1024)
        print(f"Отримано з сервера: {data.decode('utf-8')}")


# Головна функція для вибору режиму роботи
if __name__ == "__main__":
    mode = input("Оберіть режим (server/client): ").strip().lower()

    if mode == "server":
        run_server()  # Запуск серверної частини
    elif mode == "client":
        run_client()  # Запуск клієнтської частини
    else:
        print("Неіснуючий режим. Оберіть 'server' або 'client'.")
