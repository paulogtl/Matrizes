chuva = [
    [10, 12, 8, 9, 11, 13, 14],
    [7, 6, 5, 8, 9, 10, 11],
    [15, 14, 13, 12, 11, 10, 9]
]

totais = [sum(cidade) for cidade in chuva]
maior = max(totais)
indice = totais.index(maior)
print(f"A cidade {indice+1} teve mais chuva na semana: {maior} mm")