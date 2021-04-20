import re
texto = "Hoy estuvimos trabajando con re-regular expression-en python-con VSCode"
x = re.sub("[-]*\s","|",texto)
print(x)