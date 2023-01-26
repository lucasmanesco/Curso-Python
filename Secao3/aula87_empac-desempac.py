"""
Introdução ao desempacotamento + tuples (tuplas)
"""

#nome1, nome2, nome3 = ['Lucas', 'Jessica', 'Amora', 'Mike']  # too many values to unpack

_, nome2, *resto = ['Lucas', 'Jessica', 'Amora', 'Mike']  # _ variável que não vou usar
print(_, nome2, resto)

