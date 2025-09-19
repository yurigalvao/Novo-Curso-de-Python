# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - é dono de (tem e controla o ciclo de vida)
# Herança - é um (é um tipo de)
#
# Herança ou composição
#
# Classe principal (Pessoa)
#  -> super class, base class, parent class
# Classes filhas (Cliente)
#  -> sub class, child class, derived class
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print('Classe PESSOA')
        print(self.nome, self.sobrenome, self.__class__.__name__)



class Cliente(Pessoa):
    def falar_nome_classe(self):
        print('Eita, nem sai da classe Cliente')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Aluno(Pessoa):
    cpf = 'cpf aluno'
    ...


c1 = Cliente('Luiz', 'Otávio')
c1.falar_nome_classe()
a1 = Aluno('Maria', 'Helena')
a1.falar_nome_classe()
print(a1.cpf)
