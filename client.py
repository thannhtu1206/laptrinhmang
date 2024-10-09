import socket

def client_program():
    # Tạo socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Cấu hình server host và port
    host = '127.0.0.1'
    port = 12345

    # Kết nối đến server
    client_socket.connect((host, port))

    # Nhập hai số từ người dùng
    num1 = input("Nhập số thứ nhất: ")
    num2 = input("Nhập số thứ hai: ")

    # Gửi hai số đến server
    client_socket.send(f"{num1} {num2}".encode())

    # Nhận kết quả tổng từ server
    result = client_socket.recv(1024).decode()

    # Hiển thị kết quả tổng
    print(f"Tổng của {num1} và {num2} là: {result}")

    # Đóng kết nối
    client_socket.close()

if __name__ == '__main__':
    client_program()
