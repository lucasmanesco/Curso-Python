"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma (x, y, z):  # parâmetros
    print(f'{x=} y={y} z={z}', '|', 'x + y + z =', x + y + z)


print(soma)  # chama função

print(soma(1, 2, 3))  # executa função -> argumentos

soma(1, 2, z=5)
#soma(1, y=2, 5)  # todos os argumentos após o nomeado devem ser nomeados