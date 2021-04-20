import re
path = r"C:\Users\nicoa\Documents\Programacion\UCEMA_Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt"
lista = []
lista2 = []
with open(path,"r") as file:
    for lineas in file:
        lista.extend(lineas.split())
    print("Hay", len(lista), "palabras")
    for i in range(len(lista)):
        lista2.append(len(lista[i]))
    print(lista2)
    print(max(lista2))
    numero = lista2.index(14)
    print(lista[numero])