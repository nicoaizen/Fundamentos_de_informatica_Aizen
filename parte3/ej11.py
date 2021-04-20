import re
def dos_P(lista):
  for elemento in lista:
      resultado = re.match("(P\w*)\W(P\w*)", elemento)
      if resultado is not None:
          print (resultado.group())
lista = ["Práctica Python", "Práctica C++", "Práctica Fortran"]
print (dos_P(lista))