# O código cria um jogo onde o jogador deve adivinhar uma palavra oculta. O programa carrega uma lista de palavras de um arquivo de texto chamado "lista_palavras.txt", escolhe aleatoriamente uma palavra dessa lista e desafia o jogador a adivinhá-la. O jogador tem um número limitado de tentativas para adivinhar a palavra, e o programa fornece feedback sobre as letras corretas e incorretas.

# Detalhamento das Estruturas Usadas:


# carregar_palavras(nome_arquivo):
# Esta função recebe o nome de um arquivo como entrada.
# Abre o arquivo especificado no modo de leitura ('r').
# Lê cada linha do arquivo, remove qualquer espaço em branco extra e armazena as palavras em uma lista.
# Retorna a lista de palavras.


# escolher_palavra(lista_palavras):
# Esta função recebe a lista de palavras como entrada.
# Utiliza o módulo random para escolher aleatoriamente uma palavra da lista.
# Retorna a palavra escolhida.


# exibir_palavra_escondida(palavra, letras_adivinhadas):
# Esta função recebe a palavra a ser adivinhada e um conjunto de letras adivinhadas como entrada.
# Cria uma string vazia chamada palavra_escondida.
# Itera através das letras na palavra oculta:
# Se a letra estiver no conjunto de letras adivinhadas, ela é adicionada à palavra_escondida.
# Caso contrário, um caractere de sublinhado ("_") é adicionado à palavra_escondida.
# Retorna a palavra_escondida resultante.


# jogar_jogo(palavra):
# Esta função é o núcleo do jogo.
# Inicializa um conjunto vazio chamado letras_adivinhadas para armazenar as letras que o jogador já adivinhou.
# Define um limite de tentativas (6 neste caso).
# Entra em um loop enquanto o número de tentativas for maior que zero.
# A cada iteração do loop, exibe a palavra oculta usando a função exibir_palavra_escondida, o número de tentativas restantes e as letras que o jogador já tentou adivinhar.
# Solicita ao jogador que insira uma única letra.
# Verifica se a entrada do jogador é válida (uma única letra do alfabeto).
# Verifica se a letra já foi adivinhada antes.
# Adiciona a letra ao conjunto letras_adivinhadas.
# Verifica se a letra faz parte da palavra oculta e atualiza as tentativas restantes conforme necessário.
# Se o jogador adivinhar todas as letras da palavra, exibe uma mensagem de parabéns e sai do loop.
# Se o jogador esgotar todas as tentativas, exibe uma mensagem de "Game Over" com a palavra correta.


import random

def carregar_palavras(nome_arquivo):
    """
    Carrega uma lista de palavras a partir de um arquivo de texto.

    Args:
        nome_arquivo (str): O nome do arquivo contendo as palavras.

    Returns:
        list: Uma lista de palavras lidas do arquivo.
    """
    with open(nome_arquivo, 'r') as arquivo:
        return [linha.strip() for linha in arquivo]

def escolher_palavra(lista_palavras):
    """
    Escolhe aleatoriamente uma palavra de uma lista de palavras.

    Args:
        lista_palavras (list): Uma lista de palavras.

    Returns:
        str: A palavra escolhida aleatoriamente.
    """
    return random.choice(lista_palavras)

def exibir_palavra_escondida(palavra, letras_adivinhadas):
    """
    Exibe uma palavra com letras adivinhadas e espaços para letras não adivinhadas.

    Args:
        palavra (str): A palavra a ser exibida.
        letras_adivinhadas (set): Um conjunto de letras adivinhadas.

    Returns:
        str: A palavra com letras adivinhadas reveladas e espaços para letras não adivinhadas.
    """
    palavra_escondida = ""
    for letra in palavra:
        if letra in letras_adivinhadas:
            palavra_escondida += letra
        else:
            palavra_escondida += "_"
    return palavra_escondida

def jogar_jogo(palavra):
    """
    Função principal que permite aos jogadores adivinharem uma palavra.

    Args:
        palavra (str): A palavra que os jogadores devem adivinhar.

    Returns:
        None
    """
    letras_adivinhadas = set()
    tentativas = 6

    print("Bem-vindo ao jogo de adivinhação de palavras!")
    
    while tentativas > 0:
        palavra_escondida = exibir_palavra_escondida(palavra, letras_adivinhadas)
        print(f"Palavra: {palavra_escondida}")
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras tentadas: {', '.join(letras_adivinhadas)}")

        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, insira uma única letra válida.")
            continue

        if letra in letras_adivinhadas:
            print("Você já tentou essa letra antes.")
            continue

        letras_adivinhadas.add(letra)

        if letra not in palavra:
            tentativas -= 1

        if set(palavra) == letras_adivinhadas:
            print("Parabéns! Você adivinhou a palavra!")
            break

    if tentativas == 0:
        print(f"Game Over! A palavra era: {palavra}")

if __name__ == "__main__":
    lista_palavras = carregar_palavras("lista_palavras.txt")
    palavra = escolher_palavra(lista_palavras)
    jogar_jogo(palavra)
