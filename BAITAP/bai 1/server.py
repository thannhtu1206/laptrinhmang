import socket
import threading

# Function to calculate the sum of digits of a number
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

# Function to find numbers within range [a, b] with a digit sum equal to 15
def find_numbers_with_digit_sum(a, b, target_sum=15):
    return [x for x in range(a, b + 1) if sum_of_digits(x) == target_sum]

# TCP - Sequential Server
def tcp_sequential_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12380))
    server_socket.listen(5)
    print("TCP Sequential Server is listening on port 12380...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} established.")
        
        # Receive data from client and parse
        data = client_socket.recv(1024).decode()
        a, b = map(int, data.split())
        
        # Find numbers with digit sum equal to 15 and send response
        numbers = find_numbers_with_digit_sum(a, b)
        response = " ".join(map(str, numbers))
        
        client_socket.send(response.encode())
        client_socket.close()

# TCP - Parallel Server
def tcp_parallel_server():
    def handle_client(client_socket, client_address):
        print(f"Connection from {client_address} established.")
        
        # Receive data from client and parse
        data = client_socket.recv(1024).decode()
        a, b = map(int, data.split())
        
        # Find numbers with digit sum equal to 15 and send response
        numbers = find_numbers_with_digit_sum(a, b)
        response = " ".join(map(str, numbers))
        
        client_socket.send(response.encode())
        client_socket.close()
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12381))
    server_socket.listen(5)
    print("TCP Parallel Server is listening on port 12381...")

    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

# UDP - Sequential Server
def udp_sequential_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("127.0.0.1", 12382))
    print("UDP Sequential Server is listening on port 12382...")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        a, b = map(int, data.decode().split())
        
        # Find numbers with digit sum equal to 15 and send response
        numbers = find_numbers_with_digit_sum(a, b)
        response = " ".join(map(str, numbers))
        
        server_socket.sendto(response.encode(), client_address)

# UDP - Parallel Server
def udp_parallel_server():
    def handle_client(data, client_address, server_socket):
        print(f"Processing request from {client_address}.")
        a, b = map(int, data.decode().split())
        
        # Find numbers with digit sum equal to 15 and send response
        numbers = find_numbers_with_digit_sum(a, b)
        response = " ".join(map(str, numbers))
        
        server_socket.sendto(response.encode(), client_address)
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("127.0.0.1", 12383))
    print("UDP Parallel Server is listening on port 12383...")

    while True:
        data, client_address = server_socket.recvfrom(1024)
        client_handler = threading.Thread(target=handle_client, args=(data, client_address, server_socket))
        client_handler.start()

# Main function to choose and start the server
def main():
    print("Select server mode:")
    print("1: TCP Sequential")
    print("2: TCP Parallel")
    print("3: UDP Sequential")
    print("4: UDP Parallel")
    
    choice = input("Enter choice (1-4): ")
    if choice == '1':
        tcp_sequential_server()
    elif choice == '2':
        tcp_parallel_server()
    elif choice == '3':
        udp_sequential_server()
    elif choice == '4':
        udp_parallel_server()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()

