import socket

i = 0

while i < 100:
    sock = socket.socket()
    sock.connect(('localhost', 2000))

    data = sock.recv(1024)
    sock.close()

    print(data)
    i += 1

