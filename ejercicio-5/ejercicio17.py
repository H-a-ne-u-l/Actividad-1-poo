import math


class Circulo:

    @staticmethod
    def calcular_area(radio: float) -> float:
        return math.pi * (radio**2)

    @staticmethod
    def calcular_longitud(radio: float) -> float:
        return 2 * math.pi * radio


def main():
    radio = float(input("Ingrese el radio del circulo: "))

    area = Circulo.calcular_area(radio)
    longitud = Circulo.calcular_longitud(radio)

    print(f"El area del circulo es: {area}")
    print(f"La longitud de la circunferencia es: {longitud}")


if __name__ == "__main__":
    main()
