# Métodos de classe + factories (fábricas)
# # São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, recebemos a própria classe.


class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_anonimo(cls, idade):
        return cls('Anônima', idade)


Pessoa.metodo_de_classe()
print(Pessoa.ano)

p1 = Pessoa('Lucas', 28)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa.criar_anonimo(23)

print(p2.nome, p2.idade)
