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

# Montando Estrutura
app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
layout = QGridLayout()

# Confiugurando
window.setCentralWidget(central_widget)
window.setWindowTitle('Minha Janela')
central_widget.setLayout(layout)

# Criando botões (Widgets)
botao1 = QPushButton('Texto do Botão 01')
botao1.setStyleSheet('font-size: 60px; color: blue')
botao2 = QPushButton('Texto do Botão 02')
botao2.setStyleSheet('font-size: 40px; color: green')
botao3 = QPushButton('Texto do Botão 03')
botao3.setStyleSheet('font-size: 50px; color: red')

# Adicionando Widgets
layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

# Criando Status Bar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')

# Criando Menu Bar
menu = window.menuBar()
menu1 = menu.addMenu('Menu1')


# Criando Ação do Menu 1
@Slot()
def slot1(status_bar):
    def inner():
        status_bar.showMessage('Meu slot foi executado!')
    return inner


@Slot()
def slot2(checked):
    print('Está marcado?', checked)


@Slot()
def slot3(action):
    def inner():
        slot2(action.isChecked())
    return inner


acao1 = menu1.addAction('Ação1')
acao1.triggered.connect(slot1(status_bar))

acao2 = menu1.addAction('Ação2')
acao2.setCheckable(True)
acao2.toggled.connect(slot2)
acao2.hovered.connect(slot3(acao2))

# Criando Ação do Botão
botao1.clicked.connect(slot3(acao2))

# Executando app (Loop da aplicação)
window.show()
app.exec()
