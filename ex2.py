# O código permite que os jogadores escolham o tamanho do tabuleiro e, em seguida, joguem o jogo da velha. Ele usa uma abordagem de matriz para representar o tabuleiro, permitindo a verificação das condições de vitória em linhas, colunas e diagonais. O jogo continua até que um jogador vença ou ocorra um empate.

# Detalhamento das Estruturas Usadas:


# criar_tabuleiro(dimensao):
# Esta função cria um tabuleiro vazio de dimensão dimensao x dimensao.
# Utiliza list comprehensions para criar uma matriz de strings inicialmente preenchida com espaços em branco.


# exibir_tabuleiro(tabuleiro):
# Esta função recebe o tabuleiro como entrada e o exibe na saída padrão.
# Calcula a dimensão do tabuleiro a partir do comprimento de uma linha.
# Itera pelas linhas do tabuleiro e exibe cada linha separada por barras verticais ("|").
# Utiliza um linha de hifens ("-") para criar a separação entre as linhas.


# verificar_vitoria(tabuleiro, jogador):
# Esta função verifica se um jogador venceu o jogo.
# Calcula a dimensão do tabuleiro.
# Verifica vitória em linhas e colunas usando loops for.
# Verifica vitória nas diagonais principais e secundárias.
# Retorna True se houver uma vitória e False caso contrário.


# jogar_jogo():

# Esta função é a principal e controla o jogo.
# Solicita ao jogador a dimensão desejada do tabuleiro.
# Inicializa o tabuleiro usando criar_tabuleiro.
# Começa o loop principal do jogo, que continua até que um jogador vença ou ocorra um empate.
# Exibe o tabuleiro usando exibir_tabuleiro.
# Solicita ao jogador que escolha uma linha e coluna para colocar sua marca.
# Verifica se a entrada do jogador é válida (dentro dos limites do tabuleiro e célula não ocupada).
# Atualiza o tabuleiro com a marca do jogador.
# Verifica se o jogador atual venceu usando verificar_vitoria.
# Alternar para o próximo jogador ("X" para "O" ou vice-versa).
# Se o loop terminar sem uma vitória, é declarado um empate.


def criar_tabuleiro(dimensao):
    """
    Cria um tabuleiro vazio de dimensão `dimensao x dimensao`.

    Args:
        dimensao (int): A dimensão do tabuleiro (número de linhas e colunas).

    Returns:
        list: Uma matriz representando o tabuleiro inicializado com espaços em branco.
    """
    return [[" " for _ in range(dimensao)] for _ in range(dimensao)]

def exibir_tabuleiro(tabuleiro):
    """
    Exibe o tabuleiro na saída padrão.

    Args:
        tabuleiro (list): O tabuleiro do jogo representado como uma matriz de strings.

    Returns:
        None
    """
    dimensao = len(tabuleiro)
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * (4 * dimensao - 1))

def verificar_vitoria(tabuleiro, jogador):
    """
    Verifica se um jogador venceu o jogo.

    Args:
        tabuleiro (list): O tabuleiro do jogo representado como uma matriz de strings.
        jogador (str): O jogador atual ("X" ou "O").

    Returns:
        bool: True se o jogador venceu, False caso contrário.
    """
    dimensao = len(tabuleiro)
    
    # Verificar linhas e colunas
    for i in range(dimensao):
        if all(tabuleiro[i][j] == jogador for j in range(dimensao)) or all(tabuleiro[j][i] == jogador for j in range(dimensao)):
            return True
    
    # Verificar diagonais
    if all(tabuleiro[i][i] == jogador for i in range(dimensao)) or all(tabuleiro[i][dimensao - 1 - i] == jogador for i in range(dimensao)):
        return True

    return False

def jogar_jogo():
    """
    Função principal que permite aos jogadores jogar o jogo da velha com dimensão variável.

    Returns:
        None
    """
    dimensao = int(input("Digite a dimensão do tabuleiro (quadrado): "))
    tabuleiro = criar_tabuleiro(dimensao)
    jogador_atual = "X"

    for _ in range(dimensao ** 2):
        exibir_tabuleiro(tabuleiro)
        print(f"É a vez do jogador {jogador_atual}")
        
        while True:
            try:
                linha = int(input(f"Digite o número da linha (0-{dimensao - 1}): "))
                coluna = int(input(f"Digite o número da coluna (0-{dimensao - 1}): "))

                if 0 <= linha < dimensao and 0 <= coluna < dimensao:
                    if tabuleiro[linha][coluna] == " ":
                        tabuleiro[linha][coluna] = jogador_atual
                        break
                    else:
                        print("Essa célula já está ocupada. Tente novamente.")
                else:
                    print(f"Valores fora do intervalo permitido (0-{dimensao - 1}). Tente novamente.")
            except ValueError:
                print("Entrada inválida. Informe um número válido para linha e coluna.")

        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break

        # Alternar para o próximo jogador
        jogador_atual = "X" if jogador_atual == "O" else "O"
    else:
        exibir_tabuleiro(tabuleiro)
        print("Empate! O jogo terminou sem vencedor.")

if __name__ == "__main__":
    jogar_jogo()
