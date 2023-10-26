import socket
import random

# List of server addresses
servers = [("127.0.0.1", 12345)]

# Create a load balancer socket
load_balancer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lb_host = "127.0.0.1"
lb_port = 8888

load_balancer_socket.bind((lb_host, lb_port))
load_balancer_socket.listen(5)

print(f"Load balancer listening on {lb_host}:{lb_port}")

while True:
    client_socket, addr = load_balancer_socket.accept()
    print(f"Accepted connection from {addr}")

    # Select a random server
    server = random.choice(servers)

    # Forward the request to the selected server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(server)

    data = client_socket.recv(1024).decode("utf-8").strip()
    server_socket.send(data.encode("utf-8"))

    response = server_socket.recv(1024).decode("utf-8")
    client_socket.send(response.encode("utf-8"))

    server_socket.close()
    client_socket.close()