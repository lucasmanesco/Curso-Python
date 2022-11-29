"""
Conversão de tipos, coerção
type convertion, typecasting, coercion
é o ato de converter um tipo em outro
tipos imutáveis e primitivos: str, int, float, bool
"""

print(1 + 1) # soma
print('a' + 'b') # concatenação

# print('1' + 1) # TypeError

print('1', type('1'))
print(int('1'), type(int('1')))
print(int('1') + 1)
print(float('1') + 1)

print(bool(''))

print(str(11) + 'b')
