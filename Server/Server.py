import threading
import sqlite3
from socket import socket

import threading

services = [b'SAVE_KEY', b'DIFFIE-HELLMAN',  b'SEND_MESSAGE']


def DispatchServer(conn: socket, addr):
    print('Dispatch')
    print('connected:', addr)
    print('conn:\n', conn)


    conn.send(b'Connected')
    service = conn.recv(1024)
    print(service)
    for s in services:
        if service == s:
            conn.send(s)
            conn.close()
            conn = None
            break
    if conn is not None:
        conn.send(b'No such service')
        conn.close()


def SaveKey(conn: socket, addr):
    key = conn.recv(1024).decode(encoding='utf-8').split(' ')
    dbconn = sqlite3.connect('ServerStorage.db')
    dbconn.execute('insert or replace into OPEN_KEYS values()')
    cursor = dbconn.cursor()
    return 0


def DiffieHellman():
    return 0

def PSEC_KEM():
    return 0


def AcceptServer(sock: socket, command):
    try:
        while command[0] != 'exit':
            print('Accept')
            conn, addr = sock.accept()
            print('Client connected:\n\taddress: %s' % addr[1])
            threading.Thread(target=DispatchServer, args=(conn, addr)).start()
    except Exception as ex:
        print('Exception %s' % ex.__str__())
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
    sock.bind(('', 9099))
    print('listen')
    sock.listen(1)
    accept_serv = threading.Thread(target=AcceptServer, args=(sock, cmd))

    accept_serv.setDaemon(True)

    accept_serv.start()
    CommandCycle(sock, cmd)
    accept_serv.join()



