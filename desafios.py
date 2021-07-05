import pandas  as pd
import seaborn as sns
import scipy.stats as ss

path = r"C:\Users\nicoa\Documents\Programacion\datos\personas_2011.csv"

#Desafio 1: Averiguá para qué sirven los parámetro sep, index_col, nrows y header, skiprows

# SEP
df = pd.read_csv(path, sep = ";")
print(df)
# INDEX_COL: te ordena en primer lugar la columna correspondiente al numero que le pases, si index_col = 0, la tabla se ordena normal., si le pones index:col = 1, la primer colummna la ubica antes de la inicial
df = pd.read_csv(path, sep= ";", index_col = 0)
#print(df)
#NROWS : te devuelve las primeras filas correspondiente al numero que le pasas, si es 0 te devuelve toda la tabla resumida
df = pd.read_csv(path, sep= ";", index_col = 0, nrows = 0)
#print(df)
#HEADER: te pasa todos los datos de esa fila, es decir, el dato correspondiente a cada columna de esa fila
df = pd.read_csv(path, sep= ";", index_col = 0, nrows = 0, header = 68551) # nos da la info del dato numero 68550
print(df)

# dato NaN significa que no hay dato
df = pd.read_csv(path, sep = ";")
print(df.info()) #te devuelve el nombre de las columnas en forma de listas, con el conteo de los datos que no son nulos y te dice que tipo de dato tiene, en algunos es un numero entero, en otros es numero con coma
print(df["seniority_level"]) # es un objeto
print(df.describe()) #te devuelve el count, mean, std, min, 25%, 50%, 75%, max
print(df["persona_id"]) #te devuelve los datos (enumerados) de esa columna (id), además te indica --> Name, Length, dtype
print(df["max_dedicacion_horaria_docente_id"])
print(df["max_dedicacion_horaria_docente_id"].mean()) #2.284580592105263

#df.loc[fila, columna] cuenta a partir de la fila = 0 (la fila 1 esta en la posicion 0)

print(df.loc[2,"persona_id"])
print(df.seniority_level) # es lo mismo que poner corchete y comillas

#¿Cómo obtendrías la edad de esa persona?
print(df.loc[2,"edad"]) #30

#Podemos acceder los datos de una columna del DataFrame como una lista mediante el método tolist():
print(df["edad"].tolist())

#Desafío IV: Extrae la columna seniority_level y contá cuántas personas tenían expertice nivel B, C y D

print(df["seniority_level"].count())
print(df.groupby("seniority_level").count())
print(df.groupby("seniority_level"))
print(df.groupby("seniority_level")[["persona_id"]].count())
#B = 6674, C = 13645, D = 5774
print(df.groupby("edad")[["persona_id"]].count())

#Desafío V: ¿Qué resultados obtuviste en cada caso? Explicá qué hace cada linea de código
#a) print(df["seniority_level"].count()) 
    #obtuvimos el conteo de todas las filas de seniority_level = 68552
#b) print(df.groupby("seniority_level").count())
    #cuenta todos los datos que corresponden a cadacattegoria del Senority Level de acuerdo a cada colummna, x ej: de sexo_id, 4834 tienen categoria A, 6674 categoria B, etc
#c) print(df.groupby("seniority_level")[["persona_id"]].count())
    #cuenta cuantos datos de la columna persona_id pertenecen a las ≠ categorias de Seniority Level:
"""                 
seniority_level  persona_id          
A                      33085
B                      4834
C                      6674
D                     13645
S/D                    5774
                      4540
"""
print(df["edad"] * 2)
print(df["edad"] + 2)
print(df["edad"] > 2)