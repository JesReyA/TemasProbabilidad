import os
import random
import matplotlib.pyplot as plt
from matplotlib import image as mpimg


numero_aleatorio_carta = random.randint(1,13)
numero_aleatorio_tipo_carta = random.randint(1,4)

if numero_aleatorio_tipo_carta == 1:
    tipo_carta = "Corazones"
elif numero_aleatorio_tipo_carta == 2:
    tipo_carta = "Espadas"
elif numero_aleatorio_tipo_carta == 3:
    tipo_carta = "Diamantes"
else:
    tipo_carta = "Trebol"

ruta_imagen_carta_png = f"imagenes/{numero_aleatorio_carta}{tipo_carta}.png"
ruta_imagen_carta_jpg = f"imagenes/{numero_aleatorio_carta}{tipo_carta}.jpg"

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