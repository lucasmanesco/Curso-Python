"""
CPF: 746.824.890-70
Cálculo do primeiro dígito do CPF
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma 
contagem regressiva começando de 10
Ex.:  746.824.890-70
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0
Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10:
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
-------------------------------------------------------------------------
Cálculo do segundo dígito do CPF
Colete a soma dos 9 primeiro dígitos do CPF,
MAIS O PRIMEIRO DÍGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70
   11  10  9  8  7  6  5  4  3  2
*  7   4   6  8  2  4  8  9  0  7 <-- PRIMEIRO DÍGITO
   77  40  54 64 14 24 40 36 0  14
Somar todos os resultados:
77+40+54+64+14+24+40+360+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""

while True:
    cpf = input('Digite o CPF (somente números): ')

# Verificando input
    if cpf.isdigit() and len(cpf) == 11:
        cpf_str = str(cpf)
    else:
        print('Formato incorreto. Digite somente valores númericos.')
        continue

# Cálculo primeiro dígito
    c1 = 10
    soma1 = 0
    for dig1 in cpf_str[:9]:
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
    for dig2 in (cpf_str[:9]+str(r1)):
        m4 = int(dig2) * c2
        soma2 += m4
        c2 -= 1
    m5 = soma2 * 10
    r2 = m5 % 11
    if r2 > 9:
        r2 = 0
    else:
        r2 = r2

# Validando CPF
    if str(r1) == cpf_str[9] and str(r2) == cpf_str[10]:
        print('CPF válido.')
    else:
        print('CPF inválido.')

# Deseja continuar?
    print('Deseja verificar outro CPF?')
    opcao = input('[S]im / [N]ão: ')
    if opcao.upper() == 'S':
        continue
    else:
        break
