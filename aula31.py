"""
Flag (Bandeira) - Marcar um local
None = Não Valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
"""

#v1 = 'a'
#v2 = 'b'

#print(id(v1)) # identidade do objeto na memória
#print(id(v2)) # identidade do objeto na memória

condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não Passou no if')
else:
    print('Passou no if')
