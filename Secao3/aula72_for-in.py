""" while - usar quando não sei quantas repetições serão realizadas """

texto = 'Python'

i = 0
tamanho_string = len(texto)

while i < tamanho_string:
    print(texto[i])
    i += 1

""" for - já sei quantas repetições serão realizadas """

texto2 = 'Lucas'

for letra in texto2:
    print(letra)
