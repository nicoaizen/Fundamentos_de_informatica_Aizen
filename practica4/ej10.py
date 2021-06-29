import glob
path = r"C:\Users\nicoa\Documents\Programacion\UCEMA_Fundamentos_de_informatica-master\Python_intro\manipulacion_archivos.txt"
archivo = r"C:\Users\nicoa\Documents\Programacion\UCEMA_Fundamentos_de_informatica-master\Python_intro\completo.txt"
with open(archivo,"a") as file:
    archivos = glob.glob(path + "/*.txt")
    for texto in archivos:
        with open(texto,"r") as text:
           transcript = text.read()
           with open(archivo,"a") as final:
               final.write(transcript)
print(final)