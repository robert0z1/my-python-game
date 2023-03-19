import socket
import threading

class ChatServer:
    def __init__(self):
        self.clients = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(("localhost", 5000))
        self.server_socket.listen(1)

    def broadcast(self, message):
        for client in self.clients:
            client.send(message.encode())

    def handle_client(self, client):
        while True:
            try:
                message = client.recv(1024).decode()
                self.broadcast(message)
            except:
                self.clients.remove(client)
                client.close()
                break

    def run(self):
        while True:
            client, address = self.server_socket.accept()
            self.clients.append(client)
            client_thread = threading.Thread(target=self.handle_client, args=(client,))
            client_thread.start()

if __name__ == "__main__":
    server = ChatServer()
    server.run()
ChatServer()
