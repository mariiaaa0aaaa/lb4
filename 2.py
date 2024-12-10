import socket
import threading

def handle_client(conn, addr):
    with conn:
        print(f"Підключено до {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Отримано: {data.decode('utf-8')}")
            conn.sendall(data)

def echo_server():
    HOST = ''  # Приймає з'єднання на всіх доступних інтерфейсах
    PORT = 8001  # Порт сервера

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        print(f"Сервер працює на порту {PORT}...")

        while True:
            conn, addr = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()

if __name__ == "__main__":
    echo_server()
