# Métodos de classes + factories (fábricas)
# São métodos onde "self" será "cls", ou seja, 
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe

class Pessoa:
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')


print(Pessoa.ano)
p1 = Pessoa('João', 34)
Pessoa.metodo_de_classe()
