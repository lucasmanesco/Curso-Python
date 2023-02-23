"""
List comprehension em Python
List comprehension é uma forma rápida para criar listas
a partir de iteráveis.
"""

print(list(range(10)))

lista1 = []
for numero in range(10):
    lista1.append(numero)
print(lista1)

lista2 =[(numero * 2) for numero in range(10)]
print(lista2)
