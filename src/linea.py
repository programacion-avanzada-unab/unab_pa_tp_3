"""
Nivel 2: Clase Linea
Define una clase Línea con dos atributos: _punto_a y _punto_b. Son dos puntos por los que pasa la línea en un
espacio de dos dimensiones. Crear archivo linea.py dentro de src
La clase dispondrá de los siguientes métodos:
● Linea(Punto, Punto) Constructor que recibe como parámetros dos objetos de la clase Punto, que son
utilizados para inicializar los atributos.
● mueve_derecha(float) Desplaza la línea a la derecha la distancia que se indique.
● mueve_izquierda(float) Desplaza la línea a la izquierda la distancia que se indique.
● mueve_arriba(float) Desplaza la línea hacia arriba la distancia que se indique.
● mueve_abajo(float) Desplaza la línea hacia abajo la distancia que se indique
"""
from src.punto import Punto

class Linea:
    def __init__(self, punto_a, punto_b):
        self._punto_a = punto_a 
        self._punto_b = punto_b

    def mueve_derecha(self, desplazamiento):
        self._punto_a.x = self._punto_a.x + desplazamiento # self._punto_a.x += desplazamiento
        self._punto_b.x = self._punto_b.x + desplazamiento # self._punto_b.x += desplazamiento

    def mueve_izquierda(self, desplazamiento):
        self._punto_a.x = self._punto_a.x - desplazamiento # self._punto_a.x -= desplazamiento
        self._punto_b.x = self._punto_b.x - desplazamiento # self._punto_b.x -= desplazamiento

    def mueve_arriba(self, desplazamiento):
        self._punto_a.y = self._punto_a.y + desplazamiento # self._punto_a.y += desplazamiento
        self._punto_b.y = self._punto_b.y + desplazamiento # self._punto_b.y += desplazamiento

    def mueve_abajo(self, desplazamiento):
        self._punto_a.y = self._punto_a.y - desplazamiento # self._punto_a.y -= desplazamiento
        self._punto_b.y = self._punto_b.y - desplazamiento # self._punto_b.y -= desplazamiento

    def __str__(self):
        return f"{self._punto_a}---{self._punto_b}"