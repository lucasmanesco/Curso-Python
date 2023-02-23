"""
List comprehension em Python
List comprehension é uma forma rápida para criar listas
a partir de iteráveis.
"""

#print(list(range(10)))

lista1 = []
for numero in range(10):
    lista1.append(numero)
#print(lista1)

lista2 =[(numero * 2) for numero in range(10)]
#print(lista2)

# Mapeamento de dados em list comprehension:
# Transformar uma lista em nova lista 
# transformando os dados e mantendo o tamanho da lista.
produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30}
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    ]
#print(novos_produtos)
print(*novos_produtos, sep='\n')
