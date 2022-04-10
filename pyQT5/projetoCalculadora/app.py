import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLineEdit, QSizePolicy


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Calculadora do Daniel")  # Mudando o título da Janela
        self.setFixedSize(400, 400)  # Definindo um tamanho fixo para Janela
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)
        # Criando um display de texto
        self.display = QLineEdit()
        self.grid.addWidget(self.display, 0, 0, 1, 5)
        # Não permite digitar no display
        self.display.setDisabled(True)
        self.display.setStyleSheet('*{background: #363636; font-size: 30px; color: #FFFAFA;}')
        self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

        # Adicionando os botões
        self.addButtons(QPushButton('7'), 1, 0, 1, 1, None,
                        'background: #A9A9A9; color: #fff; font-weight: 700; color: #FFFAFA;')
        self.addButtons(QPushButton('8'), 1, 1, 1, 1, None,
                        'background: #A9A9A9; color: #fff; font-weight: 700; color: #FFFAFA;')
        self.addButtons(QPushButton('9'), 1, 2, 1, 1, None,
                        'background: #A9A9A9; color: #fff; font-weight: 700; color: #FFFAFA;')
        self.addButtons(QPushButton('+'), 1, 3, 1, 1, None,
                        'background: #4F4F4F; color: #fff; font-weight: 700; color: #FFFAFA;')
        self.addButtons(
            QPushButton('C'), 1, 4, 1, 1,
            lambda: self.display.setText(''),
            'background: #4F4F4F; color: #fff; font-weight: 700; color: #FFFAFA;'
        )

        self.addButtons(QPushButton('4'), 2, 0, 1, 1, None,
                        'background: #A9A9A9; color: #fff; font-weight: 700; color: #FFFAFA;'
                        )
        self.addButtons(QPushButton('5'), 2, 1, 1, 1, None,
                        'background: #A9A9A9; color: #fff; font-weight: 700; color: #FFFAFA;'
                        )
        self.addButtons(QPushButton('6'), 2, 2, 1, 1, None,
                        'background: #A9A9A9; color: #fff; font-weight: 700; color: #FFFAFA;'
                        )
        self.addButtons(QPushButton('-'), 2, 3, 1, 1, None,
                        'background: #4F4F4F; color: #fff; font-weight: 700; color: #FFFAFA;'
                        )
        self.addButtons(
            QPushButton('<-'), 2, 4, 1, 1,
            lambda: self.display.setText(
                self.display.text()[:-1]
            ),
            'background: #4F4F4F; color: #fff; font-weight: 700'
        )

        self.addButtons(QPushButton('1'), 3, 0, 1, 1, None,
                        'background: #A9A9A9; color: #fff; font-weight: 700; color: #FFFAFA;'
                        )
        self.addButtons(QPushButton('2'), 3, 1, 1, 1, None,
                        'background: #A9A9A9; color: #fff; font-weight: 700; color: #FFFAFA;'
                        )
        self.addButtons(QPushButton('3'), 3, 2, 1, 1, None,
                        'background: #A9A9A9; color: #fff; font-weight: 700; color: #FFFAFA;'
                        )
        self.addButtons(QPushButton('/'), 3, 3, 1, 1, None,
                        'background: #4F4F4F; color: #fff; font-weight: 700; color: #FFFAFA;'
                        )
        self.addButtons(QPushButton(''), 3, 4, 1, 1, None,
                        'background: #A9A9A9; color: #fff; font-weight: 700; color: #FFFAFA;'
                        )

        self.addButtons(QPushButton('.'), 4, 0, 1, 1, None,
                        'background: #A9A9A9; color: #fff; font-weight: 700; color: #FFFAFA;'
                        )
        self.addButtons(QPushButton('0'), 4, 1, 1, 1, None,
                        'background: #A9A9A9; color: #fff; font-weight: 700; color: #FFFAFA;'
                        )
        self.addButtons(QPushButton(''), 4, 2, 1, 1, None,
                        'background: #A9A9A9; color: #fff; font-weight: 700; color: #FFFAFA;'
                        )
        self.addButtons(QPushButton('*'), 4, 3, 1, 1, None,
                        'background: #4F4F4F; color: #fff; font-weight: 700; color: #FFFAFA;'
                        )
        self.addButtons(
            QPushButton('='), 4, 4, 1, 1,
            self.buttonEqual,
            'background: #4682B4; color: #fff; font-weight: 700; color: #FFFAFA;'
        )

        self.setCentralWidget(self.cw)

    # Função para adicionar os botões
    def addButtons(self, button, row, col, rowspan, colspan, funcao=None, style=None):
        self.grid.addWidget(button, row, col, rowspan, colspan)

        if not funcao:
            # Função para quando clicar no botão, adicionar no display o número que exibe no botão clicado
            button.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + button.text()
                )
            )
        else:
            button.clicked.connect(funcao)

        if style:
            button.setStyleSheet(style)

        # Size policy para distribuir os botões em tela
        button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

    def buttonEqual(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception as e:
            self.display.setText('Conta Inválida!')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()
