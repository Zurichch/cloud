# Run after server.py is running (start multiple times to see coordination): python client.py
import socket
import time

HOST = 'localhost'
PORT = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("[Client] Connected to coordinator")
    s.sendall("REQUEST_CS".encode())
    print("[Client] Requested access to CS")

    msg = s.recv(1024).decode()
    if msg == "GRANT_CS":
        print("[Client] Entering critical section")
        time.sleep(3)  # simulate doing work in Critical Section

        print("[Client] Leaving critical section")
        s.sendall("RELEASE_CS".encode())
