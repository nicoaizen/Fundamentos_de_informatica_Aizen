contadores = {}
alfabeto = "abcdefghijklmnopqrstuvwxyz"
for letra in alfabeto + alfabeto.upper(): 
    contadores[letra] = 0
cadena = input("Escribir una cadena")
for caracter in cadena: 
    if caracter.lower() in alfabeto:
        contadores[caracter]+=1
for campo, valor in contadores.items():
    print (campo, valor)