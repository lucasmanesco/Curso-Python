# QApplication e QPushButton de PySide6.Widgets
# QApplication -> O widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6

# QWidget e QLayout de PySide6.QtWidgets
# QWidget -> Genérico
# QLayout -> Um widget de layout que recebe outros widgets

import sys

from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

botao1 = QPushButton('Texto do Botão 01')
botao1.setStyleSheet('font-size: 60px; color: blue')
botao1.show()

botao2 = QPushButton('Texto do Botão 02')
botao2.setStyleSheet('font-size: 40px; color: green')
botao2.show()

app.exec()  # Loop da aplicação
