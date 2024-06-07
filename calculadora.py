class Calculadora:
    @staticmethod
    def somar(numero1, numero2):
        return numero1 + numero2

    @staticmethod
    def subtrair(numero1, numero2):
        return numero1 - numero2

    @staticmethod
    def multiplicar(numero1, numero2):
        return numero1 * numero2

    @staticmethod
    def dividir(numero1, numero2):
        if numero2 != 0:
            return numero1 / numero2
        else:
            raise ValueError("Não é possível dividir por zero")