from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication, QPushButton)


class KeySwapWindow(QWidget):

    def __init__(self):
        super(KeySwapWindow, self).__init__()
        # запускаем метод рисующий виджеты окна

        self.initUI()

    def initUI(self):

        server_ip_lbl = QLabel('Server ip:')
        connection = QLabel('Connection status:')

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(server_ip_lbl, 0, 0)

        grid.addWidget(connection, 1, 0)

        self.setLayout(grid)

        self.setGeometry(300, 300, 650, 100)
        self.setWindowTitle('Diffie-Hellman key swap')
        self.show()



