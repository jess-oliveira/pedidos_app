pedidos = [
    ['X-burguer', 'Refrigerante', 'Pudim'],
    ['X-salada', 'Coca-cola', 'Torta'],
    ['X-egge', 'Suco', 'Salada de fruta'],
    ['PEDIDO ERRADO']
]

# Função responsável por mostrar todos os pedidos cadastrados
def lista_de_pedidos():

    # Título da seção
    print('ORDENS DE PEDIDOS:\n')

    # enumerate percorre a lista e devolve:
    # índice + valor da posição
    #
    # n -> número do pedido
    # pedido -> lista com os itens do pedido
    #
    # start=1 faz a contagem começar em 1 ao invés de 0
    for n, pedido in enumerate(pedidos, start=1):

        # join junta os itens da lista usando ", " como separador
        #
        # Exemplo:
        # ['X-burguer', 'Refrigerante']
        #
        # vira:
        # X-burguer, Refrigerante
        print(f'{n} - {", ".join(pedido)}')


# Função para inserir um novo pedido
def inserir_pedido():

    # Recebe os itens digitados pelo usuário
    # strip remove espaços extras no começo e fim
    entrada = input(
        '\nDigite os itens do pedido (separados por vírgula): '
    ).strip()

    # split(',') separa os itens usando vírgula
    #
    # Exemplo:
    # "X-burguer, Refrigerante"
    #
    # vira:
    # ['X-burguer', ' Refrigerante']
    #
    # o strip dentro da lista remove espaços de cada item
    novo_pedido = [item.strip() for item in entrada.split(',')]

    # Adiciona o novo pedido na lista principal
    pedidos.append(novo_pedido)

    print('\nPedido inserido com sucesso!\n')

    # Mostra lista atualizada
    lista_de_pedidos()


# Função para excluir o último pedido cadastrado
def excluir_pedido():

    # Confirmação antes de remover
    resposta = input(
        '\nDeseja excluir último pedido cadastrado? (s/n) '
    )

    # Se usuário confirmar
    if resposta == 's':

        # pop() sem índice remove o último item da lista
        pedidos.pop()

        print('\nÚltimo pedido removido com sucesso!\n')

        # Mostra lista atualizada
        lista_de_pedidos()


# Função responsável pelo menu do sistema
def mostrar_menu():

    # Largura usada para alinhar os textos
    largura = 40

    print('''
           PEDIDOS APP'''.center(largura))

    print('''
        1 - Inserir novo pedido.
        2 - Excluir último pedido.
        3 - Ver lista de pedidos.
        4 - Encerrar app.'''.ljust(largura))


# Função principal do programa
def main():

    # while True mantém o app rodando
    # até o usuário escolher sair
    while True:

        # Mostra menu na tela
        mostrar_menu()

        # Recebe opção escolhida
        acao = input(
            '\nDigite o número do que deseja fazer: '
        )

        # Verifica se a opção existe
        if acao not in ['1', '2', '3', '4']:

            print('!!! Opção inválida !!! Escolha novamente:')

            # volta para o início do loop
            continue

        # match funciona parecido com vários if/elif
        # mas deixa o código mais organizado
        match acao:

            case '1':
                inserir_pedido()

            case '2':
                excluir_pedido()

            case '3':
                lista_de_pedidos()

            case '4':
                print('\nEncerrando app. Até mais!\n')

                # encerra o loop principal
                break


# Liga o sistema chamando a função principal
main()