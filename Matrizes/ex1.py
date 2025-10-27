temperaturas = [
    [22.5, 23.0, 21.8],
    [24.1, 23.9, 24.5],
    [20.0, 19.8, 20.2],
    [25.0, 24.5, 25.2],
    [22.0, 22.3, 22.1]
]

for i, sala in enumerate(temperaturas):
    media = sum(sala) / len(sala)
    print(f"Sala {i+1}: média de temperatura = {media:.2f}°C")