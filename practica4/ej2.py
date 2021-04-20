from itertools import islice
path = r"C:\Users\nicoa\Documents\Programacion\UCEMA_Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt"
def leer_n_lineas(archivo,n):
    with open(archivo,"r") as file:
        for l in islice(file,n):
            print(l)
leer_n_lineas(path,8)