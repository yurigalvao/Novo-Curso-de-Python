# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.
class Carro:
    def __init__(self, nome='Sei lá'):
        self.nome = nome 


    def acelerar(self):
        print(f'{self.nome} está acelerando')

fusca = Carro('Fusca')
#Carro.acelerar(fusca)
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome='Celta')
#Carro.acelerar(celta)
print(celta.nome)
celta.acelerar()
