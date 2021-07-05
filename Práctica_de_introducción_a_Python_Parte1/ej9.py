costo_total = int(input("Ingresar valor de la casa"))
porcentaje_deposito = costo_total * 0.25
cantidad_ahorrada = int(input("Ingresar cantidad ahorrada"))
g = cantidad_ahorrada * 0.04
sueldo_anual = int(input("Ingresar sueldo anual"))
porcentaje_ahorrado0 = int(input("Ingresar porcentaje"))
sueldo_mensual = sueldo_anual / 12
porcentaje_ahorrado = porcentaje_ahorrado0 * 0.1 * sueldo_mensual
meses = (porcentaje_deposito - cantidad_ahorrada - g) / porcentaje_ahorrado
print("Tomara",round(meses),"meses en pagar el depostio")