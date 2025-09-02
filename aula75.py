# Exercicios
# Crie funções que duplicam, triplicam e quadruplicam um número
# o número recebido como parâmetro

def creation_multiplication(multiplicator): # Criei uma função que cria outras funções
    def multiplier(number): # Função criada que multiplica um numero pelo multiplicador
        return number * multiplicator # Esta função retorna a multiplicação dos dois argumentos
    return multiplier # Retorna a função multiplicadora

duplication = creation_multiplication(2) # Criei uma variável que armazena  a função de duplicação
triplication = creation_multiplication(3) # Criei uma variável que armazena a função de triplicação
quadruplication = creation_multiplication(4) # Criei uma variável que armazena a função de quadruplicação


# Chamei as funções e imprimi seus resultados passando o 2 como argumento
print(duplication(2)) 
print(triplication(2))
print(quadruplication(2))   
