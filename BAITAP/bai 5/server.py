import socket
import threading

# Bài 5: Server xử lý tính tổng các chữ số của số nguyên do client gửi

def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

# TCP - Tuần Tự Server
def tcp_sequential_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12380))
    server_socket.listen(5)
    print("TCP Tuần Tự Server đang lắng nghe trên cổng 12380...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Kết nối từ {client_address} đã được thiết lập.")
        data = client_socket.recv(1024).decode()
        number = int(data)

        digit_sum = sum_of_digits(number)
        response = str(digit_sum)

        client_socket.send(response.encode())
        client_socket.close()

# TCP - Song Song Server
def tcp_parallel_server():
    def handle_client(client_socket, client_address):
        print(f"Kết nối từ {client_address} đã được thiết lập.")
        data = client_socket.recv(1024).decode()
        number = int(data)

        digit_sum = sum_of_digits(number)
        response = str(digit_sum)

        client_socket.send(response.encode())
        client_socket.close()
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12381))
    server_socket.listen(5)
    print("TCP Song Song Server đang lắng nghe trên cổng 12381...")

    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

# UDP - Tuần Tự Server
def udp_sequential_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("127.0.0.1", 12382))
    print("UDP Tuần Tự Server đang lắng nghe trên cổng 12382...")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        number = int(data.decode())

        digit_sum = sum_of_digits(number)
        response = str(digit_sum)

        server_socket.sendto(response.encode(), client_address)

# UDP - Song Song Server
def udp_parallel_server():
    def handle_client(data, client_address, server_socket):
        print(f"Kết nối từ {client_address} đã được thiết lập.")
        number = int(data.decode())

        digit_sum = sum_of_digits(number)
        response = str(digit_sum)

        server_socket.sendto(response.encode(), client_address)
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("127.0.0.1", 12383))
    print("UDP Song Song Server đang lắng nghe trên cổng 12383...")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        client_handler = threading.Thread(target=handle_client, args=(data, client_address, server_socket))
        client_handler.start()

# Hàm chính để chọn chế độ server
def main():
    choice = input("Chọn chế độ server (1: TCP tuần tự, 2: TCP song song, 3: UDP tuần tự, 4: UDP song song): ")
    if choice == '1':
        tcp_sequential_server()
    elif choice == '2':
        tcp_parallel_server()
    elif choice == '3':
        udp_sequential_server()
    elif choice == '4':
        udp_parallel_server()
    else:
        print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()