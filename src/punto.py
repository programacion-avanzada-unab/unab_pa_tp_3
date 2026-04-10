"""
Crear la clase Punto con dos atributos x e y (ambos numéricos), con el correspondiente constructor
que recibe ambos valores.
● Definir métodos tales como:
○ eje_x, eje_y
○ impresion (devuelve en representación de string ambos valores)
○ opuesto (devuelve el punto opuesto)
○ Cualquier otro método que considere importante
"""

class Punto:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def eje_x(self):
        return self.x

    def eje_y(self):
        return self.y

    def impresion(self):
        return f"({self.x},{self.y})"

    def opuesto(self):
        """Si tengo el punto (5,3) me devuelve (-5,-3)"""
        factor = -1
        return Punto(self.x*factor, self.y*factor)
    
