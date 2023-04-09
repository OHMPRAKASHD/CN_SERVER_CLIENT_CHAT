import socket

# Define host and port
HOST = '127.0.0.1'
PORT = 12345

# Create socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

print('Connected to server')

# Start the chat
while True:
    # Send a message to the server
    message = input('Enter your message: ')
    client_socket.send(message.encode())

    # Receive response from the server
    data = client_socket.recv(1024).decode()

    # Exit loop if no more data is received
    if not data:
        break

    # Print the received data
    print(f'Received from server: {data}')

# Close the socket
client_socket.close()

