def esMultiplo(numero1, numero2):
    return numero1 % numero2 == 0
numero1 = int(input("Insertar numero1"))
numero2 = int(input("Insertar numero2"))
if esMultiplo(numero1, numero2):
	print(numero1," es multiplo de ", numero2)
else:
	print(numero1," no es multiplo de ", numero2)