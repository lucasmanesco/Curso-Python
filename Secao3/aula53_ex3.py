"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos
escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é nomrla"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Olá! Digite o seu nome: ')

curto = len(nome) <= 4
normal = len(nome) >= 5 and len(nome) <= 6
grande = len(nome) >= 6

if curto:
    print('Seu nome é curto!')
elif normal:
    print('Seu nome é normal!')
elif grande:
    print('Seu nome é grande!')
