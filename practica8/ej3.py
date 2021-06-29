# Ejercicio 3
# Realizá un programa que agregue datos a un DataFrame vacío.

import pandas as pd

muestra = {1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]}
df = pd.DataFrame()

df["Numeros"] = [1, 4, 3, 4, 5]
print(df)