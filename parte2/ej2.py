numero = input("Insertar un numero"):
    if numero > 0 and numero % 2 == 0:
      print("Es positivo y par")
    elif numero > 0 and numero % 2 != 0:
      print("Es positivo e impar")
    elif numero < 0 and numero % 2 == 0:
      print("Es negativo y par")
    elif numero < 0 and numero % 2 != 0:
      print("Es negativo e impar")
    elif numero == 0:
      print("Es cero y par")