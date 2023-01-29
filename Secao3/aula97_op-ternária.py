"""
Operação Ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""

condicao = 10 == 11
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)

digito = 9
novo_digito = digito if digito <= 9 else 0
print(novo_digito)
