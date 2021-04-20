dict = {}
cadena = input("Escribir una cadena")
for a in cadena:
	if a in dict:
		dict[a]+=1
	else:
		dict[a]=1	
for campo, valor in dict.items():
	print(campo,"->",valor)