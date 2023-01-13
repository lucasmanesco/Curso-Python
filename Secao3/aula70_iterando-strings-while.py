frase = 'O Python é uma linguagem de programação '\
        'multiparadigma. ' \
        'Python foi criado por Guido van Rossum.'

i = 0
j = len(frase)
frase_low = frase.lower()
resultado = 0

while i < j:
    if frase_low[i].isalpha():
        if frase_low.count(frase_low[i]) > resultado:
            resultado = frase_low.count(frase_low[i])
            posicao = i
    i += 1

print(frase)
print(f'O caractere que mais aparece na frase é "{frase_low[posicao]}", apareceu {resultado} vezes.')
