path = r"C:\Users\nicoa\Documents\Programacion\UCEMA_Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt"
with open(path, "r") as file:
    texto = file.read()
    palabras = texto.split()
    print(len(palabras))
    print(palabras)