
class Connection:

    def __init__(self, conn, addr, name):
        self.__connection = conn
        self.__address = addr
        self.__username = name

    @property
    def conn(self):
        return self.__connection

    @property
    def addr(self):
        return self.__address

    @property
    def username(self):
        return self.__username
