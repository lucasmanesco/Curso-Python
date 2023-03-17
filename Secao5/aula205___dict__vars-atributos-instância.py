# __ dict__ e vars para atributos de instância


class Pessoa:
    ano_atual = 2022  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade


p1 = Pessoa('João', 32)
dados = {'nome': 'Maria', 'idade': 20}
p2 = Pessoa(**dados)
# p1.nome = 'EITA'
# del p1.nome
# print(p1.idade)

print(p1.__dict__)
print(vars(p1))

p1.__dict__['outra'] = 'coisa'
print(p1.outra)
