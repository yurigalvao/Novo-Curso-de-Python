"""
Closure e funções que retornam outras funções
"""

def saudation(saudation):
    def to_greet(name):
        return f'{saudation}, {name}!'
    return to_greet


falar_bom_dia = saudation('Bom dia')
falar_boa_noite = saudation('Boa noite')

for nome in ['Maria', 'Helena', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
