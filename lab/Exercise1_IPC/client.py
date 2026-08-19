# Run this after server.py is running: python client.py
import socket
import pickle
from data_object import DataObject

HOST = '127.0.0.1'
PORT = 8000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("<CLIENT> Connected to server.")

# Create the Data object
values = [1, 2, 3, 4, 5, 6, 7, 8]
obj = DataObject(values)

# Send the serialized object
raw_data = pickle.dumps(obj)
client_socket.send(raw_data)

# Receive the response
total_value = client_socket.recv(1024).decode()
print(f"<SERVER> Response from Server: {total_value}")

exit_msg = "exit"
raw_exit = pickle.dumps(exit_msg)
response = client_socket.send(raw_exit)
print(f"<SERVER> {response}")

client_socket.close()
