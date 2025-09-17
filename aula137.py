# Exercicio com classes
# 1 - Crie uma classe Carro (nome)
# 2 - Crie uma classe Motor (nome)
# 3 - Crie uma classe Fabricante (nome)
# 4 - Faça a ligação entre CArro tem Motor
# Obs: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e Fabricante
# Obs: Um Fabricante pode fabricar vários Carros
# Exiba o nome do carro, motor, e fabricante na tela
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor:
    def __init__(self, nome):
        self.nome = nome




class Fabricante:
    def __init__(self, nome):
        self.nome = nome


fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)


fiat_uno = Carro('Uno')
fiat = Fabricante('Fiat')
fiat_uno.fabricante = fiat
fiat_uno.motor = motor_1_0
print(fiat_uno.nome, fiat_uno.fabricante.nome, fiat_uno.motor.nome)


ka = Carro('Ka unlimited')
ford = Fabricante('Ford')
motor_1_6 = Motor('1.6')
ka.fabricante = ford
ka.motor = motor_1_6
print(ka.nome, ka.fabricante.nome, ka.motor.nome)
