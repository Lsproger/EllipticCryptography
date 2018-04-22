import socket

services = [b'SAVE_KEY', b'DIFFIE-HELLMAN',  b'SEND_MESSAGE']

try:
    sock = socket.socket()
    sock.connect(('localhost', 9099))
    data = sock.recv(1024)
    if data == b'Connected':
        i = 0
        print('Choose service')
        for s in services:
            print(i, ' -- ', s)
            i += 1
        service = services[int(input())]
        sock.send(service)
        answ = sock.recv(1024)
        print(answ)
    sock.send(b'')
    sock.close()
except Exception as ex:
    print('Exception:\n', ex.__str__())
    sock.close()


