"""Calculadora com while"""

while True:


    n1 = input('Informe o primeiro valor: ')
    n2 = input('Informe o segundo valor: ')

    numeros_validos = None

    try:
        fn1 = float(n1)
        fn2 = float(n2)
        numeros_validos = True
    except:
        numeros_validos = None
    
    if numeros_validos == None:
        print('Digite valores numéricos.')
        continue
    
    operacao = input('Qual operação deseja realizar?\nA - Adição\nS - Subtração\nM - Multiplicação\nD - Divisão\n->')

    operadores_validos = 'ASMD'

    if operacao.upper() not in operadores_validos.upper() or len(operacao) > 1:
        print('Operação inválida.')
        continue

    if operacao.upper() == 'A':
        print(f'Resultado = {fn1 + fn2}')
    elif operacao.upper() == 'S':
        print(f'Resultado = {fn1 - fn2}')
    elif operacao.upper() == 'M':
        print(f'Resultado = {fn1 * fn2}')
    elif operacao.upper() == 'D':
        print(f'Resultado = {fn1 / fn2}')

    opcao = input('Deseja fazer outro cálculo? (S)/(N)').upper().startswith('S')

    if opcao is not True:
        break
