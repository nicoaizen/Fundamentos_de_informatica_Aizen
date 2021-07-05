# Ejercicio 8
# Realizá un programa que dado dos DataFrames genere otro que 
# contenga solo las columnas en común.

import pandas as pd

df1 = pd.DataFrame()
df1["1"] = ["1", "1", "1"]
df1["B"] = ["b", "b", "b"]

df2 = pd.DataFrame()
df2["2"] = ["2", "2", "2"]
df2["B"] = ["b", "b", "b"]

a = set.intersection(set(df1), set(df2))

df_nuevo = pd.DataFrame(a)
print(df_nuevo)