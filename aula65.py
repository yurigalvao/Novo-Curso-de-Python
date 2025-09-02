"""
Introdução às funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (Nada).
"""

#def imprimir(a, b, c):  #Parâmetros
#    print(a, b, c)


#imprimir(1, 2, 3)  # Argumentos 
#imprimir(4, 5, 6)

def saudacao(nome = 'Sem nome'):  # Como se fosse uma variável
    print(f'Olá, {nome}!')

saudacao('Yuri')
saudacao()
