"""
PyQT é um toolkit desenvolvido em C++ utilizado por vários programas para criação
de aplicações GUI (Interface Gráfica). Também inclui diversas funcionalidades
como: acesso a base de dados, threads, comunicação de rede, etc...

pip install pyqt5
"""
import sys  # Para inicializar
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtWidgets import QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        self.botton = QPushButton('Texto do botão')
        self.botton.setStyleSheet('font-size: 40px;')
        self.botton.clicked.connect(self.acaoBotao)
        self.grid.addWidget(self.botton, 0, 0, 1, 1)

        self.setCentralWidget(self.cw)

    def acaoBotao(self):
        print("Olá Mundo!")


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
