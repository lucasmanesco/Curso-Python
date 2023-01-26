"""
Tipo tupla - lista mutável
"""

lista = ['Lucas', 'Jéssica', 'Mike', 'Amora']
lista[0] = 'Nelson'
print(lista)

nomes = tuple(lista)
nomes = list(lista)

tupla = (28, 26, 6, 1.5)
tupla1 = 1, 2, 3, 4

tupla[1] = 30  # 'tuple' object does not support item assignment