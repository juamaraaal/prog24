# JOGO DA VELHA em Python
# AUTOR: Edson Luiz Parisotto
# Professor de programação
# www.parisotto.net
# modificado por júlia amaral em 15/10/24
# 
# Cria uma lista chamada 'casas' para representar as posições no tabuleiro
casas = []
i = 1

# Inicializa as casas do tabuleiro como vazias (espaços)
while i <= 9:
    casas.append(" ")  # Adiciona um espaço em branco para cada casa
    i += 1

# Inicializa o número da jogada e define o primeiro jogador
jogada = 1
jogador = "0"  # Pode ser melhor iniciar como "X" ou "O"

# Loop principal do jogo
while jogada <= 10:  # O jogo pode ter no máximo 10 jogadas
    casa = 1

    # Monta e imprime a grade do tabuleiro
    print("##### JOGO DA VELHA #####")
    print("=" * 25)
    for indice, valor in enumerate(casas):
        if indice != 2 and indice != 5 and indice != 8:
            print(f" {valor} |", end='')  # Imprime o valor da casa com uma barra vertical
        else:
            # Quando chega a um final de linha, imprime os números das casas
            print(f" {valor}     {casa} | {casa+1} | {casa+2}")
            casa += 3  # Atualiza a casa para a próxima linha
            if indice != 8: print("---|---|---   ---|---|---")  # Imprime separadores entre as linhas
    print("=" * 25)

    # Verifica se alguém ganhou (deu velha)
    velha = []
    if jogada >= 5:  # Verifica a partir da quinta jogada
        # Adiciona condições de vitória à lista 'velha'
        velha.append(casas[0] != " " and casas[0] == casas[1] and casas[0] == casas[2])  # Linha 1
        velha.append(casas[3] != " " and casas[3] == casas[4] and casas[3] == casas[5])  # Linha 2
        velha.append(casas[6] != " " and casas[6] == casas[7] and casas[6] == casas[8])  # Linha 3
        velha.append(casas[0] != " " and casas[0] == casas[3] and casas[0] == casas[6])  # Coluna 1
        velha.append(casas[1] != " " and casas[1] == casas[4] and casas[1] == casas[7])  # Coluna 2
        velha.append(casas[2] != " " and casas[2] == casas[5] and casas[2] == casas[8])  # Coluna 3
        velha.append(casas[0] != " " and casas[0] == casas[4] and casas[0] == casas[8])  # Diagonal \
        velha.append(casas[2] != " " and casas[2] == casas[4] and casas[2] == casas[6])  # Diagonal /

        # Se alguém ganhou, imprime o resultado e sai do jogo
        if True in velha:
            print(f"Deu VELHA! Venceu o jogador \"{jogador}\"!")
            exit()

    # Alterna o jogador
    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"

    # Define a jogada do jogador
    while jogada < 10:  # Permite até 9 jogadas
        # Solicita ao jogador que escolha uma casa
        casa = int(input(f"Vez do jogador \"{jogador}\"!\nEscolha uma casinha: "))
        if casa > 9 or casa < 1:  # Verifica se a casa escolhida é válida
            print(f"{casa} não é uma casa válida.")
        elif casas[casa-1] != " ":  # Verifica se a casa já está ocupada
            print(f"{casa} já está ocupada.")
        else:
            break  # Sai do loop se a entrada é válida

    # Grava a jogada no tabuleiro
    if jogada < 10:
        casas[casa-1] = jogador  # Atualiza a casa com o símbolo do jogador

    if jogada < 10: print(f"\n" * 10)  # Limpa a tela (não é a melhor prática, mas funciona)

    jogada += 1  # Incrementa o número da jogada

# Se o loop termina, significa que deu empate
print("Empate! Fim do Jogo da Velha")
