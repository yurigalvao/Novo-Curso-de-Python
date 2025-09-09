# Métodos em instâncias de classes Python
# Hard coded - É algo que foi escrito diretamente no código
# O primeiro parametro sempre tem que ser self
class Carro:
    def __init__(self, nome='Sei lá'):
        self.nome = nome 


    def acelerar(self):
        print(f'{self.nome} está acelerando')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()