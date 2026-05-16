import sympy as sp

class TemaSeis:
    def __init__(self):
        self.definicion = "La probabilidad Total es la suma de las probabilidades de los eventos individuales."
        self.probabilidad_evento_A = 0
        self.probabilidad_evento_B = 0
        self.probabilidad_programada = 0
        self.probabilidad_restante = 0
        self.desc_evento_A = "Calcular la probabilidad de que un paciente sufra una reacción alérgica grave a un medicamento de anestesia, \ndependiendo de si el procedimiento es de Urgencia o Programado (ya que en urgencias hay menos tiempo para revisar el historial médico del paciente)."
        self.desc_evento_B = "Una planta procesadora de leche quiere calcular la probabilidad total de que un lote de leche se contamine con \nbacterias antes de salir al mercado, dependiendo del método de pasteurización utilizado."
    
    def calcular_evento_A(self):
        self.probabilidad_restante = 1 - self.probabilidad_programada
        probabilidad_total = self.probabilidad_programada*self.probabilidad_evento_A + self.probabilidad_restante*self.probabilidad_evento_B
        return probabilidad_total
    
    def calcular_evento_B(self):
        self.probabilidad_restante = 1 - self.probabilidad_programada
        probabilidad_total = self.probabilidad_programada*self.probabilidad_evento_A + self.probabilidad_restante*self.probabilidad_evento_B
        return probabilidad_total