"""
Sets são eficientes para remover valores duplicados de iteráveis.
- não tem indexes;
- não garantem ordem;
são iteráveis (for, in, not in)
"""
l1 = [1, 2, 3, 3, 3, 3, 3, 1]
s1 = set(l1)
l2 = list(s1)
print(l2)

for numero in s1:
    print(numero)