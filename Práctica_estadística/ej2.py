# Ejercicio Estadistica
# Dado este archivo caracterizar estadísticamente los datos 
# incluídos en el mismo.

import pandas as pd

path = r"C:\Users\nicoa\Documents\Programacion\datos\Datos.csv"
datos = pd.read_csv(path, sep=",")
print(datos)

#No hay columnas sin datos
print(len(datos))
datos.dropna(thresh= 1, inplace = True, axis= 0)
print(len(datos))

#Elimino columnas duplicadas
datos.drop_duplicates(inplace=True)
print(len(datos))

#Los valores float son sueldo y altura

print(datos.describe())
print(datos["Sueldo"].mode())

print(datos.sort_values(by = "Altura", ascending = False)) #Hay dos personas con alturas irreales y dos con altura Nan
print(datos.sort_values(by = "Altura", ascending = True)) #Hay personas con 1,12/1,20 que podrían ser niños pero sino es raro
print(datos[datos["Altura"] >= 2].count()) #Hay 18 personas
print(datos[datos["Altura"] <= 1.4].count()) #Hay 14 personas

