import os
import random
import matplotlib.pyplot as plt
from matplotlib import image as mpimg


class TemaCinco:
    def __init__(self):
        self.cartas = []
        self.definicion = "La probabilidad es un método por el cual se obtiene la frecuencia de un acontecimiento determinado mediante \nla realización de un experimento aleatorio, del que se conocen todos los resultados posibles,\n bajo condiciones suficientemente estables."
        self.cartasTrebol = 12
        self.cartasDiamante = 12
        self.cartasCorazon = 12
        self.cartasEspada = 12
    


    def mazoCartas(self):
        for i in range(1, 13):
            for j in range(1, 5):
                self.cartas.append(i, j)

    