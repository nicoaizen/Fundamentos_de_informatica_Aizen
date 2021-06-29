# Ejercicio 3
# Escribí un programa para convertir un diccionario a una serie de
# Pandas.

# Diccionario de muestra:
dict1 = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50}
lista1 = []
lista3 = []
lista4 = []

import pandas as pd
for keys, values in dict1:
    lista1.append(dict1[keys])

serie1 = pd.Series(lista1, dtype=int)

contador = 0
for i in dict1.keys():
    contador += 1
    lista3.append(i)
    lista4.append(contador)

serie = pd.DataFrame(data ={"letra":lista3, "numero":lista1}, index = lista4)