"""
enumerate - enumera iteráveis (índices)
"""

lista = ['Lucas', 'Jéssica', 'Amora', 'Mike']
lista.append('Nelson')

# lista_enumerada = enumerate(lista) , start=10

for item in enumerate(lista):
    print(item)

for item in enumerate(lista):
    i, nome = item
    print(i, nome)

# desempacotamento
for i, nome in enumerate(lista):
    print(i, nome)

for tupla_enumerada in enumerate(lista):
    print('FOR da tupla: ')
    for valor in tupla_enumerada:
        print(f'\t{valor}')
    