class Edades:

    @staticmethod
    def calcular_edalber(edjuan: float) -> float:
        return 2 * edjuan / 3

    @staticmethod
    def calcular_edana(edjuan: float) -> float:
        return 4 * edjuan / 3

    @staticmethod
    def calcular_edmama(edjuan: float, edalber: float, edana: float) -> float:
        return edjuan + edalber + edana


def main():
    edjuan = float(input("How old is Juan? "))

    edalber = Edades.calcular_edalber(edjuan)
    edana = Edades.calcular_edana(edjuan)
    edmama = Edades.calcular_edmama(edjuan, edalber, edana)

    print(f"la edad de la mama es: {edmama}")
    print(f"la edad de Juan es: {edjuan}")
    print(f"la edad de Alberto es: {edalber}")
    print(f"la edad de Ana es: {edana}")


if __name__ == "__main__":
    main()
