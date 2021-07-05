#6
# Implementá una clase que represente una calculadora sencilla, que permita sumar, restar y multiplicar. Este objeto debe entender 
# los siguientes mensajes:
"""
cargar(numero)
sumar(numero)
restar(numero)
multiplicar(numero)
valorActual()
"""

class Calculadora:
    def __init__(self, numero):
        self.numero = numero

    def cargar(self, n):
        self.numero == n

    def sumar(self, n):
        self.numero += n

    def restar(self, n):
        self.numero -= n

    def multiplicar(self, n):
        self.numero * n

    def valorActual(self):
        self.numero

calculadora = Calculadora
print(calculadora.cargar(0))
print(calculadora.sumar(4))
print(calculadora.multiplicar(5))
print(calculadora.restar(8))
print(calculadora.multiplicar(2))
print(calculadora.valorActual())

# Si se evalúa la siguiente secuencia: el resultado debe ser 24.