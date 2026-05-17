import sympy as sp

class TemaTres:
    def __init__(self):
        self.definicion = "La probabilidad condicional es la probabilidad de que ocurra un evento A sabiendo que ha ocurrido un evento B. "
        self.problema= "En la FES Aragón, se sabe que el 15\% de los alumnos pertenecen a la carrera de Ingeniería en Computación, mientras que el 5\% la población estudiantil total utiliza el sistema operativo Linux. Además, se ha detectado que el 60% de los estudiantes de Ingeniería en Computación emplean Linux en sus equipos. Si se selecciona un alumno al azar y se descubre que utiliza Linux, ¿cuál es la probabilidad de que pertenezca a la carrera de Ingeniería en Computación?"
        self.probabilidad_ICO = 0.15
        self.probabilidad_Linux = 0.20
        self.probabilidad_ICO_y_Linux = 0.60

    def calcular_probabilidad_condicional(self):
        probabilidad_condicional_uno = self.probabilidad_ICO * self.probabilidad_ICO_y_Linux
        probabilidad = probabilidad_condicional_uno / self.probabilidad_Linux
        return probabilidad_condicional_uno, probabilidad
         