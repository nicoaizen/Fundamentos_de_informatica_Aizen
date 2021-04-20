import re
path = r"C:\Users\nicoa\Documents\Programacion\UCEMA_Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt"
path2 = r"C:\Users\nicoa\Documents\Programacion\UCEMA_Fundamentos_de_informatica-master\Python_intro\ej5.txt"
with open(path, "r") as file:
    texto = file.read()
    with open(path2, "w") as file2:
         file2.write(re.sub("[t]","t\n",texto))