# Desempacotamento em chamadas de métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 'Eduarda']
tupla = 'Python', 'é', 'legal'

salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2          3
    ['Luiz', 'João', 'Eduarda', (0, 1, 2, 3, 4)],  # 2
]

print(*lista)
print(*string)
print(*tupla)

print(*salas, sep='\n')