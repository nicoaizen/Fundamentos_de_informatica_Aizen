# Ejercicio 5
# Realizá un programa que verifique si una columna dada se encuentra
# presente en un DataFrame.

import pandas as pd

muestra = {1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]}
df = pd.DataFrame(muestra)

def se_encuentra(columna):
    print(columna in df.columns)

se_encuentra(2)
