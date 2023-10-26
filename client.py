import socket

def send_request(host, port, request):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((host, port))
        client_socket.send(request.encode("utf-8"))
        response = client_socket.recv(1024).decode("utf-8")
        return response
    finally:
        client_socket.close()

load_balancer_host = "127.0.0.1"
load_balancer_port = 8888

while True:
    print("Options:")
    print("1. PUT")
    print("2. GET")
    print("3. DEL")
    print("4. Quit")
    choice = input("Enter choice: ")

    if choice == "1":
        key = input("Enter key: ")
        value = input("Enter value: ")
        request = f"PUT {key} {value}"
    elif choice == "2":
        key = input("Enter key: ")
        request = f"GET {key}"
    elif choice == "3":
        key = input("Enter key: ")
        request = f"DEL {key}"
    elif choice == "4":
        print("Exiting client.")
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
        continue

    response = send_request(load_balancer_host, load_balancer_port, request)
    print("Response:", response)
