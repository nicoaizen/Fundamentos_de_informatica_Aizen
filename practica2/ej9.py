nombres = []
edades = []
edad_max = max(edades)
while True:	
	nombre = input("Nombre del alumno")
	edad = input("Edad del alumno")
	if nombre != "*":
		nombres.append(nombre)
		edades.append(edad)
	if nombre == "*": break;	
print("La edad maxima es ", edad_max)
print("Alumnos con edad maxima:")
for nombre, edad in (nombres, edades):
	if edad == edad_max:
		print(nombre)