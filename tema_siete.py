import sympy as sp

#Probabilidad Aditiva / Regla de Adición

class TemaSiete:
    def __init__(self):
        self.definicion = "La Regla Aditiva es una fórmula utilizada en probabilidad para calcular la probabilidad de que ocurra el evento A o el evento B.\nLa regla de adición o regla de la suma, establece que si tenemos un evento A y un evento B, la probabilidad de que ocurra el evento A o el evento B se calcula de la siguiente manera:\nP(A⋃B) = P(A) + P(B) − P(A⋂B)"
        self.problema_uno="Una empresa quiere saber la probabilidad de que un joven elegido al azar esté suscrito a Netflix o a Spotify"
        self.problema_dos="Una fábrica de celulares audita sus equipos buscando que al menos tengan un tipo de defecto antes de enviarlos a reparación. Los defectos pueden ser en Pantalla (A), Batería (B) o Software (C)."
        self.problema_tres="Un hospital quiere saber la probabilidad de que un paciente en la sala de espera presente al menos uno de los 4 síntomas principales de un nuevo virus: Fiebre (A), Tos (B), Dolor Muscular (C) o Fatiga (D)."
        self.probabilidades_uno = []
        self.probabilidades_dos = []
        self.probabilidades_tres = []

    def calcular_probabilidad_dos_eventos(self):
        probabilidad_uno = self.probabilidades_uno[0]
        probabilidad_dos = self.probabilidades_uno[1]
        probabilidad_uno_y_dos = self.probabilidades_uno[2]
        probabilidad_uno_o_dos = probabilidad_uno + probabilidad_dos - probabilidad_uno_y_dos
        return probabilidad_uno_o_dos

    def calcular_probabilidad_tres_eventos(self):
        probabilidad_uno = self.probabilidades_dos[0]
        probabilidad_dos = self.probabilidades_dos[1]
        probabilidad_tres = self.probabilidades_dos[2]
        probabilidad_uno_y_dos = self.probabilidades_dos[3]
        probabilidad_uno_y_tres = self.probabilidades_dos[4]
        probabilidad_dos_y_tres = self.probabilidades_dos[5]
        probabilidad_uno_y_dos_y_tres = self.probabilidades_dos[6]
        probabilidad_uno_o_dos_o_tres = probabilidad_uno + probabilidad_dos + probabilidad_tres - probabilidad_uno_y_dos - probabilidad_uno_y_tres - probabilidad_dos_y_tres + probabilidad_uno_y_dos_y_tres
        return probabilidad_uno_o_dos_o_tres
        
    def calcular_probabilidad_cuatro_eventos(self):
        probabilidad_uno = self.probabilidades_tres[0]
        probabilidad_dos = self.probabilidades_tres[1]
        probabilidad_tres = self.probabilidades_tres[2]
        probabilidad_cuatro = self.probabilidades_tres[3]
        probabilidad_uno_y_dos = self.probabilidades_tres[4]
        probabilidad_uno_y_tres = self.probabilidades_tres[5]
        probabilidad_uno_y_cuatro = self.probabilidades_tres[6]
        probabilidad_dos_y_tres = self.probabilidades_tres[7]
        probabilidad_dos_y_cuatro = self.probabilidades_tres[8]
        probabilidad_tres_y_cuatro = self.probabilidades_tres[9]
        probabilidad_uno_y_dos_y_tres = self.probabilidades_tres[10]
        probabilidad_uno_y_dos_y_cuatro = self.probabilidades_tres[11]
        probabilidad_uno_y_tres_y_cuatro = self.probabilidades_tres[12]
        probabilidad_dos_y_tres_y_cuatro = self.probabilidades_tres[13]
        probabilidad_uno_y_dos_y_tres_y_cuatro = self.probabilidades_tres[14]
        probabilidad_uno_o_dos_o_tres_o_cuatro = probabilidad_uno + probabilidad_dos + probabilidad_tres + probabilidad_cuatro - probabilidad_uno_y_dos - probabilidad_uno_y_tres - probabilidad_uno_y_cuatro - probabilidad_dos_y_tres - probabilidad_dos_y_cuatro - probabilidad_tres_y_cuatro + probabilidad_uno_y_dos_y_tres + probabilidad_uno_y_dos_y_cuatro + probabilidad_uno_y_tres_y_cuatro + probabilidad_dos_y_tres_y_cuatro - probabilidad_uno_y_dos_y_tres_y_cuatro
        return probabilidad_uno_o_dos_o_tres_o_cuatro
