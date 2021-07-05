# Ejercicio 2
# Escribí un programa que guarde en una lista una columna de un 
# DataFrame.

import pandas as pd

muestra = {1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]}
df = pd.DataFrame(muestra)

lista1 = df[1].to_list()
print(lista1)
