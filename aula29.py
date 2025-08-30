"""
Introdução ao try/except
try -> tentar executar o código
except -> tratar o erro
"""

numero = input('Digite um número para eu dobrar: ')
try:
    numero = int(numero)
    print(f'O dobro de {numero} é {numero * 2}')
except ValueError:
    print('Por favor, digite um número válido.')
