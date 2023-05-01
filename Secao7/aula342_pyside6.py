# QApplication e QPushButton de PySide6.Widgets
# QApplication -> O widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6

# QWidget e QLayout de PySide6.QtWidgets
# QWidget -> Genérico
# QLayout -> Um widget de layout que recebe outros widgets

import sys

from PySide6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget

app = QApplication(sys.argv)

botao1 = QPushButton('Texto do Botão 01')
botao1.setStyleSheet('font-size: 60px; color: blue')

botao2 = QPushButton('Texto do Botão 02')
botao2.setStyleSheet('font-size: 40px; color: green')

botao3 = QPushButton('Texto do Botão 03')
botao3.setStyleSheet('font-size: 50px; color: red')

central_widget = QWidget()

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

central_widget.show()

app.exec()  # Loop da aplicação
