path = r"C:\Users\nicoa\Documents\Programacion\UCEMA_Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt"
lista = []
with open(path,"r") as file:
    for i in range(70):
        lista.append(file.readline(i))
print(len(lista))
def imprimir_n_ultimas(n):
    print(lista[(70-n):])
imprimir_n_ultimas(5)