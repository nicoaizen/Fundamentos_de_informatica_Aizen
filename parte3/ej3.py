import re
texto = "voorheesville"
x = re.search("(he*)", texto)
if(x!=None):
	print("El texto cumple con la condicion")
else:
	print("El texto no cumple con la condicion")

y = re.search("(he{2,3}*)", texto)
if(y!=None):
	print("El texto cumple con la condicion")
else:
	print("El texto no cumple con la condicion")

z = re.search("(he.*)", texto)
if(z!=None):
	print("El texto cumple con la condicion")
else:
	print("El texto no cumple con la condicion")