class Dispositivo:
    def __init__(self):
        self.bateria = 100

    def cargar_a_tope(self):
        self.bateria = 100

    def descargado(self):
        self.bateria <= 20

    def valor_bateria(self):
        return self.bateria

class Celular(Dispositivo):
    def utilizar(self, min):
        self.bateria -= min/2

class Notebook(Dispositivo):
    def utilizar(self, min):
        self.bateria -= min

class CargadorUniversal(Dispositivo):
    def __init__(self):
        self.dispositivos = []
    
    def agregar(self, dispositivo):
        self.dispositivos.append(dispositivo)

    def cargar(self):
        for i in self.dispositivos:
            i.cargar_a_tope()

un_celu = Celular()
una_notebook = Notebook()
print(un_celu.descargado())
un_celu.utilizar(180)
print(un_celu.descargado())
una_notebook.utilizar(100)
una_notebook.cargar_a_tope()
print(una_notebook.descargado())
print(un_celu.valor_bateria())