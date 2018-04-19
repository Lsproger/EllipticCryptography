import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication, QPushButton, QInputDialog)
from Algorithms.Functions import generate_keys
from Client.KeySwapWindow import KeySwapWindow

class MainWindow(QWidget):

    def getx(self): return self.__addwin  # методы для чтения,

    def setx(self, value): self.__addwin = value  # записи

    def delx(self): del self.__addwin  # удаления свойства

    addwin = property(getx, setx, delx, "Свойство 'addwin'.")  # определение свойства
    # ---конец описания свойства

    __public_key = 0
    __private_key = 0
    __server_ip = '127.0.0.1'
    __connect_status = 'Not connected'

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.__private_key, self.__public_key = self.__loadKeys()

        server_ip_lbl = QLabel('Server ip:')
        connection = QLabel('Connection status:')

        public_key_lbl = QLabel('Your public:')
        private_key_lbl = QLabel('Your private:')
        guide = QLabel('You can use next functions:')

        gen_keys_btn = QPushButton('Generate keys', self)
        key_swap_btn = QPushButton('Diffie-Hellman', self)
        create_ds_btn = QPushButton('Create digital signature', self)
        psec2_btn = QPushButton('Send message using PSEK-KEM algorythm (One-time note)', self)

        self.public_key = QTextEdit(self.__public_key)
        self.private_key = QLineEdit(self.__private_key)
        self.server_ip_edit = QLineEdit(self.__server_ip)
        self.connection_status_lbl = QLabel(self.__connect_status)

        self.public_key.setReadOnly(False)
        self.private_key.setReadOnly(False)

        self.public_key.setToolTip('Generated public key. If empty - generate keys!')
        self.private_key.setToolTip('Generated private key. If empty - generate keys!')

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(server_ip_lbl, 0, 0)
        grid.addWidget(self.server_ip_edit, 0, 1, 1, 2)

        grid.addWidget(connection, 1, 0)
        grid.addWidget(self.connection_status_lbl, 1, 1, 1, 2)

        grid.addWidget(public_key_lbl, 2, 0)
        grid.addWidget(self.public_key, 2, 1, 1, 2)

        grid.addWidget(private_key_lbl, 3, 0)
        grid.addWidget(self.private_key, 3, 1, 1, 2)

        grid.addWidget(guide, 4, 0, 1, 2)

        grid.addWidget(gen_keys_btn, 5, 0)
        grid.addWidget(key_swap_btn, 5, 1)
        grid.addWidget(create_ds_btn, 5, 2)
        grid.addWidget(psec2_btn, 6, 0, 1, 3)

        self.setLayout(grid)

        gen_keys_btn.clicked.connect(self.__gen_keys_btn_clicked)
        key_swap_btn.clicked.connect(self.__key_swap_btn_clicked)

        self.setGeometry(300, 300, 650, 100)
        self.setWindowTitle('Elliptic cryptographer')
        self.show()

    def __loadKeys(self):
        return 'None', 'x:None<br>y:None'
        # Implementation of loading keys from server


    def __gen_keys_btn_clicked(self):
        # Check connection
        sender = self.sender()
        self.__private_key, self.__public_key = generate_keys()
        self.__update_lables()

    def __key_swap_btn_clicked(self):
        self.addwin = KeySwapWindow()

    def __update_lables(self):
        self.private_key.setText(str(self.__private_key))
        self.public_key.setText('x: %d <br> y: %d' % (self.__public_key.x, self.__public_key.y))
