estoque = [
    [10, 15, 12],
    [5, 8, 6],
    [20, 18, 22],
    [7, 9, 10]
]

for i, produto in enumerate(estoque):
    total = sum(produto)
    print(f"Produto {i+1}: total em estoque = {total}")