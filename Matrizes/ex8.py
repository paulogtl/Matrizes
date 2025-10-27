sala = [
    ["O", "X", "O", "O", "X", "O"],
    ["O", "O", "O", "X", "O", "O"],
    ["X", "X", "O", "O", "O", "X"],
    ["O", "O", "X", "O", "O", "O"],
    ["O", "X", "O", "X", "O", "X"]
]

print("Mapa de cadeiras:")
for i, fila in enumerate(sala):
    print(f"Fila {i+1}: {' '.join(fila)}")