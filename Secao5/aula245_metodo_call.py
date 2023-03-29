# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".

class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'está chamando:', self.phone)
        return 'ring-ring'


call1 = CallMe('19988410611')
retorno = call1('Lucas Manesco')
print(retorno)
