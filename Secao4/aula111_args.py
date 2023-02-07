"""
args - argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te do desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)

def soma(*args):
    total = 0  # acumulador
    for numero in args:
        total += numero
    return total

soma1 = soma(1, 2, 3)
print(soma1)

soma2 = soma(4, 5, 6)
print(soma2)

soma3 = soma(10, 20, 30, 40, 50, 60)
print(soma3)

print(sum(10, 20, 30, 40, 50, 60))
