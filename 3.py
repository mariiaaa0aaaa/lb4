import socket
import os

# Серверна частина
def start_server():
    HOST = '127.0.0.1'  # Локальний хост
    PORT = 8001  # Порт сервера

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Сервер працює на {HOST}:{PORT}...")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Підключено до {addr}")

            try:
                # Отримуємо розмір файлу
                file_size = int(conn.recv(1024).decode('utf-8'))
                print(f"Розмір файлу: {file_size} байт")

                # Отримуємо сам файл
                with open('file.txt', 'wb') as f:
                    bytes_received = 0
                    while bytes_received < file_size:
                        data = conn.recv(1024)
                        if not data:
                            break
                        f.write(data)
                        bytes_received += len(data)
                    print("Файл отримано та збережено як 'file.txt'.")
            except Exception as e:
                print(f"Сталася помилка на сервері: {e}")

# Клієнтська частина
def send_file():
    HOST = '127.0.0.1'  # IP-адреса сервера
    PORT = 8001  # Порт сервера

    # Введення шляху до файлу
    file_path = input("Введіть шлях до файлу для відправки: ")

    try:
        # Перевіряємо, чи існує файл
        if not os.path.isfile(file_path):
            print(f"Файл за шляхом {file_path} не знайдено.")
            return

        # Отримуємо розмір файлу
        file_size = os.path.getsize(file_path)
        print(f"Розмір файлу: {file_size} байт")

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))

            # Відправляємо розмір файлу
            client_socket.sendall(str(file_size).encode('utf-8'))

            # Відправляємо сам файл
            with open(file_path, 'rb') as f:
                while True:
                    bytes_data = f.read(1024)
                    if not bytes_data:
                        break
                    client_socket.sendall(bytes_data)

            print(f"Файл {file_path} успішно відправлено.")
    except FileNotFoundError as e:
        print(f"Помилка: файл не знайдений. {e}")
    except Exception as e:
        print(f"Сталася помилка: {e}")
    finally:
        print("Клієнтська частина завершена.")

# Головна функція для вибору між сервером та клієнтом
def main():
    choice = input("Виберіть з'єднання:\n1. Запустити сервер\n2. Запустити клієнт\nВведіть 1 або 2: ")

    if choice == '1':
        start_server()  # Запуск сервера
    elif choice == '2':
        send_file()  # Запуск клієнта
    else:
        print("Неіснуюче з'єднання. Спробуйте ще раз.")

if __name__ == "__main__":
    main()