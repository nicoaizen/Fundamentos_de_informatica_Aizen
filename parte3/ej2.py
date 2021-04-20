import re
patron = "[^a-zA-Z0-9]"
texto = "Ejemplo02"
print(re.search(patron, texto))