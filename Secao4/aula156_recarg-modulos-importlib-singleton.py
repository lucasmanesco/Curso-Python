import importlib

import aula156_m

print(aula156_m.variavel)

for i in range(10):
    importlib.reload(aula156_m)
    print(i)

print('Fim')
