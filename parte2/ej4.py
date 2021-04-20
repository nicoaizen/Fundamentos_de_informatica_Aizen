gramos = int(input("Ingresar el peso en gramos"))
zona = input("Ingresar la zona")
if gramos < 5000:
    if zona == "America del Sur":
        print(10 * gramos)
    if zona == "America Central":
        print(15 * gramos)
    if zona == "America del Norte":
        print(18 * gramos)
    if zona == "Europa":
        print(24 * gramos)
    if zona == "Asia":
        print(30 * gramos)
else:
    print("La entrega fue rechazada")