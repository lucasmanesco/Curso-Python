"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4
lista = [10, 20, 30, 40, 50]
print(lista)

lista.append('Lucas')
print(lista)

nome = lista.pop()
lista.append(100)
print(lista)

del lista [-1]
print(lista)

# lista.clear()
# print(lista)

lista.insert(0, 5)
print(lista)