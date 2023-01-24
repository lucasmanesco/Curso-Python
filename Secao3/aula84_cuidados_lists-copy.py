"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Lucas', 'Jéssica']
# lista_b = lista_a

lista_b = lista_a.copy()

lista_a[0] = 'Nelson'
print(lista_b)
