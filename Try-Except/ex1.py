try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 / num2
except ValueError:
    print("Erro: Por favor, insira apenas números.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
else:
    print(f"Resultado da divisão: {resultado}")