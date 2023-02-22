# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
print(a, b)

pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'Manesco'
}
a, b = pessoa.values() # / items() / keys()
(a1, a2), (b1, b2) = pessoa.items()
print(a, b)
print(a1, a2, b1, b2)

for chave, valor in pessoa.items():
    print(chave, valor)

dados_pessoa = {
    'idade': 28,
    'altura': 1.75
}
pessoas_completa = {**pessoa, **dados_pessoa}
print(pessoas_completa)

# args e kwargs
# args (já vimos)
# kwargs keyword arguments (argumentos nomeados)


def mostro_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

        
mostro_argumentos_nomeados(nome='Lucas', qlq=123)

configuracoes = {
    'arg1' : 1,
    'arg2' : 2,
    'arg3' : 3,
    'arg4' : 4,
}
mostro_argumentos_nomeados(**configuracoes)

