"""
Exercício - Unir listas
Crie uma função zipper (como o zipper de roupas)
O trabalho dessa função será unir duas listas na ordem.
Use todos os valores da menor lista.
EX.:
c
Resultado:
[('Salvador', 'BA), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
"""

# from intertools import zip_longest
# print(list(zip_longest(l1, l2, fillvalue='Sem Cidade')))

def zipper(*args):
    return list(zip(*args))

    # intervalo = min(len(l1), len(l2))
    # return [(l1[i], l2[i]) for i in range(intervalo)]


cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

zipped = zipper(cidades, estados)
print(zipped)
