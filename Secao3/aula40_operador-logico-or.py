"""
Operadores Lógicos
and (e) or (ou) not (não)
or - qualquer condição veradeira avalia toda a expressão como verdadeira.
Se qualquer expressão for verdadeira, a expressão inteira será avaliada como verdadeira.
falsy = 0 / 0.0 / '' / False
None - 'não valor'
"""

entrada = input('[E]ntrar / [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
print(True or False)
print(0 or False or 0 or 'abc' or True)
