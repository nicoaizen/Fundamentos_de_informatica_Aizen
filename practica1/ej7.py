sueldo = int(input("Escribir sueldo"))
ventas = int(input("Escribir ventas"))
comision = sueldo * ventas * 0.1
total = sueldo + comision
print("Usted ha ganado $",comision, "en comisiones, y un total de $",total,"este mes")