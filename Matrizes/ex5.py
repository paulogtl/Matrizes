pontos = [
    [10, 12, 8, 9],
    [7, 11, 10, 13],
    [9, 10, 12, 11]
]

totais = [sum(time) for time in pontos]
maior = max(totais)
indice = totais.index(maior)
print(f"O time {indice+1} teve a maior pontuação total: {maior} pontos")