"""
Exercício
Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro.
"""


# def duplica(numero):
#     resultado = numero * 2
#     return resultado

# def triplica(numero):
#     resultado = numero * 3
#     return resultado

# def quadruplica(numero):
#     resultado = numero * 4
#     return resultado


def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        resultado = multiplicador * numero
        return resultado
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))