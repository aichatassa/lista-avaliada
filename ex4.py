# O código implementa um "Banco de Dados" de dicionários
# Usuários podem cadastrar informações em campos obrigatórios e opcionais. 
# Há um menu com três opções: cadastrar usuário, imprimir usuários e encerrar.

# Detalhamento das Estruturas Usadas:

# banco_usuarios (Lista de Dicionários):
# É uma lista que armazena os dicionários que representam os usuários cadastrados.
# Cada dicionário contém os campos e valores do usuário.


# cadastrar_usuario(campos_obrigatorios):
# A função recebe uma lista campos_obrigatorios que contém os campos que são obrigatórios para o cadastro.
# Ela cria um dicionário usuario para representar o novo usuário.
# Em um loop, solicita ao usuário os valores para os campos obrigatórios e os campos adicionais (opcional) até que o usuário digite "sair".
# O dicionário do usuário é adicionado à lista banco_usuarios.


# **imprimir_usuarios(*args, kwargs):
# A função permite imprimir usuários com várias opções:
# Imprimir todos os usuários.
# Filtrar por nomes de usuários específicos.
# Filtrar por campos e valores específicos.
# Filtrar por nomes de usuários e campos e valores específicos.
# A função aceita argumentos variáveis (*args e **kwargs) para lidar com diferentes opções de filtragem.
# Ela verifica a escolha do usuário e itera sobre os dicionários de usuários em banco_usuarios, aplicando os filtros e imprimindo os resultados correspondentes.


# main():
# A função principal inicia o programa.
# Ela solicita ao usuário que defina os campos obrigatórios.
# Em seguida, entra em um loop de menu que permite ao usuário escolher entre as opções de cadastro, impressão ou encerramento do programa.

banco_usuarios = []

def cadastrar_usuario(campos_obrigatorios):
    """
    Cadastra um usuário no banco de dados.

    Esta função permite ao usuário cadastrar um novo usuário no banco de dados, fornecendo valores para os campos
    obrigatórios especificados.

    Args:
        campos_obrigatorios (list): Uma lista de nomes dos campos obrigatórios para o cadastro.

    Returns:
        None
    """
    usuario = {}

    for campo_obrigatorio in campos_obrigatorios:
        valor = input(f"Digite o valor para o campo '{campo_obrigatorio}': ")
        usuario[campo_obrigatorio] = valor

    while True:
        novo_campo = input("Digite um campo adicional ou 'sair' para encerrar: ").strip()

        if novo_campo.lower() == 'sair':
            break

        valor = input(f"Digite o valor para o campo '{novo_campo}': ")
        usuario[novo_campo] = valor

    banco_usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def imprimir_usuarios(*args, **kwargs):
    """
    Imprime os usuários do banco de dados com base nas opções escolhidas.

    Esta função oferece várias opções de impressão dos usuários do banco de dados, permitindo filtrar por nomes, campos
    e combinações desses critérios.

    Args:
        *args: Argumentos posicionais que podem ser nomes de usuários para filtragem.
        **kwargs: Argumentos nomeados que são pares de campo e valor para filtragem.

    Returns:
        None
    """
    opcao = input("Escolha uma opção:\n1 - Imprimir todos\n2 - Filtrar por nomes\n3 - Filtrar por campos\n4 - Filtrar por nomes e campos\nOpção: ")

    if opcao == '1':
        for usuario in banco_usuarios:
            print(usuario)
    elif opcao == '2':
        nomes = args
        for usuario in banco_usuarios:
            if usuario.get('Nome') in nomes:
                print(usuario)
    elif opcao == '3':
        campos = kwargs.keys()
        for usuario in banco_usuarios:
            if all(usuario.get(campo) == valor for campo, valor in kwargs.items()):
                print(usuario)
    elif opcao == '4':
        nomes = args
        campos = kwargs.keys()
        for usuario in banco_usuarios:
            if (usuario.get('Nome') in nomes) and all(usuario.get(campo) == valor for campo, valor in kwargs.items()):
                print(usuario)
    else:
        print("Opção inválida.")

def main():
    """
    Função principal que gerencia o menu do banco de dados de usuários.

    Returns:
        None
    """
    print("Bem-vindo ao Banco de Dados de Usuários!")
    campos_obrigatorios = input("Digite os nomes dos campos obrigatórios separados por vírgula: ").split(',')
    campos_obrigatorios = [campo.strip() for campo in campos_obrigatorios]

    while True:
        print("\nMenu:")
        print("1 - Cadastrar usuário")
        print("2 - Imprimir usuários")
        print("0 - Encerrar")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastrar_usuario(campos_obrigatorios)
        elif escolha == '2':
            imprimir_usuarios()
        elif escolha == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
