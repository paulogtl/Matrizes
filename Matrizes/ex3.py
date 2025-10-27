agenda = [
    ["Ana", "Bruno", "Carlos"],
    ["Diana", "Eduardo", "Fernanda"],
    ["Gustavo", "Helena", "Igor"],
    ["Joana", "Kleber", "Laura"],
    ["Marcos", "Nina", "Otávio"]
]

print("Agenda semanal:")
dias = ["Seg", "Ter", "Qua", "Qui", "Sex"]
for i in range(5):
    print(f"{dias[i]}: {', '.join(agenda[i])}")