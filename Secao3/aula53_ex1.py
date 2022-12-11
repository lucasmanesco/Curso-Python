"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Informe um número: ')

try:
    n = int(numero)
    if n % 2 == 0:
        print(f'O número informado ({n}) é par.')
    else:
        print(f'O número informado ({n}) é ímpar.')
except:
    print('O valor informado não é um número inteiro.')
