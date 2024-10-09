import socket

def server_program():
    # Tạo socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Cấu hình host và port
    host = '127.0.0.1'
    port = 12345
    
    # Bind server socket đến host và port
    server_socket.bind((host, port))
    
    # Lắng nghe kết nối từ client
    server_socket.listen(1)
    print("Server đang lắng nghe...")

    # Chấp nhận kết nối từ client
    conn, address = server_socket.accept()
    print("Kết nối từ:", str(address))

    # Nhận dữ liệu từ client
    data = conn.recv(1024).decode()
    
    if data:
        # Tách dữ liệu thành 2 số
        num1, num2 = map(int, data.split())
        result = num1 + num2
        
        # Gửi kết quả tổng lại cho client
        conn.send(str(result).encode())

    # Đóng kết nối
    conn.close()

if __name__ == '__main__':
    server_program()
