class Seguimiento:

    @staticmethod
    def calcular_primera_suma(suma: float, x: float) -> float:
        return suma + x

    @staticmethod
    def calcular_nuevo_x(x: float, y: float) -> float:
        return x + (y ** 2)

    @staticmethod
    def calcular_suma_final(suma: float, x: float, y: float) -> float:
        return suma + (x / y)


def main():
    suma = 0.0
    x = 20.0

    suma = Seguimiento.calcular_primera_suma(suma, x)

    y = 40.0

    x = Seguimiento.calcular_nuevo_x(x, y)

    suma = Seguimiento.calcular_suma_final(suma, x, y)

    print(f"EL VALOR DE LA SUMA ES: {suma}")


if __name__ == "__main__":
    main()
