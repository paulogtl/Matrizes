vendas = [
    [100, 120, 130, 110, 115, 140, 150],
    [80, 90, 85, 88, 92, 95, 100],
    [60, 65, 70, 75, 80, 85, 90],
    [50, 55, 60, 65, 70, 75, 80],
    [30, 35, 40, 45, 50, 55, 60]
]

for i, produto in enumerate(vendas):
    total = sum(produto)
    print(f"Produto {i+1}: receita semanal = R${total}")