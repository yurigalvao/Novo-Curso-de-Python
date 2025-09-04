#def fazer_pizza(*args, **kwargs):
#    print("Ingredientes da pizza (args):", args)
#    print("Instruções especiais (kwargs):", kwargs)

#fazer_pizza('mussarela', 'calabresa', 'cebola', borda_recheada=True, sem_cebola=True)

# exercicio para treinar *args e **kwargs
#def minha_funcao(*args, **kwargs):
#    print('args:', args)
#    print('kwargs:', kwargs)

#minha_funcao(1, 2, 3, nome='Yuri', idade=24)    

# Lambda
# Função anônima, ou seja, sem nome

estudantes = [
    {'nome': 'João', 'nota': 7.5},
    {'nome': 'Maria', 'nota': 9.0},
    {'nome': 'Pedro', 'nota': 6.0}
]
"""
A função sorted() é chamada pra ordenar a lista "estudantes". Ela retorna uma lista nova ordenada, sem alterar a original. key=lambda x:x['nota'] é a parte principal, lambda x - cria uma nova função sem nome que aceita um unico argumento x, x['nota'] - para cada dicionário na lista, a função lambda retorna o valor da chave 'nota', é isso que a função sorted() usa para decidir a ordem dos itens, ou seja, a lambda age como a chave de ordenação. reverse=True - ordena em ordem decrescente, do maior para o menor.
"""
estudantes = sorted(estudantes, key=lambda x: x['nota'], reverse=True) 
print(estudantes)