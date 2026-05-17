from customtkinter.windows.widgets import core_widget_classes
import sympy as sp

#Regla Multiplicativa / Regla de Multiplicación

class TemaOcho:
    def __init__(self):
        self.definicion="La regla del producto (o regla de la multiplicación) en probabilidad se utiliza para calcular la probabilidad de que dos o más eventos ocurran al mismo tiempo, o de forma sucesiva."
        self.problema = (
            "Tienes una caja de chocolates artesanales. Sabes que dentro hay 'x' chocolates rellenos de cajeta y 'z' chocolates rellenos de menta. Todos se ven exactamente iguales por fuera.\n\n"
            "Tienes mucha hambre, así que decides sacar un chocolate al azar, comértelo, y luego sacar un segundo chocolate inmediatamente después.\n\n"
            "¿Cuál es la probabilidad de sacar primero un chocolate de Cajeta/Menta y de segundo otro de Cajeta/Menta?"
        )
        self.cantidad_cajeta=0
        self.cantidad_menta=0
        self.cantidad_total= self.cantidad_cajeta + self.cantidad_menta
        self.evento_a = 0
        self.evento_b = 0

    def calcular_probabilidad(self):
        probabilidad = 0.0
        procedimiento = ""
        self.cantidad_total= self.cantidad_cajeta + self.cantidad_menta
        match self.evento_a:
            case(1):
                cant_a = self.cantidad_cajeta
                print("Caso 1: Cajeta")
                match self.evento_b:
                    case(1):
                        cant_b = self.cantidad_cajeta
                        print("Caso 1: Cajeta")
                        probabilidad = (self.cantidad_cajeta/self.cantidad_total) * (self.cantidad_cajeta-1)/(self.cantidad_total-1)
                        procedimiento = f"Probabilidad = ({self.cantidad_cajeta}/{self.cantidad_total}) * ({self.cantidad_cajeta-1}/{self.cantidad_total-1}) = {probabilidad:.4f}"
                    case(2):
                        cant_b = self.cantidad_menta
                        print("Caso 2: Menta")
                        probabilidad = (self.cantidad_cajeta/self.cantidad_total) * (self.cantidad_menta)/(self.cantidad_total-1)
                        procedimiento = f"Probabilidad = ({self.cantidad_cajeta}/{self.cantidad_total}) * ({self.cantidad_menta}/{self.cantidad_total-1}) = {probabilidad:.4f}"
                
            case(2):
                cant_a = self.cantidad_menta
                print("Caso 2: Menta")
                match self.evento_b:
                    case(1):
                        cant_b = self.cantidad_cajeta
                        print("Caso 1: Cajeta")
                        probabilidad = (self.cantidad_menta/self.cantidad_total) * (self.cantidad_cajeta)/(self.cantidad_total-1)
                        procedimiento = f"Probabilidad = ({self.cantidad_menta}/{self.cantidad_total}) * ({self.cantidad_cajeta}/{self.cantidad_total-1}) = {probabilidad:.4f}"
                    case(2):
                        cant_b = self.cantidad_menta
                        print("Caso 2: Menta")
                        probabilidad = (self.cantidad_menta/self.cantidad_total) * (self.cantidad_menta-1)/(self.cantidad_total-1)
                        procedimiento = f"Probabilidad = ({self.cantidad_menta}/{self.cantidad_total}) * ({self.cantidad_menta-1}/{self.cantidad_total-1}) = {probabilidad:.4f}"

        return probabilidad, procedimiento
                    

                

        

        
        