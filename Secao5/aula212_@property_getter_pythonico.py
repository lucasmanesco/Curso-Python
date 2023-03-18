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
"""


class Caneta:
    def __init__(self, cor):
        self.cor = cor
