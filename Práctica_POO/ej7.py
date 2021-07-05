#7
# Definí una clase de gorriones, de los cuales nos interesa conocer dos medidas conocidas como CSS (coeficiente de serenidad silenciosa), 
# CSSP y CSSV (como el CSS pero “pico” y “veces”). El CSS resulta de dividir la cantidad total de kilómetros que vuela desde que se lo 
# comienza a estudiar, por la cantidad total de gramos de comida que ingiere. El CSSP es la misma división pero considerando solamente 
# lo que voló la vez que más voló y lo que comió la vez que más comió. El CSSV es otra vez la misma idea, respecto de la cantidad de 
# veces que voló y comió. Si un gorrión nunca comió, los coeficientes deben ser None. Un gorrión se considera en equilibrio si su CSS está
# entre 0.5 y 2

class Golondrina:
    def __init__(self):
        self.km_volados = []
        self.g_comida = []

    def volar(self, km):
        self.km_volados.append(km)
    
    def comer(self, g):
        self.g_comida.append(g)

    def css(self):
        css = sum(self.km_volados) / sum(self.g_comida)
        if len(self.g_comida) == 0:
            return None
        elif css >= 0.5 and css <= 2:
            return css

    def cssp(self):
        if len(self.g_comida) != 0:
            return max(self.km_volados) / max(self.g_comida)
        else:
            None

    def cssv(self):
        if len(self.g_comida) != 0:
            return len(self.km_volados) / len(self.g_comida)
        else:
            None

rio = Golondrina()
rio.volar(10)
rio.volar(6)
rio.volar(8)
print(rio.km_volados)
rio.comer(5)
rio.comer(5)
rio.comer(2)
print(rio.g_comida)
print(rio.css())
print(rio.cssp())
print(rio.cssv())