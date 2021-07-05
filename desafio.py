import pandas as pd
path = r"C:\Users\nicoa\Downloads\personas_2011.csv"
df = pd.read_csv(path, sep=";")
print(df.head(15))

# pd.read_csv
# sep
# header: se puede pasar fila para que sea encabezado
# dtype: tipo de datos del dataframe. def: detecta automatico
# skiprows: ignora numero de filas. def: 0
# nrows cant de lineas q se leen del archivo. Sirve cuando 
# el archivo es muy grande

# df.head: muestra una parta del df. def: 5
# df.tail: muestra la ultima parte del df. def: 5
# df.max: max por columna
# df.min: min por columna
# df.count: devuelva cantidad de datos no nulos por columna

datos = {"A": [-1, 54, 4, 5]}
df = pd.DataFrame(datos)
print(df.loc[df["A"]]>0)

pd.concat() # se pueden concatenar objetos de manera de
# unirlos generando nuevas columnas

#to_dict()
#to_list()