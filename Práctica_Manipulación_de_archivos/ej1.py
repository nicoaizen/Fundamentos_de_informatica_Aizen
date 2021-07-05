def texto (archivo):
    contador = 0
    with open(archivo, "r") as file:
        for i in file:
            if i[0] != "P":
                contador += 1