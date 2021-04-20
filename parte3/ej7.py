import re
lista = ["Cat 100", "---200", "xxxyyy", "jjj", "box4000", "tent500"]
for l in lista:
    x = re.match("^\d^\s[^a-zA-Z]", l)
if(x!=None):
	print("El texto cumple con la condicion")
else:
	print("El texto no cumple con la condicion")