lista = []
numero = int(input("Introducir un numero en la lista"))
while numero >=0:
	lista.append(numero)
	numero = int(input("Introducir un numero en la lista"))
for numero in lista:
	print(numero, " ", end="")