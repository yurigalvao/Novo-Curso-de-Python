"""
Treino para relembrar a estrutura for
"""
#numero = int(input('Digite um número: '))

#for n in range (1, numero+1):
#    print(n)

# Exercicio para percorrer uma lista 
"""
estoque = ['maçã', 'banana', 'laranja', 'uva', 'morango', 'abacaxi', 'kiwi']

for fruta in estoque:
    print(fruta)
    if fruta in ['laranja', 'uva']:
        print(f'Produto {fruta} em falta! Favor repor!')
    else:
        print(f'Produto {fruta} em estoque!')
"""
# Exercicio while
#contador = 1
#while contador <= 5:
#    print(f'O valor atual do contador é {contador}')
#    contador += 1

#while True:
#    cidade = input('Digite o nome de uma cidade: ')
#    if cidade.lower() == 'paris':
#        print('Parabens você acertou!')
#    else:
#        print('Tente novamente!')

# exercicio com listas 
opcao = ('Adicionar Item', 'Visualizar item especifico', 'Visualizar lista completa', 'Sair')
lista_de_compras = []

while True:
    for i,item in enumerate(opcao):
        print(f'{i + 1} - {item}')
    opcao_escolhida = input('Escolha uma opção: ')
    if opcao_escolhida == '1':
        item = input('Digite o nome do item: ')
        lista_de_compras.append(item)
        print('Item adicionado com sucesso!')
    elif opcao_escolhida == '2':
        item = int(input('Digite o número do item que deseja visualizar: '))
        if 0 <= item - 1 < len(lista_de_compras):
            print(f'O item {item} é {lista_de_compras[item]}')
        else:
            print('Item não encontrado.')
    elif opcao_escolhida == '3':
        print('Lista de Compras: ')
        for i, item in enumerate(lista_de_compras):
            print(f'{i} - {item}')
    elif opcao_escolhida == '4':
        print('Saindo...')
        break
    else:
        print('Digite uma opção válida!')

