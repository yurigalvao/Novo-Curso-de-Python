"""
Lambda deve ser usado para funções mais simples
"""

def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y

def criaa_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

duplicador = executa(lambda m: lambda n: m * n, 2)
print(duplicador(2))

print(executa(lambda x, y: x + y, 2, 3), executa(soma, 2, 3), soma(2, 3))