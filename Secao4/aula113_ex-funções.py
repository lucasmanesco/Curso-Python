# Exercício com funções

"""
Crie uma função que multiplica todos os argumentos não nomeados recebidos.
Retorne o total para uma variável e mostre o valor da variável.
"""


def multiply(*args):
    total = 1
    for num in args:
        total *= num
    return total


print(multiply(1, 2, 3, 4, 5))


"""Crie uma função que fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar."""


def odd_even(num):
    if num % 2 == 0:
        message = f'The number {num} is odd.'
    message = f'The number {num} is even.'
    return message


print(odd_even(5))