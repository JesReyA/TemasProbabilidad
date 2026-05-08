import os
import random
import matplotlib.pyplot as plt
from matplotlib import image as mpimg

class TemaUno:
    def __init__(self):
        self.numero_aleatorio_carta = random.randint(1,13)
        self.numero_aleatorio_tipo_carta = random.randint(1,4)
        self.definicion = " Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quod."

    def mostrar_carta(self):
        if self.numero_aleatorio_tipo_carta == 1:
            tipo_carta = "Corazones"
        elif self.numero_aleatorio_tipo_carta == 2:
            tipo_carta = "Espadas"
        elif self.numero_aleatorio_tipo_carta == 3:
            tipo_carta = "Diamantes"
        else:
            tipo_carta = "Trebol"

        ruta_imagen_carta_png = f"imagenes/{self.numero_aleatorio_carta}{self.tipo_carta}.png"
        ruta_imagen_carta_jpg = f"imagenes/{self.numero_aleatorio_carta}{self.tipo_carta}.jpg"

        if os.path.exists(ruta_imagen_carta_png):
            imagen_carta = mpimg.imread(ruta_imagen_carta_png)
            plt.imshow(imagen_carta)
            plt.axis('off')
            plt.show()
        else:
            imagen_carta = mpimg.imread(ruta_imagen_carta_jpg)
            plt.imshow(imagen_carta)
            plt.axis('off')
            plt.show()