import socket
import threading

# Функція для серверної частини
def echo_server():
    HOST = '127.0.0.1'  # IP-адреса сервера
    PORT = 8001         # Порт сервера

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))  # Прив'язка до адреси та порту
        server_socket.listen(1)  # Очікування з'єднань
        print(f"Сервер запущено на {HOST}:{PORT}, очікується підключення...")

        conn, addr = server_socket.accept()  # Прийом підключення
        with conn:
            print(f"Підключено клієнта {addr}")
            while True:
                data = conn.recv(1024)  # Отримання даних від клієнта
                if not data:
                    break
                print(f"Отримано від клієнта: {data.decode('utf-8')}")
                conn.sendall(data)  # Відправка даних назад клієнту

# Функція для клієнтської частини
def echo_client():
    HOST = '127.0.0.1'  # IP-адреса сервера
    PORT = 8001         # Порт сервера

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((HOST, PORT))  # Підключення до сервера
            print(f"Підключено до сервера {HOST}:{PORT}")

            # Введення повідомлення для відправки
            message = input("Введіть повідомлення, що відправиться на сервер: ")
            client_socket.sendall(message.encode('utf-8'))  # Відправка даних

            # Отримання відповіді від сервера
            data = client_socket.recv(1024)
            print(f"Отримано від сервера: {data.decode('utf-8')}")  # Виведення відповіді

        except ConnectionRefusedError:
            print(f"Не вдається підключитися до сервера за адресою {HOST}:{PORT}")
        except Exception as e:
            print(f"Виникла помилка: {e}")

# Головна функція для вибору між сервером та клієнтом
def main():
    choice = input("Виберіть режим:\n1. Запустити сервер\n2. Запустити клієнт\nВведіть 1 або 2: ")

    if choice == '1':
        echo_server()  # Запуск сервера
    elif choice == '2':
        echo_client()  # Запуск клієнта
    else:
        print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
