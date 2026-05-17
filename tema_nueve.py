from sympy import Pow
import sympy as sp
import random
from scipy import stats

#Medidas de tendencia central y dispersión

class TemaNueve:
    def __init__(self):
        self.definicion = "La moda es el valor que más se repite en un conjunto de datos.\nLa mediana es el valor que se encuentra en la posición central de un conjunto de datos ordenado.\nLa media es el promedio de los valores de un conjunto de datos.\nLa desviación estándar es la raíz cuadrada de la varianza y mide la dispersión de los datos con respecto a la media. \nLa varianza es el promedio de las diferencias al cuadrado entre cada valor y la media."
        self.titulo = "Medidas de tendencia central y dispersión"
        self.datos = []
        self.sumaVarianza = 0
        self.media = 0

    def conjuntoNumeros(self):
        self.datos = []
        for i in range(0, 30):
            self.datos.append(random.randint(1, 100))

    def calculateModa(self):
        moda = stats.mode(self.datos)
        return moda.mode
    
    def calculateMedia(self):
        suma = 0
        for valor in self.datos:
            suma += valor

        self.media = suma / len(self.datos)
        return self.media
    
    def calculateMediana(self):
        self.datos.sort()
        
        n = len(self.datos)
        mediana = (self.datos[n//2 - 1] + self.datos[n//2]) / 2
        return mediana


    def calculateDesviacionPoblacional(self):
        desviacionPoblacional = sp.sqrt(self.calculateVarianzaPoblacional())
        return desviacionPoblacional            

    def calculateVarianzaPoblacional(self):
        self.sumaVarianza = 0
        for valor in self.datos:
            self.sumaVarianza += Pow(valor - self.media, 2)
        
        varianzaPoblacional = self.sumaVarianza / len(self.datos)
        return varianzaPoblacional
    
    def calculateVarianzaMuestral(self):
        varianzaMuestral = self.sumaVarianza / (len(self.datos) - 1)
        return varianzaMuestral
    
    def calculateDesviacionMuestral(self):
        desviacionMuestral = sp.sqrt(self.calculateVarianzaMuestral())
        return desviacionMuestral

        
    
