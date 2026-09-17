class Potencias:

    @staticmethod
    def calcular_cuadrado(numero: float) -> float:
        return numero ** 2

    @staticmethod
    def calcular_cubo(numero: float) -> float:
        return numero ** 3


def main():
    numero = float(input("Ingrese un numero: "))

    cuadrado = Potencias.calcular_cuadrado(numero)
    cubo = Potencias.calcular_cubo(numero)

    print(f"El cuadrado de {numero} es: {cuadrado}")
    print(f"El cubo de {numero} es: {cubo}")


if __name__ == "__main__":
    main()
