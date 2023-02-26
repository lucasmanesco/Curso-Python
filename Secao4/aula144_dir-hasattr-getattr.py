# dir, hasattr, getattr em Python
# dir - mostra todos os nomes definidos dentro de string

string = 'Lucas'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo))
    print(string)
else:
    print('Não existe o método', metodo)
