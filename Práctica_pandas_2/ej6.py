# Ejercicio 6
# Escribí un programa que dado dos diccionarios genere dos DataFrame
# y los una tanto en el eje de las columnas como en el eje de las 
# filas.

import pandas as pd

datos_a = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}
datos_b = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}
labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

dfa = pd.DataFrame(datos_a, index=labels)
dfb = pd.DataFrame(datos_b, index=labels)
resultado = pd.concat([dfa, dfb])
print(resultado)