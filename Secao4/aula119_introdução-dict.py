"""
Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo par "chave/valor"
Chaves podem ser consideradas como índice que vimos na lista e podem ser imutáveis,
como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro dicionário.
Usamos as chaves - {} ou a classe dict para criar dicionários.
Imutáveis: str, int, float, bool, tuple
Mutável: dict, list
pessoa = {
    'nome' : 'Lucas',
    'sobrenome' : 'Manesco',
    'idade' : 28,
    'altura' : 1.8,
    'endereço' : [
        {'rua': 'tal tal', 'numero': 123}
        {'rua': 'outra tal', 'numero': 123}
    ]
}
"""

pessoa = {
    'nome' : 'Lucas',
    'sobrenome' : 'Manesco',
    'idade' : 28,
    'altura' : 1.8,
    'endereço' : [
        {'rua': 'Josè Zappi', 'numero': 363},
        {'rua': 'Avenida dos Estados', 'numero': 4826}
    ]
}

# print(pessoa, type(pessoa))

print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])
