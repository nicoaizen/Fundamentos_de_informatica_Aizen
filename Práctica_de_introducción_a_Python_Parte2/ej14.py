def calcularTemperaturaMedia(temperatura1, temperatura2):
	return (temperatura1 + temperatura2)/2
cantidad = int(input("Introducir dias"))
for a in range(cantidad):
	temperatura_min = float(input("Introducir temperatura minima"))
	temperatura_max = float(input("Introducir temperatura maxima"))
	print("La temperatura media es, ", calcularTemperaturaMedia(temperatura_min, temperatura_max))