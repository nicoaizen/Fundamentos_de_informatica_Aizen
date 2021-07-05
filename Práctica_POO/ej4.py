#4
#Definí una clase que modele un contador, el cual puede incrementar o disminuir en uno el valor que se ingresa, recordando el valor 
# actual. También puede resetear este valor y al hacerlo se pone en cero. Además es posible indicar directamente un número nuevo que 
# reemplace al valor actual. Este objeto debe entender los siguientes mensajes:
"""
inc() listo
dis() listo
reset()
valorActual()
valorNuevo(nuevoValor) listo
"""
# Como ejemplo el resultado de ejecutar las siguientes líneas tiene que ser 12 y 25.

"""
contador = Contador(10)
contador.inc()
contador.inc()
contador.dis()
contador.inc()
contador.valorActual()
contador.valorNuevo(27)
contador.dis()
contador.dis()
contador.valorActual()
"""

class Contador:    
    def __init__(self, numero):
        self.numero = numero

    def inc(self):
        self.numero += 1

    def dis(self):
        self.numero -= 1

    def valor_nuevo(self, vn):
        self.numero = vn
    
    def valor_actual(self):
        self.numero
    
    def reset(self):
        self.numero = 0

    def guardar_numero(self):
        a == self.numero
    
    def volver_original(self, numero):
        self.numero = numero
    
a = Contador(110)
print (a.guardar_numero())
print (a.inc())
print (a.numero)
print (a.dis())
print (a.numero)
print (a.valor_actual())
print (a.numero)
print (a.valor_nuevo(120))
print (a.numero)
print (a.reset())
print (a.numero)
print (a.volver_original(a.guardar_numero()))
print (a.numero)