from sys import path

import aula157_package.modulo
from aula157_package import modulo
from aula157_package.modulo import soma_mod

# print(__name__)
# print(*path, sep='\n')

print(soma_mod(1, 2))
print(aula157_package.modulo.soma_mod(1, 2))
print(modulo.soma_mod(1,2))
