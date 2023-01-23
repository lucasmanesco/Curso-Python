"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [1, 2, 3, 4]    # Create
print(lista)            # Read
lista[2] = 30           # Update
del lista[2]            # Delete

print(lista)

lista.append(5)         # adicionar no final
print(lista)

lista.pop()             # remover o último
print(lista)

lista.pop(1)             # remover um item específico
print(lista)