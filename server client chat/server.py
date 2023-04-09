import socket

# Define host and port
HOST = '127.0.0.1'
PORT = 12345

# Create socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to a specific address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

print(f'Server listening on {HOST}:{PORT}')

# Accept incoming connections
client_socket, address = server_socket.accept()

print(f'Connected by {address}')

# Start the chat
while True:
    # Receive data from the client
    data = client_socket.recv(1024).decode()

    # Exit loop if no more data is received
    if not data:
        break

    # Print the received data
    print(f'Received from client: {data}')

    # Send a response back to the client
    message = input('Enter your message: ')
    client_socket.send(message.encode())

# Close the socket
client_socket.close()
server_socket.close()

