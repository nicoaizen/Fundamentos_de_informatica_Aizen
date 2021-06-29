#Dada la siguiente clase, identificá la interfaz y el estado de la misma:

class Perro:
    def __init__(self):
        self._alimento = 0
        self._caricias = 0

    def energia(self):
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2

#interfaz = los mensajes que pueden llegar a entdender los objetos
# --> energia, comer, acariciar, estaDebil
#estado = atributos. los atributos estan definidos en el constructor. 
"""el constructor es def__init__(self)"""
# --> alimento y caricias