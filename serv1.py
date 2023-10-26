import socket

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 12345

# Initialize the key-value store
kv_store = {}

server_socket.bind((host, port))
server_socket.listen(5)

print(f"Server 1 listening on {host}:{port}")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Accepted connection from {addr}")

    data = client_socket.recv(1024).decode("utf-8").strip()
    parts = data.split()
    response = ""

    if parts[0] == "PUT":
        key = parts[1]
        value = ' '.join(parts[2:])
        kv_store[key] = value
        response = "!200"
    elif parts[0] == "GET":
        key = parts[1]
        if key in kv_store:
            response = f"!200 {kv_store[key]}"
        else:
            response = "!400"
    elif parts[0] == "DEL":
        key = parts[1]
        if key in kv_store:
            del kv_store[key]
        response = "!200"
    else:
        response = "!400"

    client_socket.send(response.encode("utf-8"))
    client_socket.close()