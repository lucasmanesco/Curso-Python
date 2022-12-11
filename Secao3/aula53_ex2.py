"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex:
Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23.
"""

hora = int(input('Olá! Que hora do dia é agora? '))

dia = hora >= 0 and hora <= 11
tarde = hora >= 12 and hora <= 17
noite = hora >= 18 and hora <= 23

if dia:
    print('Bom dia!')
elif tarde:
    print('Boa tarde!')
elif noite:
    print('Boa noite!')
