import socket

# Define the main server address and port
MAIN_SERVER_HOST = '127.0.0.1'
MAIN_SERVER_PORT = 12345

# Create a socket object
main_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
main_server_socket.bind((MAIN_SERVER_HOST, MAIN_SERVER_PORT))

# Listen for incoming connections
main_server_socket.listen(5)

print("Main Server is listening for connections...")

while True:
    # Accept incoming connections
    client_socket, client_address = main_server_socket.accept()
    print(f"Connection established with {client_address}")

    # Forward the connection to the sub-server
    sub_server_host = '127.0.0.1'
    sub_server_port = 54321
    sub_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sub_server_socket.connect((sub_server_host, sub_server_port))

    # Forward data between the client and the sub-server
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        sub_server_socket.sendall(data)
        
        sub_server_response = sub_server_socket.recv(1024)
        client_socket.sendall(sub_server_response)

    # Close the connection
    sub_server_socket.close()
    client_socket.close()
