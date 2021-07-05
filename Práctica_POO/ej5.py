#5
#Modificá el ejercicio anterior de manera que sea capaz de recordar cual fue el último comando que se le dió, en forma de mensaje. 
# Estos mensajes pueden ser: "reset", "incremento", "disminución" o "actualización" (para cuando se coloca un valor nuevo). 
# El método para saber el último comando es ultimoComando, y el resultado de aplicarlo a la serie de comandos dicha en el ejercicio 
# anterior debería ser "disminución".

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