"""
Exercício com Classes
1 - Crie uma classe Carro (Nome)
2 - Crie uma Classe Motor (Nome)
3 - Crie uma Classe Fabricante (Nome)
4 - Faça a ligação entre Carro tem Motor
Obs.: Um motor pode ser de vários carros
5 - Faça a ligação entre Carro e Fabricante
Obs.: Um fabricante pode fabricar vários carros
Exiba o nome do carro, motor e fabricante na tela
"""


class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    # motor getter
    @property
    def motor(self):
        return self._motor

    # motor setter
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    # fabricante getter
    @property
    def fabricante(self):
        return self._fabricante

    # fabricante setter
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0
print(fusca.fabricante.nome, fusca.nome, fusca.motor.nome)

golf = Carro('Golf')
motor_2_0 = Motor('2.0')
golf.fabricante = volkswagen
golf.motor = motor_2_0
print(golf.fabricante.nome, golf.nome, golf.motor.nome)

uno = Carro('Uno')
fiat = Fabricante('Fiat')
uno.fabricante = fiat
uno.motor = motor_1_0
print(uno.fabricante.nome, uno.nome, uno.motor.nome)
