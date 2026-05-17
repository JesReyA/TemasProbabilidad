import sympy as sp

#Teorema de Bayes

class TemaCuatro:
    def __init__(self):
        self.definicion = "El teorema de Bayes es una fórmula matemática que determina la probabilidad condicional, es decir, la posibilidad de que algo ocurra basándose en lo sucedido en situaciones similares. Puede ayudar a revisar o actualizar una predicción o teoría existente a la luz de nuevas evidencias. "
        self.problema="""Un restaurante de hamburguesas tiene convenio con 3 aplicaciones de entrega a domicilio para repartir sus pedidos.
        \nUberEats maneja 4 de cada 10 pedidos (40%) y tiene una tasa de entrega a tiempo del 90%.
        \nDiDi Food maneja el 35% de los pedidos y tiene una tasa de entrega a tiempo del 85%.
        \nRappi maneja el 25% de los pedidos restantes y tiene una tasa de entrega a tiempo del 95%.
        \nUn cliente llama furioso al restaurante para quejarse de que su comida llegó tarde. ¿Cuál es la probabilidad de que ese pedido haya sido entregado por DiDi Food?"""
        self.p_UberEats = 0.4
        self.p_DiDiFood = 0.35
        self.p_Rappi = 0.25
        self.p_UberEats_a_tiempo = 0.9
        self.p_DiDiFood_a_tiempo = 0.85
        self.p_Rappi_a_tiempo = 0.95
        self.p_UberEats_tarde = 1- self.p_UberEats_a_tiempo
        self.p_DiDiFood_tarde = 1- self.p_DiDiFood_a_tiempo
        self.p_Rappi_tarde = 1- self.p_Rappi_a_tiempo

    def calcular_probabilidad(self):
        probabilidad_uno = self.p_DiDiFood_tarde * self.p_DiDiFood
        probabilidad_dos = self.p_UberEats_tarde * self.p_UberEats + self.p_DiDiFood_tarde * self.p_DiDiFood + self.p_Rappi_tarde * self.p_Rappi
        probabilidad_total = probabilidad_uno / probabilidad_dos
        return probabilidad_uno, probabilidad_dos, probabilidad_total