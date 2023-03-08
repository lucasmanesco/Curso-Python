"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

Ex.:
l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]

Resultado:
l3 = [2, 4, 6, 8]
"""

resultado = []

def soma_listas(*args):
    for x, y in zip(*args):
        resultado.append(x + y)
    return resultado


l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]

print(soma_listas(l1, l2))
