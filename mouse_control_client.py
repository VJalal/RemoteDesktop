import socket
import base64

# Define the server host and port
HOST = "IP"
PORT = 53866

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Connect to the server
    client_socket.connect((HOST, PORT))
    print("Connected to server")

    while True:
        # Prompt the user for mouse position input
        x = input("Enter the X position (or 'q' to quit): ")
        if x == "q":
            break

        y = input("Enter the Y position (or 'q' to quit): ")
        if y == "q":
            break

        # Send the mouse position data to the server
        data = f"{x},{y}"
        client_socket.sendall(data.encode())

        img = client_socket.recv(4096 * 2000).decode()
        img = base64.b64decode(img)

        with open("rec_img.png", "wb") as file:
            file.write(img)
