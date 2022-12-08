"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - hexadecimal
(Caracatere)(><^)(quantidade)
> - esquerda
< - direita
^ - centro
= - força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.> 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'

print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{variavel:&^10}')

print(f'{1000.621651781561:.1f}')
print(f'{1000.621651781561:,.1f}')
print(f'{1000.621651781561:+,.1f}')
print(f'{1000.621651781561:0>+10,.1f}')
print(f'{1000.621651781561:0=+10,.1f}')

print(f'O hexadecimal de 1500 é {1500:08X}')

print(f'{variavel!r}')
