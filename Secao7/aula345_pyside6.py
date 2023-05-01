# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window -> setCentralWidget)
#     -> CentralWidget (central_widget -> setLayout)
#         -> Layout (layout)
#             -> Widget 1 (botao1)
#             -> Widget 2 (botao2)
#             -> Widget 3 (Botao3)
#     -> show
# -> exec

import sys

from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QWidget)


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Estrutura
        self.central_widget = QWidget()
        self.grid_layout = QGridLayout()

        # Configurando
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Minha Janela')
        self.central_widget.setLayout(self.grid_layout)

        # Botões
        self.botao1 = self.make_button('Texto do Botão 01')
        self.botao2 = self.make_button('Texto do Botão 02')
        self.botao3 = self.make_button('Texto do Botão 03')

        # Adicionando Widgets
        self.grid_layout.addWidget(self.botao1, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.botao2, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.botao3, 3, 1, 1, 2)

        # Status Bar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Mostrar mensagem na barra')

        # Criando Menu Bar
        self.menu = self.menuBar()
        self.menu1 = self.menu.addMenu('Menu1')

        # Actions Button
        self.botao1.clicked.connect(self.acao2_marcada)

        # Actions Menu
        self.acao1 = self.menu1.addAction('Ação1')
        self.acao1.triggered.connect(self.muda_mensagem_statusbar)
        self.acao2 = self.menu1.addAction('Ação2')
        self.acao2.setCheckable(True)
        self.acao2.toggled.connect(self.acao2_marcada)
        self.acao2.hovered.connect(self.acao2_marcada)

    @Slot()
    def muda_mensagem_statusbar(self):
        self.status_bar.showMessage('Meu slot foi executado!')

    @Slot()
    def acao2_marcada(self):
        print('Está marcado?', self.acao2.isChecked())

    def make_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet('font-size: 60px; color: blue')
        return btn


if __name__ == '__main__':
    app = QApplication(sys.argv)
    self = MyWindow()
    self.show()
    app.exec()
