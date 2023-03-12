"""
Funcções recursivas e recursividade
- funções que podem se chamar de volta
- úteis para dividir problemas grandes em partes menores
Toda função recursiva deve ter:
- um problema que possa ser dividido em partes menores
- um caso recursivo que resolve o pequeno problema
- um caso base que para a recursão
- fatorial - n! = 5 *4 *3 *2 *1 = 120
"""


def recursiva(start=0, end=10):
    # Caso base
    if start >= end:
        return end

    print(start, end)

    # Caso recursivo: contar até o final
    start += 1
    return recursiva(start, end)


print(recursiva())
