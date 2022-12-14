"""
Iterando strings com while
"""

nome = input('Insira seu nome: ')

tamanho_nome = len(nome)
novo_nome = ''

i = 0
while i < tamanho_nome:
    novo_nome += '*' + nome[i]
    i += 1

print(novo_nome)
