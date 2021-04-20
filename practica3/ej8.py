import re
numeros = "uno 1 dos 2 tres 3"
x = re.split("\D+", numeros)
for a in x:
    print(a)