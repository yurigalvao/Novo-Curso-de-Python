#def fazer_pizza(*args, **kwargs):
#    print("Ingredientes da pizza (args):", args)
#    print("Instruções especiais (kwargs):", kwargs)

#fazer_pizza('mussarela', 'calabresa', 'cebola', borda_recheada=True, sem_cebola=True)

# exercicio para treinar *args e **kwargs
def minha_funcao(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)

minha_funcao(1, 2, 3, nome='Yuri', idade=24)    