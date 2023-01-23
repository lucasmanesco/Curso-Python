"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""

#        -54321
#         01234
string = 'ABCDE'  # 5 caracteres (len)

#          0         1       2         3      4    5   6   7   8
lista = ['Lucas', 'Amora', 'Mike', 'Jéssica', 28, 1.5, 6, 26, True]

print(lista)
print(lista[2])

print(lista[2].upper(), type(lista[2]))

lista[0] = 'Manesco'

print(lista)