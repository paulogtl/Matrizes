import random

# Função para exibir o tabuleiro
def exibir_tabuleiro(tabuleiro):
    print("=== Tabuleiro ===")
    for linha in tabuleiro:
        print(" ".join(linha))

# Função para validar entrada do jogador
def obter_entrada(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if 0 <= valor <= 4:
                return valor
            else:
                print("Valor fora do intervalo. Digite um número entre 0 e 4.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro entre 0 e 4.")

# Função para fornecer dica de direção
def fornecer_dica(linha_jogador, coluna_jogador, linha_tesouro, coluna_tesouro):
    dica = []
    if linha_jogador < linha_tesouro:
        dica.append("mais para baixo")
    elif linha_jogador > linha_tesouro:
        dica.append("mais para cima")
    if coluna_jogador < coluna_tesouro:
        dica.append("mais para a direita")
    elif coluna_jogador > coluna_tesouro:
        dica.append("mais para a esquerda")
    print("O tesouro está " + " e ".join(dica) + ".")

# Inicialização do tabuleiro
tabuleiro = [["~" for _ in range(5)] for _ in range(5)]

# Posição aleatória do tesouro
linha_tesouro = random.randint(0, 4)
coluna_tesouro = random.randint(0, 4)

# Loop de tentativas
for tentativa in range(1, 8):
    exibir_tabuleiro(tabuleiro)
    print(f"Tentativa {tentativa} de 7")
    linha = obter_entrada("Escolha a linha (0-4): ")
    coluna = obter_entrada("Escolha a coluna (0-4): ")

    if linha == linha_tesouro and coluna == coluna_tesouro:
        tabuleiro[linha][coluna] = "T"
        exibir_tabuleiro(tabuleiro)
        print("Parabéns! Você encontrou o tesouro!")
        break
    else:
        if tabuleiro[linha][coluna] == "X":
            print("Você já tentou essa posição. Tente outra.")
        else:
            tabuleiro[linha][coluna] = "X"
            fornecer_dica(linha, coluna, linha_tesouro, coluna_tesouro)

# Se não encontrou o tesouro após 7 tentativas
else:
    tabuleiro[linha_tesouro][coluna_tesouro] = "T"
    exibir_tabuleiro(tabuleiro)
    print(f"Fim de jogo! O tesouro estava na posição ({linha_tesouro}, {coluna_tesouro}).")