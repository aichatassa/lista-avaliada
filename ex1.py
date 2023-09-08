# O código cria um jogo da velha 4x4 onde dois jogadores, "X" e "O", se alternam para preencher células vazias no tabuleiro. O objetivo é que um jogador forme uma linha, coluna ou diagonal completa com suas marcações antes do adversário ou que todas as células sejam preenchidas, resultando em um empate.

# Detalhamento das Estruturas Usadas:


# exibir_tabuleiro(tabuleiro):
# Esta função recebe o tabuleiro como entrada e o exibe no formato de um tabuleiro 4x4 no console.
# Itera pelas linhas do tabuleiro e imprime cada linha separada por barras verticais ("|").
# Utiliza uma linha de hífens ("-") para criar a separação entre as linhas.


# verificar_vitoria(tabuleiro, jogador):
# Esta função verifica se um jogador venceu o jogo.
# Primeiro, verifica todas as linhas do tabuleiro para ver se todas as células em uma linha contêm a marcação do jogador.
# Em seguida, verifica todas as colunas do tabuleiro para ver se todas as células em uma coluna contêm a marcação do jogador.
# Também verifica as duas diagonais principais para determinar se todas as células nelas contêm a marcação do jogador.
# Retorna True se houver uma vitória e False caso contrário.


# jogar_jogo():
# Esta função é a principal e controla o jogo.
# Inicializa o tabuleiro como uma matriz 4x4 preenchida com espaços em branco.
# Define jogador_atual como "X" para começar.
# Inicia um loop que permite que os jogadores alternem entre si até que haja um vencedor ou empate (total de 16 jogadas).
# Exibe o tabuleiro atual usando exibir_tabuleiro e informa qual jogador deve jogar.
# Solicita ao jogador que insira uma linha e uma coluna para sua jogada.
# Verifica se as entradas do jogador são válidas (0 a 3) e se a célula está vazia.
# Atualiza o tabuleiro com a marcação do jogador.
# Verifica se o jogador atual venceu usando verificar_vitoria. Se vencer, o jogo é encerrado.
# Alternar para o próximo jogador ("X" se o jogador atual for "O" e vice-versa).
# Se o loop terminar sem uma vitória, declara um empate.

def exibir_tabuleiro(tabuleiro):
    """
    Exibe o tabuleiro na saída padrão.

    Args:
        tabuleiro (list): O tabuleiro do jogo representado como uma matriz de strings.

    Returns:
        None
    """
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 23)

def verificar_vitoria(tabuleiro, jogador):
    """
    Verifica se um jogador venceu o jogo.

    Args:
        tabuleiro (list): O tabuleiro do jogo representado como uma matriz de strings.
        jogador (str): O jogador atual ("X" ou "O").

    Returns:
        bool: True se o jogador venceu, False caso contrário.
    """
    for linha in tabuleiro:
        if all(cell == jogador for cell in linha):
            return True

    for coluna in range(4):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(4)):
            return True

    if all(tabuleiro[i][i] == jogador for i in range(4)) or all(tabuleiro[i][3 - i] == jogador for i in range(4)):
        return True

    return False

def jogar_jogo():
    """
    Função principal que permite aos jogadores jogar o jogo da velha 4x4.

    Returns:
        None
    """
    tabuleiro = [[" " for _ in range(4)] for _ in range(4)]
    jogador_atual = "X"

    for _ in range(16):
        exibir_tabuleiro(tabuleiro)
        print(f"É a vez do jogador {jogador_atual}")

        while True:
            try:
                linha = int(input("Digite o número da linha (0-3): "))
                coluna = int(input("Digite o número da coluna (0-3): "))

                if 0 <= linha <= 3 and 0 <= coluna <= 3:
                    if tabuleiro[linha][coluna] == " ":
                        tabuleiro[linha][coluna] = jogador_atual
                        break
                    else:
                        print("Essa célula já está ocupada. Tente novamente.")
                else:
                    print("Valores fora do intervalo permitido (0-3). Tente novamente.")
            except ValueError:
                print("Entrada inválida. Informe um número de 0 a 3 para linha e coluna.")

        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break

        jogador_atual = "X" if jogador_atual == "O" else "O"
    else:
        exibir_tabuleiro(tabuleiro)
        print("Empate! O jogo terminou sem vencedor.")

if __name__ == "__main__":
    jogar_jogo()
