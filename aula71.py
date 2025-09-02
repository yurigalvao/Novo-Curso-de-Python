"""
args - Argumentos não nomeados
* - *args (empacotamento)
"""
# Lembre-se de desempacotamento
#x, y, *resto = 1, 2, 3, 4
#print(x, y, resto)


def soma(*args): # argumentos nao nomeado
    total = 0
    for numero in args:
        total += numero
    return total



#soma_1_2_3 = soma(1, 2, 3)
#print(soma_1_2_3)

#soma_4_5_6 = soma(4, 5, 6)
#print(soma_4_5_6)

numeros = 1, 2, 3, 4, 56, 7, 78, 4
outra_soma = soma(*numeros) # Desempacotando a tupla para passar na função soma
print(outra_soma)

print(*numeros)
print(sum(numeros)) # Função interna do Python que faz a soma de iteráveis