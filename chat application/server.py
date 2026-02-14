import socket
import threading

host = "0.0.0.0"
port = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []

print("Server started... Waiting for users")

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            clients.remove(client)
            client.close()
            break

while True:
    client, address = server.accept()
    print("Connected with", address)

    clients.append(client)

    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()
