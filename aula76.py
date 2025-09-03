# Usada pra exercicio com dicionarios 
interface = ('Adicionar Contato', 'Buscar Contato', 'Excluir Contato','Ver lista de contatos', 'Sair') 
contatos = {}

while True:
    print('Selecione uma opção: ')
    for i, opcao in enumerate(interface):
        print(f'{i + 1}. {opcao}')

    opcao_escolhida = input('Escolha uma opção: ')

    if opcao_escolhida == '1':
        nome = input('Digite o nome do contato: ')
        telefone = int(input('Digite o telefone do contato: '))
        contatos[nome] = telefone
        print(f'Contato {nome} adicionado com sucesso!')

    elif opcao_escolhida == '2':
        nome = input('Digite o nome do contato que deseja buscar: ')
        if nome in contatos:
            print(f'O telefone de {nome} é {contatos[nome]}')
        else:
            print('Usuário não encontrado')

    elif opcao_escolhida == '3':
        nome = input('DIgite o nome do contato que deseja excluir: ')
        if nome in contatos:
            del contatos[nome]
            print(f'Contato {nome} excluído com sucesso!')
        else:
            print('Usuário não encontrado')

    elif opcao_escolhida == '4':
        for nome, telefone in contatos.items():
            print(f'Nome: {nome}, Telefone: {telefone}')
        if not contatos:
            print('Nenhum contato encontrado.')
            
    elif opcao_escolhida == '5':
        print('Saindo do programa...')
        break




