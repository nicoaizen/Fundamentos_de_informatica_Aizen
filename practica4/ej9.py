path = r"C:\Users\nicoa\Documents\Programacion\UCEMA_Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt"
with open(path, "r") as file:
    texto = file.read()
    palabras = texto.split()
    palabras_sin_coma = []
    for i in palabras:
        palabra = i.strip(",")
        palabras_sin_coma.append(palabra)
    cantidad_palabras = len(palabras_sin_coma)
    frecuencias = {}               
    for palabra in palabras_sin_coma:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    for palabra in frecuencias:
        frecuencia = frecuencias[palabra] / cantidad_palabras
        print("La palabra " + str(palabra) + "tiene una frecuencia de " + str(frecuencia))