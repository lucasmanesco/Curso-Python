# Atributos de classe

# ANO_ATUAL = 2022


class Pessoa:
    ano_atual = 2022  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade


p1 = Pessoa('João', 32)
p2 = Pessoa('Helena', 12)

print(Pessoa.ano_atual)

# Pessoa.ano_atual = 1

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
