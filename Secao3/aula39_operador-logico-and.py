"""
Operadores Lógicos
and (e) or (ou) not (não)
and - todas as condições precisam ser verdadeiras
Se qualquer expressão for falsa, a expressão inteira será avaliada como falsa.
falsy = 0 / 0.0 / '' / False
None - 'não valor'
"""

entrada = input('[E]ntrar / [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
print(True and True and True)
print(True and False and True)
print(True and 0 and True)
print(False and True)
