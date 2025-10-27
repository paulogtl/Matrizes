notas = [
    [7.5, 8.0, 6.5],
    [9.0, 8.5, 9.5],
    [6.0, 7.0, 6.5],
    [8.5, 9.0, 8.0]
]

print("Média de cada aluno:")
for i, aluno in enumerate(notas):
    media = sum(aluno) / len(aluno)
    print(f"Aluno {i+1}: {media:.2f}")

print("\nMédia de cada prova:")
for j in range(3):
    media = sum(notas[i][j] for i in range(4)) / 4
    print(f"Prova {j+1}: {media:.2f}")