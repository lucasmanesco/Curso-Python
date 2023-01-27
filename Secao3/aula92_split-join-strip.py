"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = 'Olha só, que coisa interessante!'

lista_palavras = frase.split()
print(lista_palavras)

lista_frases = frase.split(',')

for i, frase in enumerate(lista_frases):
    lista_frases[i] = lista_frases[i].strip()

print(lista_frases)

frases_unidas = '-'.join(lista_frases)
print(frases_unidas)
