class Notebook:
    def __init__(self, modelo):
        self.modelo = modelo
        self._marca = None
        self._processador = None
        self._memoria = None
        self._ram = None

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, valor):
        self._marca = valor

    @property
    def processador(self):
        return self._processador

    @processador.setter
    def processador(self, valor):
        self._processador = valor

    @property
    def memoria(self):
        return self._memoria

    @memoria.setter
    def memoria(self, valor):
        self._memoria = valor

    @property
    def ram(self):
        return self._ram

    @ram.setter
    def ram(self, valor):
        self._ram = valor


class Marca:
    def __init__(self, nome):
        self.nome = nome


class Processador:
    def __init__(self, nome):
        self.nome = nome


class Memoria:
    def __init__(self, nome):
        self.nome = nome


class Ram:
    def __init__(self, nome):
        self.nome = nome


dell = Marca('Dell')
lenovo = Marca('Lenovo')
i7 = Processador('Intel Core i7')
i5 = Processador('Intel Core i5')
ssd_512 = Memoria('SSD - 512GB')
hd_1000 = Memoria('HDD - 1TB')
ram_12 = Ram('12 GB')
ram_8 = Ram('8 GB')

note1 = Notebook('ideaPad 3i')
note1.marca = lenovo
note1.processador = i7
note1.memoria = ssd_512
note1.ram = ram_12
print(note1.modelo,
      note1.marca.nome,
      note1.processador.nome,
      note1.memoria.nome,
      note1.ram.nome)

note2 = Notebook('Latitude')
note2.marca = dell
note2.processador = i5
note2.memoria = hd_1000
note2.ram = ram_8
print(note2.modelo,
      note2.marca.nome,
      note2.processador.nome,
      note2.memoria.nome,
      note2.ram.nome)
