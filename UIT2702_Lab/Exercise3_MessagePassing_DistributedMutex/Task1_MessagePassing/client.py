# Run after server.py is running (can start multiple clients): python client.py
import socket
import threading

HOST = 'localhost'
PORT = 8000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("<CONNECTED> to server.")

# Define a thread to simultaneously handle sending and receiving messages
def receive_messages(client):
    data = client.recv(1024).decode()
    print(f"<client> Received from Server {data}")

threading.Thread(target = receive_messages, args = (client,)).start()

while True:
    msg = input("Enter message to send to server: ")
    client.send(msg.encode())

    if msg.lower() == "bye":
        break

client.close()
