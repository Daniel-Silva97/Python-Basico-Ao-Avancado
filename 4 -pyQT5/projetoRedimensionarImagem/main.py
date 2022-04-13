"""
Comando para converter o arquivo *.ui para *.py
pyuic5 arquivo.ui -o arquivo.py
"""

import sys
from Interface.design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class Redimensiona(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnChooseFile.clicked.connect(self.abrirImagem)
        self.btnRedimensionar.clicked.connect(self.redimensionar)
        self.btnSalvar.clicked.connect(self.salvar)

    def abrirImagem(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir Imagem',
            r'C:\Users\user\Pictures'
        )
        self.inputOpenFile.setText(imagem)
        self.originalImagem = QPixmap(imagem)
        self.labelImage.setPixmap(self.originalImagem)
        self.inputLargura.setText(str(self.originalImagem.width()))
        self.inputAltura.setText(str(self.originalImagem.height()))

    def redimensionar(self):
        largura = int(self.inputLargura.text())
        self.novaImagem = self.originalImagem.scaledToWidth(largura)
        self.labelImage.setPixmap(self.novaImagem)
        self.inputLargura.setText(str(self.novaImagem.width()))
        self.inputAltura.setText(str(self.novaImagem.height()))

    def salvar(self):
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar Imagem',
            r'C:\Users\user\Desktop'
        )
        self.novaImagem.save(imagem, 'PNG')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = Redimensiona()
    app.show()
    qt.exec_()
