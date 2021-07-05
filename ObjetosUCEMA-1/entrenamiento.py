class Ave:
    def esta_feliz(self):
        return self.energia > 500
    
    def arranca_en(self, ciudad):
        self.ciudad_actual = ciudad
    
    def volar_por_panamericana(self, ciudad_destino):
        kms = abs(self.ciudad_actual - ciudad_destino)
        self.volar(kms)
        self.ciudad_actual = ciudad_destino

class Golondrina(Ave):
    def __init__(self, energia):
        self.energia = energia

    def comer_alpiste(self, gramos):
        self.energia = self.energia + 4 * gramos

    def volar_en_circulos(self):
        self.volar(0)

    def volar(self, kms):
        self.energia -= 10 + kms

    def esta_debil(self):
        return self.energia <= 10

class Dragon(Ave):
    def __init__(self, cantidad_dientes, energia):
        self.energia = energia
        self.cantidad_dientes = cantidad_dientes

    def escupir_fuego(self):
        self.energia -= 2 * self.cantidad_dientes

    def comer_peces(self, unidades):
        self.energia += 100 * unidades

    def volar_en_circulos(self):
        self.energia -= 1

    def volar(self, kms):
        self.energia -= 10 + kms/10

class EntrenadorDeDragones:
    def __init__(self, vacantes):
        self.vacantes = vacantes
        self.dragones_aceptados = []
    
    def aceptar_dragon(self, dragon):
        if self.vacantes > 0:
            self.dragones_aceptados.append(dragon)
            self.vacantes -= 1
    
    def entrenar_dragones(self):
        for dragon in self.dragones_aceptados:
            for i in range(1, 20):
                dragon.volar_en_circulos()
            dragon.comer_peces(3)
    
    def esta_debil(self):
        return self.energia < 50

hipo = EntrenadorDeDragones(10)
roberta = Dragon(10, 1000)
chimuelo = Dragon(200, 1000)

ushuaia = 0
buenos_aires = 3078
valparaiso = 4533
bahia_prudhoe = 17958

#hipo.aceptar_dragon(roberta)
#hipo.aceptar_dragon(chimuelo)
#print(hipo.dragones_aceptados)
#print(hipo.vacantes)
#hipo.entrenar_dragones()
#print(roberta.energia)
#print(chimuelo.energia)