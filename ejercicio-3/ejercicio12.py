class Nomina:

    @staticmethod
    def calcular_salario_bruto(horas: float, valor_hora: float) -> float:
        return horas * valor_hora

    @staticmethod
    def calcular_retencion(salario_bruto: float, porcentaje: float) -> float:
        return salario_bruto * (porcentaje / 100)

    @staticmethod
    def calcular_salario_neto(salario_bruto: float, retencion: float) -> float:
        return salario_bruto - retencion


def main():
    horas_trabajadas = 48.0
    valor_hora = 5000.0
    porcentaje_retencion = 12.5

    salario_bruto = Nomina.calcular_salario_bruto(horas_trabajadas, valor_hora)
    retencion = Nomina.calcular_retencion(salario_bruto, porcentaje_retencion)
    salario_neto = Nomina.calcular_salario_neto(salario_bruto, retencion)

    print(f"El salario bruto es: {salario_bruto}")
    print(f"La retencion en la fuente es: {retencion}")
    print(f"El salario neto es: {salario_neto}")


if __name__ == "__main__":
    main()
