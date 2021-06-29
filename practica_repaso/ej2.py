# Realizá un programa que imprima la suma de todos los valores
# de un diccionario de números.

# print(sum(diccionario.values()))

diccionario = {}
for i in range(1,16):
    diccionario[i] = i**2
contador = 0
for i in diccionario.values():
    contador += i
print(contador)
print(sum(diccionario.values()))