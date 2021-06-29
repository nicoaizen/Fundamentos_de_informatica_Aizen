import re
frase = "Hol@&"
patron = "[@&](.*?)[&@]"
letras = re.findall(patron, frase)
print(letras)
for i in letras:
    print(i + str(re.search(i, frase).span()))