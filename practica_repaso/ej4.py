# Realizá un programa que a partir de una lista mixta (que contiene 
# distintos tipos de datos) imprima cuántos enteros tiene y además
# en el caso de los elementos que sean strings hay que crear una 
# nueva lista con estos strings pero reemplazando al A por la U 
# (tanto mayúscula como minúscula) y luego imprimir estos elementos.

lista = ["uno", 1, "dos", 2, "tres", 3, "cuatro", 4, 1.4]
numeros = []
palabras = []
for i in lista:
    if type(i) == int:
        numeros.append(i)
    if type(i) == str:
        palabras.append(i.replace("a", "u").replace("A", "U"))
print(numeros)
print(palabras)