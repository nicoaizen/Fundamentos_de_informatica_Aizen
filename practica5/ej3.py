#3
#Creá una clase Notebook cuyo estado sea: marca, modelo y precio, y que tenga un método que le aplique un descuento al precio, 
# el cual tiene que recibir un número entero (el porcentaje de descuento) y tiene que devolver cuánto valdría esa notebook si 
# se aplicase el descuento. Por último hay que instanciar esta clase y en algunos casos aplicar este descuento.

class Notebook:

    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def aplicar_descuento(self, descuento):
        self.precio -= self.precio * (descuento/100)
        print ("queda en $", self.precio)

Hp = Notebook(1,10,100000)
print (Hp.aplicar_descuento(20))

Macbook = Notebook(2,2,120000)
print (Macbook.aplicar_descuento(30))