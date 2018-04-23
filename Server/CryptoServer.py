from Server.UserConnection import Connection
from socket import socket
import sqlite3
import threading


connections_pull = [[]]
connections = connections_pull[0]


def SaveKey(conn: socket, addr, username):
    print('SaveKey service started')
    key = conn.recv(1024).decode(encoding='utf-8').split(' ')

    print(key)
    dbconn = sqlite3.connect('ServerStorage.db')
    cur = dbconn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cur.fetchall())

    cur.execute("insert or replace into OPEN_KEYS values(?, ?, ?)", [(username, int(key[0]), int(key[1]))])
    # cursor = dbconn.cursor()


def DiffieHellman():
    return 0


def PSEC_KEM():
    return 0


services = {'SAVE_KEY': SaveKey, 'DIFFIE-HELLMAN': DiffieHellman, 'SEND_MESSAGE': PSEC_KEM}


def DispatchServer(conn: socket, addr, username):
    print('Dispatch connected:', addr)
    conn.send(b'OK')
    service = conn.recv(1024)
    print(service)
    for s in services.keys():
        if service.decode(encoding='utf-8') == s:
            conn.send(bytes(s, 'utf-8'))
            threading.Thread(target=services[s], args=(conn, addr, username)).start()
            break
    if conn is not None:
        conn.send(b'No such service')
        conn.close()


def AcceptServer(sock: socket, command):
    try:
        while command[0] != 'exit':
            print('Accept')
            conn, addr = sock.accept()
            username = conn.recv(1024).decode(encoding='utf-8')
            connections.append(Connection(conn, addr, username))
            print('Client connected:\n\taddress: ', addr, '\n\tUsername: ', username)
            threading.Thread(target=DispatchServer, args=(conn, addr, username)).start()
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
    sock.bind(('', 9090))
    print('listen')
    sock.listen(1)
    accept_serv = threading.Thread(target=AcceptServer, args=(sock, cmd))

    accept_serv.setDaemon(True)

    accept_serv.start()
    CommandCycle(sock, cmd)
    accept_serv.join()



