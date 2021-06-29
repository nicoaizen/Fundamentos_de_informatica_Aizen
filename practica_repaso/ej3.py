# Escribí un programa que obtenga, a partir de una lista de strings
# una lista con la longitud de esas strings e imprima la longitud
# de la lista de strings y los elementos de la lista de longitudes

lista = ["uno", "dos", "tres", "cuatro", "cinco"]
lista1 = []
for i in lista:
    lista1.append(len(i))
contador = 0
for i in lista1:
    contador += i
for i in lista1:
    print(i)

print(len(lista))
print(contador)

# longitud de lista es len(lista)