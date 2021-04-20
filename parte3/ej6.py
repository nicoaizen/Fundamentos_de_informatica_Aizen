import re
lista_strings = ["ayer", "cumpleaños", "muchos", "regalos"]
frase = "Hoy fue mi cumpleaños y me dieron muchos regalos"
for i in lista_strings:
    patron = i
    if re.search(patron, frase) is not None:
        print("La palabra se encuentra en la lista")
    else:
        print("La palabra no se encuentra en la lista")