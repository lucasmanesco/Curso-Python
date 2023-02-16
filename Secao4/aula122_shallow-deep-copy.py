"""
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna um cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave especificada (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
"""
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]  # shallow copy não aprofunda nos níveis (imutáveis) apenas linka
}

d2 = d1.copy()  # shallow copy
# d2 = copy.deepcopy(d1)  # deepcopy

d2['c1'] = 1000

d2['l1'][1] = 9999999

print(d1)
print(d2)