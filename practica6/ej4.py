#Ejercicio 4
"""
Vamos a salir de paseo (¡si la pandemia nos deja!). Para esto podemos utilizar como vehículos
motos o autos, y de estos dos medios de transporte sabemos que:
comienzan con una cantidad que podemos establecer de combustible
- los autos pueden llevar 5 personas como máximo y al recorrer una distancia consumen
medio litro de combustible por cada kilómetro recorrido
- las motos pueden llevar 2 personas y consumen un litro por kilómetro recorrido;
- pueden cargar_combustible en la cantidad que digamos y al hacerlo suben su cantidad de combustible
- saben responder si entran una cantidad de personas. Esto sucede cuando esa cantidad
es menor o igual al máximo que pueden llevar.
- Definí las clases Moto, Auto y MedioDeTransporte y hace que las dos primeras hereden de la tercera."""


class MedioDeTransporte:
    def _init_(self, combustible_inicial):
        self.combustible = combustible_inicial
        self.pasajeros = []
    def cargar_combustible(self, litros):
        self.combustible += litros

class Auto(MedioDeTransporte):
    def recorrer(self,distancia):
        self.combustible-=(distancia/2)
    def subir_pasajero(self, pasajero):
        if len(self.pasajeros) < 5:
            self.pasajeros.append(pasajero)
    def entran_x_personas(self, personas):
        if personas > 5:
            print("No no entran", personas, "pasajeros")
        else:
            print("Sí, si entran", personas, "pasajeros")

class Moto(MedioDeTransporte):
    def recorrer(self,distancia):
        self.combustible-= distancia
    def subir_pasajero(self, pasajero):
        if len(self.pasajeros) < 2:
            self.pasajeros.append(pasajero)
    def entran_x_personas(self, personas):
        if personas > 2:
            print("No no entran", personas, "pasajeros")
        else:
            print("Sí, si entran", personas, "pasajeros")

ferrari = Auto(100)
honda = Moto(80)
honda.recorrer(80)
ferrari.recorrer(200)
print(honda.combustible)
print(ferrari.combustible)
ferrari.cargar_combustible(120)
honda.cargar_combustible(90)
print(honda.combustible)
print(ferrari.combustible)
ferrari.subir_pasajero("mateo")
ferrari.subir_pasajero("juan")
ferrari.subir_pasajero("rodrigo")
ferrari.subir_pasajero("felipe")
ferrari.subir_pasajero("matias")
ferrari.subir_pasajero("horacio")
print(ferrari.pasajeros)
honda.subir_pasajero("nicolas")
honda.subir_pasajero("augusto")
honda.subir_pasajero("horacio")
print(honda.pasajeros)
ferrari.entran_x_personas(6)
ferrari.entran_x_personas(5)
honda.entran_x_personas(3)
honda.entran_x_personas(2)