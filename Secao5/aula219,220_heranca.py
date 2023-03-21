# Herança simples - Relações entre classes
# Associação - usa;
# Agregação - tem;
# Composição - é dono de;
# Herança - é um.

# Herança ou Composição

# Classe principal (Pessoa)
#     -> super class, base class, parent class
# Classes filhas (Cliente)
#     -> sub class, child class, derived class
# MRO - Method Resolution Order


# toda classe herda (object)
class Pessoa:
    cpf = '123.456.789.10'

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)


class Cliente(Pessoa):
    ...


class Aluno(Pessoa):
    ...


c1 = Cliente('Lucas', 'Manesco')
c1.falar_nome_classe()
a1 = Aluno('José', 'Nivaldo')
a1.falar_nome_classe()
print(a1.cpf, c1.cpf)
