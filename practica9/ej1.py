# Ejercicio
# Obtener las 10 personas con mayor edad y generar un nuevo 
# DataFrame con la información de el id de la persona, el año, 
# su edad, el id de la categoría conicet y las producciones 
# académicas de los últimos 4 años. Unirlo con el DataFrame conicet 
# y en base a ese generar una tabla con el id de la persona y la 
# descripción de la categoría en conicet. Luego guardar este último 
# DataFrame en un archivo.

import pandas as pd

path = r"C:\Users\nicoa\Documents\Programacion\datos"
personas2011 = pd.read_csv(path, sep=";")
personas = pd.DataFrame()
print(personas)

personas1 = personas.sort_values(by="edad", ascending=False)
personas_mayores = personas1.head(10)
#print(personas_mayores)

lista = []
for i in personas.columns:
    if i != "persona_id" and i != "anio" and i != "edad" and i != "categoria_conicet_id" and i != "producciones_ult_4_anios":
        lista.append(i)

personas_mayores.drop(lista, axis=1, inplace=True)
print(personas_mayores)

path_conicet = r"C:\Users\nicoa\Documents\Programacion\datos\ref_categoria_conicet.csv"
conicet = pd.read_csv(path_conicet, sep=";")
personas_mayores = pd.merge(personas_mayores, conicet, on="categoria_conicet_id", how="inner")
personas_conicet = pd.concat([personas_mayores["persona_id"], personas_mayores["categoria_conicet_descripcion"]], axis=1)

print(personas_conicet)
personas_conicet.to_csv("personasmayores_conicet.csv", index=False, header=True, sep=";")
