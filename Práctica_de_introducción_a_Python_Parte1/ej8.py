correcta = int(input("Cantidad de respuestas correctas"))
incorrecta = int(input("Cantidad de respuestas incorrectas"))
en_blanco = int(input("Cantidad de respuestas en blanco"))
nota = correcta*4 - incorrecta*1 + en_blanco*0
print("La notal final del alumno es",nota)