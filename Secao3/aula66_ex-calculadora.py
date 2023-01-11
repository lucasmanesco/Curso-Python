"""Calculadora com while"""

while True:


    n1 = input('Informe o primeiro valor: ')
    n2 = input('Informe o segundo valor: ')

    try:
        fn1 = float(n1)
        fn2 = float(n2)
    except:
        print('Digite valores numéricos.')


    operacao = input('Qual operação deseja realizar?\nA - Adição\nS - Subtração\nM - Multiplicação\nD - Divisão\n->')

    if operacao.upper() == 'A':
        print(f'Resultado = {fn1 + fn2}')
    elif operacao.upper() == 'S':
        print(f'Resultado = {fn1 - fn2}')
    elif operacao.upper() == 'M':
        print(f'Resultado = {fn1 * fn2}')
    elif operacao.upper() == 'D':
        print(f'Resultado = {fn1 / fn2}')
    else:
        print('Você não selecionou nenhuma operação.')

    opcao = input('Deseja fazer outro cálculo? (S)/(N)').upper().startswith('S')

    if opcao is True:
        break
