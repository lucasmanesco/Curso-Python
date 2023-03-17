# Métodos em instâncias de classes Python
# Entendendo self em classes Python

# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.


class Carro:
    def __init__(self, modelo):
        self.modelo = modelo

    def acelerar(self):
        print(f'{self.modelo} está acelerando...')


fusca = Carro('Fusca')
print(fusca.modelo)
fusca.acelerar()
Carro.acelerar(fusca)

celta = Carro('Celta')
print(celta.modelo)
celta.acelerar()
Carro.acelerar(celta)
