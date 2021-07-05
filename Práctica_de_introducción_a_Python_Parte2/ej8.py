lista1 = []
lista2 = []
lista3 = []
for a in range(1,6):
	lista1.append(int(input("Introducir el numero" % a)))
for a in range(1,6):
	lista2.append(int(input("Introducir el numero" % a)))
for a in range(0,5):
	lista3.append(lista1[a] + lista2[a])
print("La suma de lista1 y lista2 es")
for numero in lista3:
	print(numero, " ", end="")
