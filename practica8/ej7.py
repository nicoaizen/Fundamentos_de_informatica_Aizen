# Ejercicio 7
# Creá un programa que dado un diccionario y una lista añada está
# última al DataFrame generado a partir del diccionario.

import pandas as pd
dicc =  {1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]} 
lista = [1,2,3,4,5]
df = pd.DataFrame(dicc)
s1 = pd.Series(lista, name = 4)

df[4] = lista
print(df)