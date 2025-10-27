try:
    numero = int(input("Digite um número: "))
    if numero > 10:
        print("Número válido!")
    else:
        print("Número menor ou igual a 10.")
except ValueError:
    print("Erro: Entrada inválida. Digite um número inteiro.")
else:
    print("Programa executado com sucesso.")
finally:
    print("Programa encerrado.")