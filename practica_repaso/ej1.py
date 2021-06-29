# Escribí un programa de python que imprima un diccionario cuyas 
# claves sean los números de 1 a 15 y cuyos valores sean las 
# potencias al cuadrado de estos números.

diccionario = {}
for i in range(1,16):
    diccionario[i] = i**2
for clave, valor in diccionario.items():
    print(clave, valor)

# para imprimir diccionarios usar print(clave, valor) en vez de
# print(diccionario)
# diccionario.keys --> clave
# diccionario.values --> valores