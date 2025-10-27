horarios = [
    ["06:00", "12:00", "18:00"],
    ["07:00", "13:00", "19:00"],
    ["08:00", "14:00", "20:00"],
    ["09:00", "15:00", "21:00"]
]

linha = int(input("Digite o número da linha (1 a 4): ")) - 1
if 0 <= linha < 4:
    print(f"Horários da linha {linha+1}: {', '.join(horarios[linha])}")
else:
    print("Linha inválida.")