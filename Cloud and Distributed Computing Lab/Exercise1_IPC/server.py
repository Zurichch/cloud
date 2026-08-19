# Run this first: python server.py
import socket
import pickle
from data_object import DataObject

HOST = '127.0.0.1'
PORT = 8000

# Create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"<SERVER> Listening on {HOST}:{PORT}...")

conn, addr = server_socket.accept()
print(f"<SERVER> Connected by {addr}")

while True:
    raw_data = conn.recv(1024) # Recceive the raw data

    data = pickle.loads(raw_data) # Could be of type DataObject | str

    if isinstance(data, str):
        conn.send("Connection Terminated...".encode())
        conn.close()
        print("<SERVER> Connection Terminated...")
        break

    print(f"<SERVER> Received: {data.values}")
    # Compute the sum of values
    total = str(sum(data.values))

    conn.send(total.encode())

server_socket.close()
