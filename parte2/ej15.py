socios = {}
socios["1"] = ["Florencia Ocampo","14/09/2001","cuota al día"]
socios["2"] = ["David Estévez","14/09/2001","cuota al día"]
socios["3"] = ["Sofía Cáceres","14/09/2001","cuota al día"]

numero_socio = int(input("ingresar el numero de socio: "))
while numero_socio > 0:
      nombre_y_apellido = input("ingresar el nombre y el apellido: ")
      fecha_ingreso = input("ingresar la fecha de ingreso con el siguiente formato = dd/mm/aaaa : ")
      estado_cuota = input("ingresar 'cuota al dia' o 'cuota atrasada': ")
      socios[numero_socio] = [nombre_y_apellido, fecha_ingreso , estado_cuota ]
      numero_socio = int(input("ingresar el numero de socio: "))

print(socios.values())


#B
print("El club tiene", len(socios.keys()),"socios")

#C
def pago_cuotas(nro):
      if socios[nro][2] == "cuota al dia":
            return print("El socio",nro, "no tiene deudas")
      else:
            return print("El socio", nro, "tiene deudas")

#D
socios["444"] = ["Mario Fernandez", "21/10/2017","cuota al dia" ]
socios["555"] = ["Juan Perez", "21/10/2017", "cuota al dia"]
socios["666"] = ["Maria Martinez", "21/10/2017", "cuota al dia"]

def cambiar_fecha (fecha_nueva,fecha_mal):
      for a in socios.keys():
            if socios[a][1] == fecha_mal:
                  socios[a][1] = fecha_nueva
            else:
                   socios[a][1] 
          
cambiar_fecha("22/10/2017","21/10/2017")
print(socios.values())

#E
def dar_de_baja (nombre):
      for a in socios.keys():
            if socios [a][0] == nombre:
                  del socios[a]

dar_de_baja ("Florencia Ocampo")

#F
print("Los datos de los socios son:",socios.values())