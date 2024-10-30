import socket
import threading

def sort_floats(numbers):
    """Sắp xếp danh sách số thực và trả về."""
    return sorted(numbers)

# TCP - Tuần tự Server
def tcp_sequential_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12366))
    server_socket.listen(5)
    print("Tuần tự TCP Server đang lắng nghe trên cổng 12366...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Kết nối từ {client_address} đã được thiết lập.")
        data = client_socket.recv(1024).decode()
        numbers = list(map(float, data.split()))
        sorted_numbers = sort_floats(numbers)
        response = " ".join(map(str, sorted_numbers))
        client_socket.send(response.encode())
        client_socket.close()

# TCP - Song Song Server
def tcp_parallel_server():
    def handle_client(client_socket, client_address):
        print(f"Kết nối từ {client_address} đã được thiết lập.")
        data = client_socket.recv(1024).decode()
        numbers = list(map(float, data.split()))
        sorted_numbers = sort_floats(numbers)
        response = " ".join(map(str, sorted_numbers))
        client_socket.send(response.e
