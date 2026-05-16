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

    def mazoCartas(self):
        for i in range(1, 14):
            for j in range(1, 5):
                self.cartas.append(i, j)

    

    