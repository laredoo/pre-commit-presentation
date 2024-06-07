from numero import Numero

def inserir_numero():
    try:
        valor = float(input("Insira um número: "))
        return Numero(valor)
    except ValueError:
        print("Entrada inválida. Tente novamente.")
        return inserir_numero()