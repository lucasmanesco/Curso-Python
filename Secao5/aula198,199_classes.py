"""
class - Classes são moldes para criar novos objetos
As classes geram novos objetos (instâncias) que
podem ter seus próprios atributos e métodos.
Os objetos geraod pela classe podem usar seus dados
internos para realizar várias ações.
Por convenção, usamos PascalCase para nomes de classe.
"""


# classe (objeto)
class Pessoa:
    # metodo p/ inicializar os atribudos da classe:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


# instância
p1 = Pessoa('Lucas', 'Manesco')
# p1.nome = 'Lucas'
# p1.sobrenome = 'Manesco'

# instância
p2 = Pessoa('Maria', 'Joana')
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'

print(p1)
print(p1.nome)
print(p1.sobrenome)
print(p2.nome)
print(p2.sobrenome)
