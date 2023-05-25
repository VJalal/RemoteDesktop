import socket
import mouse
import base64

# Define the host and port for the server
HOST = "0.0.0.0"
PORT = 53866

# Set the initial mouse position
current_x, current_y = mouse.get_position()

with open("img.bmp", "rb") as file:
    image_data = file.read()

img64 = base64.b64encode(image_data).decode()
print(img64)
# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Bind the socket to the host and port
    server_socket.bind((HOST, PORT))

    # Listen for incoming connections
    server_socket.listen(1)
    print("Waiting for incoming connection...")

    # Accept a client connection
    client_socket, addr = server_socket.accept()
    print("Client connected:", addr)

    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode()
        if not data:
            break

        # Extract mouse position data
        position = data.split(",")
        if len(position) != 2:
            continue  # Ignore invalid data

        try:
            x, y = map(int, position)
            client_socket.sendall(img64.encode())
        except ValueError:
            continue  # Ignore invalid data

        # Move the mouse on the host machine
        current_x = x
        current_y = y
        mouse.move(current_x, current_y)
