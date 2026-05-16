import os
import random
import matplotlib.pyplot as plt
from matplotlib import image as mpimg


class TemaCinco:
    def __init__(self):
        self.cartas = []
        self.definicion = "La probabilidad de que ocurran dos o más eventos, se calcula multiplicando la probabilidad de cada evento."
        self.cartasTrebol = 13
        self.cartasDiamante = 13
        self.cartasCorazon = 13
        self.cartasEspada = 13
        self.cartasNegras = 26
        self.cartasRojas = 26
        self.cartasJ=4
        self.cartasQ=4
        self.cartasK=4
        self.cartasA=4

    def mazoCartas(self):
        for i in range(1, 14):
            for j in range(1, 5):
                self.cartas.append((i, j))

    
    def tres_corazones_seguidos(self):
        cantidadCartas= len(self.cartas)
        probabilidadCartaUno = self.cartasCorazon / cantidadCartas
        cantidadCartas -=1
        self.cartasCorazon -=1

        probabilidadCartaDos = self.cartasCorazon / cantidadCartas
        cantidadCartas -=1
        self.cartasCorazon -=1

        probabilidadCartaTres = self.cartasCorazon / cantidadCartas

        probabilidad = probabilidadCartaUno * probabilidadCartaDos * probabilidadCartaTres

        valores = random.sample(range(1, 14), 3)
        cartas_ejemplo = [self.mostrar_carta(v, 1) for v in valores]

        return probabilidad, cartas_ejemplo
        
    def rey_rojo_y_carta_negra(self):
        cantidadCartas= len(self.cartas)
        probabilidadReyRojo = self.cartasRojas / cantidadCartas
        cantidadCartas -=1
        self.cartasRojas -=1

        probabilidadCartaNegra = self.cartasNegras / cantidadCartas
        cantidadCartas -=1
        self.cartasNegras -=1

        probabilidad = probabilidadReyRojo * probabilidadCartaNegra

        rey_rojo_j = random.choice([1, 3])
        carta_negra_i = random.randint(1, 13)
        carta_negra_j = random.choice([2, 4])
        cartas_ejemplo = [
            self.mostrar_carta(13, rey_rojo_j),
            self.mostrar_carta(carta_negra_i, carta_negra_j)
        ]

        return probabilidad, cartas_ejemplo

    def cuatro_rojas_seguidas(self):
        cantidadCartas= len(self.cartas)

        probabilidadCartaUno = self.cartasRojas / cantidadCartas
        cantidadCartas -=1
        self.cartasRojas -=1

        probabilidadCartaDos = self.cartasRojas / cantidadCartas
        cantidadCartas -=1
        self.cartasRojas -=1

        probabilidadCartaTres = self.cartasRojas / cantidadCartas
        cantidadCartas -=1
        self.cartasRojas -=1

        probabilidadCartaCuatro = self.cartasRojas / cantidadCartas

        probabilidad = probabilidadCartaUno * probabilidadCartaDos * probabilidadCartaTres * probabilidadCartaCuatro

        rojas = [(i, j) for i in range(1, 14) for j in [1, 3]]
        seleccionadas = random.sample(rojas, 4)
        cartas_ejemplo = [self.mostrar_carta(i, j) for i, j in seleccionadas]

        return probabilidad, cartas_ejemplo

    def rey_reina(self):
        cantidadCartas= len(self.cartas)
        
        probabilidadRey = self.cartasK / cantidadCartas
        cantidadCartas -=1
        self.cartasK -=1

        probabilidadReina = self.cartasQ / cantidadCartas
        cantidadCartas -=1
        self.cartasQ -=1

        probabilidad = probabilidadRey * probabilidadReina

        rey_j = random.randint(1, 4)
        reina_j = random.randint(1, 4)
        cartas_ejemplo = [
            self.mostrar_carta(13, rey_j),
            self.mostrar_carta(12, reina_j)
        ]

        return probabilidad, cartas_ejemplo

    def mostrar_carta(self, i, j):
        if j == 1:
            tipo_carta = "Corazones"
        elif j == 2:
            tipo_carta = "Espadas"
        elif j == 3:
            tipo_carta = "Diamantes"
        else:
            tipo_carta = "Trebol"

        ruta_imagen_carta_png = f"imagenes/{i}{tipo_carta}.png"
        ruta_imagen_carta_jpg = f"imagenes/{i}{tipo_carta}.jpg"

        if os.path.exists(ruta_imagen_carta_png):
            return ruta_imagen_carta_png
        else:
            return ruta_imagen_carta_jpg