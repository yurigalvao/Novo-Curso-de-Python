# @staticmethod (métodos estatísticos) são inuteis em python
# Métodos estatísticos são métodos que estão dentro da 
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua classe

class Classe:
    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('OI', args, kwargs)


    
c1 = Classe()
c1.funcao_que_esta_na_classe(1, 2, 3)
