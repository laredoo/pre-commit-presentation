class Numero:
    def __init__(self, valor):
        self.valor = valor

    def __add__(self, other):
        return self.valor + other.valor

    def __sub__(self, other):
        return self.valor - other.valor

    def __mul__(self, other):
        return self.valor * other.valor

    def __truediv__(self, other):
        if other.valor != 0:
            return self.valor / other.valor
        else:
            raise ValueError("Não é possível dividir por zero")
        
    def __eq__(self, other):
        return self.valor == other.valor

    def __ne__(self, other):
        return self.valor != other.valor

    def __lt__(self, other):
        return self.valor < other.valor

    def __gt__(self, other):
        return self.valor > other.valor

    def __le__(self, other):
        return self.valor <= other.valor

    def __ge__(self, other):
        return self.valor >= other.valor