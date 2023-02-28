# Exercícios

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
print(*produtos, sep='\n')
print()

# Aumente os preços dos produtos a seguir em 10%
# Gere novos produtos por deep copy

import copy
novos_produtos = copy.deepcopy(produtos)
i = 0
for preco in novos_produtos:
    novos_produtos[i]['preco'] = round(novos_produtos[i]['preco'] * 1.1, 2)
    i += 1
print(*novos_produtos, sep='\n')
print()

# Ordene os produtos por nome decrescente
# Gere produtos_ordenados_por_nome por deep copy

produtos_ordenados_por_nome = sorted(
    novos_produtos,
    key=lambda x: x['nome'],
    reverse=True)

print(*produtos_ordenados_por_nome, sep='\n')
print()

# Ordene os produtos por preço crescente
# Gere produtos_ordenados_por_preco por deep copy

produtos_ordenados_por_preco = sorted(
    novos_produtos,
    key=lambda y: y['preco'])

print(*produtos_ordenados_por_preco, sep='\n')
print()
