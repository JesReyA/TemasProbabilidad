import sympy as sp

class TemaDos:
    def __init__(self):
        self.definicion = "Eventos compuestos: Un evento compuesto es una combinación de dos o más eventos simples que ocurre al mismo tiempo. \nUn evento complementario es el evento que ocurre si y solo si otro evento no ocurre. \nUn evento disjunto es aquel que no puede ocurrir al mismo tiempo que otro evento. "
        self.eventos_disjuntos = "Seleccionar un alumno al azar y evaluar dos características independientes: \"El alumno cursa primer semestre\" Y \"El alumno viaja en metro a la escuela\". Que vaya en metro no cambia la probabilidad de su semestre."
        self.eventos_complementarios = "Al revisar un servidor de la escuela, el evento A es \"El servidor está activo\" y su complementario (A') es \"El servidor está caído\". No hay otra opción."
        self.eventos_compuestos = "Seleccionar a un alumno al azar y ver su carrera. Los eventos \"Estudiar Ingeniería en Computación\" y \"Estudiar Ingeniería Mecánica\" son disjuntos (asumiendo que no puedes estar inscrito en dos carreras simultáneamente)."
    
    def calcular_probabilidad_eventos_disjuntos(self, probabilidad_A, probabilidad_B):
        probabilidad_eventos_disjuntos = probabilidad_A + probabilidad_B
        return probabilidad_eventos_disjuntos
    
    def calcular_probabilidad_eventos_complementarios(self, probabilidad_A):
        probabilidad_eventos_complementarios = 1 - probabilidad_A
        return probabilidad_eventos_complementarios
    
    def calcular_probabilidad_eventos_compuestos(self,probabilidad_A, probabilidad_B):
        probabilidad_eventos_compuestos = probabilidad_A * probabilidad_B
        return probabilidad_eventos_compuestos