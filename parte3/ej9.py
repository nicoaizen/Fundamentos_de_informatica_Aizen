import re
texto = "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"
x = re.split("Hoy estuvimos trabajando con re (.*)\ en python ", texto)
for a in x:
    print(a)