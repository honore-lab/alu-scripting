import socket

# Set up the host and port for the server
HOST = "127.0.0.1"  # Localhost (runs only on your machine)
PORT = 2323         # Non-standard Telnet port to avoid conflicts

# Create a TCP socket using IPv4
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Start listening for incoming connections
server_socket.listen()

print(f"** Server is running on {HOST}:{PORT} and waiting for connections...")

while True:
    # Accept a new client connection
    conn, addr = server_socket.accept()
    print(f"[+] Connection received from {addr}")

    # Send welcome message and prompt for username
    conn.sendall(b"Welcome to the Fake Login Server!\n")
    conn.sendall(b"Username: ")
    username = conn.recv(1024).strip()

    # Prompt for password (no encryption!)
    conn.sendall(b"Password: ")
    password = conn.recv(1024).strip()

    # Echo the entered credentials back to the user
    message = f"\nHello {username.decode()}, you typed '{password.decode()}' as your password.\n"
    conn.sendall(message.encode())
    conn.sendall(b"This is why Telnet is risky! Everything is visible!\n")

    # Close the connection
    conn.close()