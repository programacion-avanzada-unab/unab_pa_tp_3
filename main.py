from src.punto import Punto
from src.linea import Linea

def main():
    print("=== PRUEBA CLASE PUNTO ===")
    p1 = Punto(2, 3)
    print("Punto: ", p1.impresion())
    opuesto_p1 = p1.opuesto()
    print("Punto opuesto: ", opuesto_p1.impresion())

    print("=== PRUEBA CLASE Linea ===")
    p2 = Punto(5, 8)
    linea = Linea(p1,p2)
    print("Linea: ", linea)
    linea.mueve_arriba(2)
    print("Linea: ", linea)

if __name__ == "__main__":
    main()