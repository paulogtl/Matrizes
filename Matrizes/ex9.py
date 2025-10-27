repeticoes = [
    [10, 15, 20],
    [12, 18, 22],
    [14, 20, 25],
    [16, 22, 30]
]

for j in range(3):
    total = sum(repeticoes[i][j] for i in range(4))
    print(f"Exercício {j+1}: total de repetições = {total}")