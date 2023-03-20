
"""
@property + @setter - getter e setter no modo Pythônico
- como getter
- p/ evitar quebrar código clinete
- p/ habilitar setter
- p/ executar ações ao obter um atributo

* Atributos que começam com _ ou __ não devem ser usados fora da classe.
"""


class Caneta:
    def __init__(self, cor):
        # private / protected
        self._cor = cor  # atributo protegido pela classe
        self._cor_tampa = None

    @property
    def cor(self):
        print('Getter: ')
        return self._cor

    @cor.setter
    def cor(self, valor):
        if valor == 'Branca':
            raise ValueError('Não aceito essa cor.')
        print('Setter: ', valor)
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta('Azul')

# setter - setar valor
caneta.cor = 'Vermelha'
caneta.cor_tampa = 'Preta'

# getter = obter valor
print(caneta.cor)
print(caneta.cor_tampa)
