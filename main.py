from numero import Numero
from calculadora import Calculadora

from utils import inserir_numero

if __name__ == "__main__":

    while True:
        print("Operações disponíveis: + (soma), - (subtração), * (multiplicação), / (divisão)")
        print("Operações booleanas disponíveis: == (igual a), != (diferente de), < (menor que), > (maior que), <= (menor ou igual a), >= (maior ou igual a)")

        num1 = inserir_numero()
        operacao = input("Insira a operação desejada (+, -, *, /, ==, !=, <, >, <=, >=): ")
        
        if operacao in ['==', '!=', '<', '>', '<=', '>=']:
            num2 = inserir_numero()
        else:
            num2 = inserir_numero()

        if operacao == '+':
            resultado = Calculadora.somar(num1, num2)
        elif operacao == '-':
            resultado = Calculadora.subtrair(num1, num2)
        elif operacao == '*':
            resultado = Calculadora.multiplicar(num1, num2)
        elif operacao == '/':
            try:
                resultado = Calculadora.dividir(num1, num2)
            except ValueError as e:
                resultado = str(e)
        elif operacao == '==':
            resultado = num1 == num2
        elif operacao == '!=':
            resultado = num1 != num2
        elif operacao == '<':
            resultado = num1 < num2
        elif operacao == '>':
            resultado = num1 > num2
        elif operacao == '<=':
            resultado = num1 <= num2
        elif operacao == '>=':
            resultado = num1 >= num2

        print("Resultado:", resultado)


