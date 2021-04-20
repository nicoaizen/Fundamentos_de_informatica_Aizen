minutos = int(input("Insertar minutos"))
h = minutos / 60 - minutos % 60 /60
min = minutos % 60
print(h, "horas y", min, "minutos")