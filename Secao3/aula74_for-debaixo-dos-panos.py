"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue o seu iterador
"""

texto = 'Lucas'  # iterável
iterador = iter(texto)  # iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
