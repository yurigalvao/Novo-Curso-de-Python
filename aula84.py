"""
List comprehension em Python
List comprehension é uma forma rápida para criar listas 
a partir de iteráveis
"""
#lista = []
#for numero in range(10):
#    lista.append(numero)
#print(lista)

#lista = [numero * 2 for numero in range(10)]
#print(lista)

# Exercicio rapido com list comprehension
temperatura_celsius = [0, 15, 25, 30, 40]
temperatura_farenheit = [(t * 9/5) + 32 for t in temperatura_celsius]

#print(temperatura_celsius)
#print(temperatura_farenheit)

# Mais um exercicio
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = [numero for numero in numeros if numero % 2 == 0] # vou pegar o numero antes percorrer no for e adicionar se ele for par
print(numeros_pares)
