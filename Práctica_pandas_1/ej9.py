# Ejercicio 9
# Escribí un programa que dado el DataFrame anterior imprima los 
# nombres en mayúscula y la longitud de los mismos en una nueva 
# tabla.

import pandas as pd

datos_ejemplo = {"nombre": ["Agustina", "Diana", "Karen", "Julián", "Emilio", "Miguel", "Mateo", "Laura", "Jorge", "Lucas"], "puntaje": [12.5, 9, 16.5, 13, 9, 20, 14.5, 10, 8, 19], "intentos": [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], "califica": [1, 0, 1, 0, 0, 1, 1, 0, 0, 1]}
labels = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

df = pd.DataFrame(datos_ejemplo, index=labels)
print(df[["nombre", "puntaje"]])

s = pd.Series(datos_ejemplo["nombre"])
df_nuevo = pd.DataFrame()
df_nuevo["nombre"] = s.str.upper()
df_nuevo["longitud"] = s.str.len()

print(df_nuevo)