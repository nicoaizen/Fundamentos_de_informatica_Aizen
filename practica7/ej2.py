# Ejercicio 2
# Realizá un programa que compare (si son mayores, menores o iguales)
#  los elementos de dos series de números de Pandas.

# Series de muestra:
# [3, 7, 12, 15, 21], [1, 4, 10, 14, 19]

import pandas as pd
serie1 = pd.Series([3, 7, 12, 15, 21], dtype = int)
serie2 = pd.Series([1, 4, 10, 14, 19], dtype = int)

serieMayor = serie1 > serie2
serieMenor = serie1 < serie2
serieIgual = serie1 == serie2

print(serieMayor)
print(serieMenor)
print(serieIgual)