import re
numero = int(input("Numero"))
texto = "Ejemplo 02"
x = re.search("^numero", texto)
if(x!=None):
	print("El string empieza con el numero",numero)
else:
	print("El string no empieza con el numero",numero)