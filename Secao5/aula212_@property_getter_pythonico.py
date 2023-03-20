
"""
@property - um getter no modo Pythonico
getter - um método para obter um atributo
cor -> get_cor()
modo Pythonico - modo de Python de fazer coisas
@property é uma propriedade do objeto, ela é
um método que se comporta como um atributo.
Geralmente é usada nas seguintes situaçõies:
 - como getter;
 - p/ evitar quebrar código cliente
 - p/ habilitar setter
 - p/ executar ações ao obter um atributo
 * Código Cliente = é o código que usa seu código
"""


class Caneta:
    def __init__(self, cor):
        # privated / protected / public - encapsulamento
        self.cor_tinta = cor

    # def get_cor(self):
    #     return self.cor

    @property
    def cor(self):
        print('Property.')
        return self.cor_tinta

    @property
    def cor_tampa(self):
        return 123456


caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor_tampa)
# print(caneta.get_cor())
