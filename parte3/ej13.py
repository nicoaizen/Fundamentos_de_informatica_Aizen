import re
texto = "$$Hola"
x = re.sub("\W{1}","-",texto)
print(x)