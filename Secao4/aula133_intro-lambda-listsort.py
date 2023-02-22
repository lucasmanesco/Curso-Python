"""
Função Lambda em Python
A função lambda é uma função como qualquer
outra em Python. Porém, são funções anônima
que contém apenas uma linha. Ou seja, tudo 
deve ser contido dentro de uma única expressão.
"""

# lista = [4, 32, 1, 34, 5, 6, 21]
# lista.sort() # reverse=True
# # sorted(lista) - shallow copy
# # print(lista)

lista = [
    {'nome': 'Lucas', 'sobrenome': 'Manesco'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# def ordena(item):
#     return item['nome']

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)
