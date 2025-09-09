# Exercicio para treino de conceitos aprendidos no dia 08/09
class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade_estoque

    def alterar_preco(self, novo_preco):
        if novo_preco:
            self.preco = novo_preco
            print(f'Preço do produto {self.nome} alterado com sucesso!')
        
    def vender(self, quantidade_vendida):
        print(f'Está sendo vendido {quantidade_vendida} do {self.nome}')
        if quantidade_vendida<=self.quantidade:
            self.quantidade -= quantidade_vendida
            print('Estoque atualizado')
        else:
            print('Quantidade de venda maior do que o estoque')

    def mostrar_estoque(self):
        return f'O estoque atual de {self.nome} é: {self.quantidade}'
    
notebook = Produto('Notebook Gamer', 5000, 10)
print(notebook.mostrar_estoque())
notebook.vender(4)
print(notebook.mostrar_estoque())
notebook.vender(7)
print(notebook.mostrar_estoque())
notebook.alterar_preco(4500)
print(notebook.preco)

        