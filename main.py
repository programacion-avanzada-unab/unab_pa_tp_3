from src.punto import Punto

def main():
    print("=== PRUEBA CLASE PUNTO ===")
    p1 = Punto(2, 3)
    print("Punto: ", p1.impresion())
    opuesto_p1 = p1.opuesto()
    print("Punto opuesto: ", opuesto_p1.impresion())

if __name__ == "__main__":
    main()