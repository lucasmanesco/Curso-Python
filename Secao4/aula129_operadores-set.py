"""
Operadores úteis:
união | união (union) - une
intersecção & (intersection) - itens presentes em ambos
diferença - itens presentes apenas no set da esquerda
diferença simétrica ^ - itens que não estão em ambos
"""

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s4 = s1 & s2
s5 = s1 - s2
s6 = s1 ^ s2
print(s3, s4, s5, s6)
