"""
Gerador de CPFs
"""
import random

while True:

    # Gerando 9 dígitos aleatórios
    nove_dig = ''
    for i in range(9):
        nove_dig += str(random.randint(0,9))

    # Cálculo primeiro dígito
    c1 = 10
    soma1 = 0
    r1 = 0
    for dig1 in nove_dig[:9]:
        m2 = int(dig1) * c1
        soma1 += m2
        c1 -= 1
    m3 = soma1 * 10
    r1 = m3 % 11
    if r1 > 9:
        r1 = 0
    else:
        r1 = r1

    # Cálculo segundo dígito
    c2 = 11
    soma2 = 0
    r2 = 0
    for dig2 in (nove_dig[:9]+str(r1)):
        m4 = int(dig2) * c2
        soma2 += m4
        c2 -= 1
    m5 = soma2 * 10
    r2 = m5 % 11
    if r2 > 9:
        r2 = 0
    else:
        r2 = r2

    print(f'CPF gerado: {nove_dig + str(r1) + str(r2)}')

    # Deseja continuar?
    print('Deseja gerar outro CPF?')
    opcao = input('[S]im / [N]ão: ')
    if opcao.upper() == 'S':
        continue
    else:
        break
