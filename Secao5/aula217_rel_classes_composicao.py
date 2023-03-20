"""
Relação entre classes: associação, agregação e composição
Composição é uma especialização da agregação.
Mas nela, quando o objeto "pai" for apagado, todas as
referências dos objetos filhos também são apagadas.
* garbage collector
"""


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        # Endereco criado dentro de Cliente
        # quando apagar o Cliente, o Endereco apaga junto
        # garbage collector
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_endereco(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    # garbage collector
    def __del__(self):
        print('Apagando:', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    # garbage collector
    def __del__(self):
        print('Apagando:', self.rua, self.numero)


cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av. Brasil', 54)
cliente1.inserir_endereco('Av. França', 62)

endereco_externo = Endereco('Av. Itália', 78)
cliente1.inserir_endereco_externo(endereco_externo)
cliente1.listar_endereco()

del cliente1

print(endereco_externo.rua, endereco_externo.numero)
print(' ------ Aqui termina o código. ------ ')
