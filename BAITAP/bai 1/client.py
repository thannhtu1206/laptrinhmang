import socket

def tcp_client(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(("127.0.0.1", port))
        a, b = int(input("Nhập a: ")), int(input("Nhập b: "))
        client_socket.send(f"{a} {b}".encode())
        print("Kết quả:", client_socket.recv(1024).decode())

def udp_client(port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        a, b = int(input("Nhập a: ")), int(input("Nhập b: "))
        client_socket.sendto(f"{a} {b}".encode(), ("127.0.0.1", port))
        data, _ = client_socket.recvfrom(1024)
        print("Kết quả:", data.decode())

def main():
    choice = input("Chọn client (1: TCP tuần tự, 2: TCP song song, 3: UDP tuần tự, 4: UDP song song): ")
    if choice == '1':
        tcp_client(12380)
    elif choice == '2':
        tcp_client(12381)
    elif choice == '3':
        udp_client(12382)
    elif choice == '4':
        udp_client(12383)
    else:
        print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
