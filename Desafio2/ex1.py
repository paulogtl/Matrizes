import random

def criar_tabuleiro(linhas, colunas, qtd_minas):
    tabuleiro = [[' ' for _ in range(colunas)] for _ in range(linhas)]
    minas = 0
    while minas < qtd_minas:
        l = random.randint(0, linhas - 1)
        c = random.randint(0, colunas - 1)
        if tabuleiro[l][c] != 'M':
            tabuleiro[l][c] = 'M'
            minas += 1
    return tabuleiro

def mostrar_tabuleiro(tabuleiro, revelado):
    print("   " + " ".join(str(i) for i in range(len(tabuleiro[0]))))
    for i in range(len(tabuleiro)):
        linha = []
        for j in range(len(tabuleiro[0])):
            if revelado[i][j]:
                if tabuleiro[i][j] == 'M':
                    linha.append('M')
                else:
                    linha.append(str(contar_minas_vizinhas(tabuleiro, i, j)))
            else:
                linha.append('-')
        print(f"{i}  " + " ".join(linha))

def contar_minas_vizinhas(tabuleiro, linha, coluna):
    total = 0
    for i in range(linha - 1, linha + 2):
        for j in range(coluna - 1, coluna + 2):
            if 0 <= i < len(tabuleiro) and 0 <= j < len(tabuleiro[0]):
                if tabuleiro[i][j] == 'M':
                    total += 1
    return total

def jogar(tabuleiro):
    linhas = len(tabuleiro)
    colunas = len(tabuleiro[0])
    revelado = [[False for _ in range(colunas)] for _ in range(linhas)]
    total_seguras = linhas * colunas - sum(row.count('M') for row in tabuleiro)
    abertas = 0

    while True:
        mostrar_tabuleiro(tabuleiro, revelado)
        try:
            linha = int(input("Digite a linha: "))
            coluna = int(input("Digite a coluna: "))
            if not (0 <= linha < linhas and 0 <= coluna < colunas):
                print("Coordenadas inválidas. Tente novamente.")
                continue
        except ValueError:
            print("Entrada inválida. Use números inteiros.")
            continue

        if revelado[linha][coluna]:
            print("Essa célula já foi revelada.")
            continue

        revelado[linha][coluna] = True

        if tabuleiro[linha][coluna] == 'M':
            mostrar_tabuleiro(tabuleiro, revelado)
            print("💥 Você explodiu uma mina! Game Over.")
            break
        else:
            abertas += 1
            if abertas == total_seguras:
                mostrar_tabuleiro(tabuleiro, revelado)
                print("🎉 Parabéns! Você venceu o jogo.")
                break

# Execução do jogo
if __name__ == "__main__":
    linhas = 5
    colunas = 5
    qtd_minas = 5
    tabuleiro = criar_tabuleiro(linhas, colunas, qtd_minas)
    jogar(tabuleiro)