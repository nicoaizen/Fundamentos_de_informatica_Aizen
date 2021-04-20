import re
texto = "Hoy estuvimos trabajando con re-regular expression-en python-con VSCode"
x = re.findall("[-]*",texto)
print(x)