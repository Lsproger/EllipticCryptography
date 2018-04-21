import threading
from socket import socket

import threading


def DispatchServer(conn, addr):
    print('Dispatch')
    print('connected:', addr)

        #data = conn.recv(1024)
        #if not data:
         #   break
    conn.send(b'Hello')

    conn.close()


def AcceptServer(sock, command):
    try:
        while command[0] != 'exit':
            print('cycle')
            conn, addr = sock.accept()
            threading.Thread(target=DispatchServer, args=(conn, addr)).start()
    finally:
        if sock:
            sock.close()
            print('Socket closed')
            raise SystemExit
    quit(1)


def CommandCycle(ssocket, command):
    while command[0] != 'exit':
        command[0] = input('Enter command:')
        if command[0] == 'exit':
            ssocket.close()
            quit(1)


if __name__ == '__main__':
    sock = socket()
    llist = [['work']]
    cmd = llist[0]
    x = 10
    print('Accept')
    sock.bind(('', 2000))
    print('listen')
    sock.listen(1)
    accept_serv = threading.Thread(target=AcceptServer, args=(sock, cmd))

    accept_serv.setDaemon(True)

    accept_serv.start()
    CommandCycle(sock, cmd)
    accept_serv.join()



