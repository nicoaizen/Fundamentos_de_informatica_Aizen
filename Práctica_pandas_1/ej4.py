# Ejercicio 4
# Escribí un programa que dado un diccionario cuyos valores son 
# listas de números, cree otro diccionario con las mismas claves, 
# pero donde los valores sean una lista de números donde se potencia 
# un número por el siguiente, tomándolos de a pares. Para ser más
#  claros miremos este ejemplo donde si un diccionario es:

dict1 = {"a": [1,3,5,2], "b": [4,2,3,3]}
dict2 = {}

for clave, valor in dict1.items():
    pares = []
    impares = []
    potencia = []
    for i in range(len(valor)):
        if i % 2 == 0:
            pares.append(valor[i])
        else:
            impares.append(valor[i])
    for i in range(len(pares)):
        potencia.append(pares[i] ** impares[i])
    dict2[clave] = potencia

import pandas as pd
df = pd.DataFrame(dict2)
print(df)