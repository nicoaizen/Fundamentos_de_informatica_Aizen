#Ejercicio 1
"""
Dadas las siguientes clases responder:

cuales son sus estados: -> alimento, caricias
cuales son sus interfaces: -> energia, comer, alimento, acariciar,
estaDebil, pasear, caricias
¿Comparten interfaz? -> energia, comer, acariciar, estaDebil
¿Son polimórficas? -> no, porque falta una tercera clase que
utilize estas interfaces
"""

class Perro:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0

    def energia(self):
        return self.alimento + (self.caricias * 10)

    def comer(self, gramos):
        self.alimento += gramos

	def alimento(self):
        return self.alimento

    def acariciar(self):
        self.caricias += 1

    def estaDebil(self):
        return self._caricias < 2

	def pasear(self, km):
		self.alimento -= km / 4

class Gato:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0

    def energia(self):
        return self.alimento + (self.caricias * 8)

    def comer(self, gramos):
        self.alimento += gramos * 1.5

	def caricias(self):
		return self.caricias

    def acariciar(self):
        self.caricias += 1

    def estaDebil(self):
        return self._caricias < 4