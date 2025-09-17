# @property + @setter - getter e setter no modo Pythônico
# - como getter
# p/ evitar quebrar código cliente
# p/ habilitar setter
# p/ executar ações ao obter um atributo
# Atributos que começam com 1 ou 2 underlines
# não devem ser usados fora da classe
class Caneta:
    def __init__(self, cor):
        # private
        self._cor = cor # não deve ser usado
        self._cor_tampa = None

    @property
    def cor(self):
        #print('PROPERTY')
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        #print('ESTOU NO SETTER', valor)
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor



caneta = Caneta('Azul')
caneta.cor = 'Rosa'
caneta.cor_tampa = 'Azul'
# getter -> obter valor
print(caneta.cor)
print(caneta.cor_tampa)

