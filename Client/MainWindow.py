import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication, QPushButton)


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def __loadKeys(self):
        return ''
        # Implementation of loading keys from server

    def generateKeys(self):
        return 0
        # Implementation of request to generate keys (return (public, private))

    def initUI(self):
        public_key_lbl = QLabel('Your public:')
        private_key_lbl = QLabel('Your private:')
        guide = QLabel('You can use next functions:')
        gen_keys_btn = QPushButton('Generate keys', self)
        key_swap_btn = QPushButton('Diffie-Hellman', self)
        create_ds_btn = QPushButton('Create digital signature', self)
        psec2_btn = QPushButton('Send message using PSEK-KEM algorythm', self)

        public_key = QLineEdit()
        private_key = QLineEdit()
        public_key.setText(self)



        public_key.setReadOnly(True)
        private_key.setReadOnly(True)

        public_key.setToolTip('Generated public key. If empty - generate keys!')
        private_key.setToolTip('Generated private key. If empty - generate keys!')

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(public_key_lbl, 1, 0)
        grid.addWidget(public_key, 1, 1, 1, 5)

        grid.addWidget(private_key_lbl, 2, 0)
        grid.addWidget(private_key, 2, 1, 1, 5)

        grid.addWidget(guide, 3, 0, 1, 2)

        grid.addWidget(gen_keys_btn, 4, 0)
        grid.addWidget(key_swap_btn, 4, 1)
        grid.addWidget(create_ds_btn, 4, 2)
        grid.addWidget(psec2_btn, 5, 0, 1, 3)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Elliptic cryptor')
        self.show()


