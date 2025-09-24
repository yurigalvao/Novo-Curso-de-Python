# __new__ e __init__ em classes Python
# __new__ é o método responsávwl por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ DEVE retornar o novo objeto
# __init__ é o método responsável por inicializar
# a instância. Por isso, init receb self
# __init__ NÂO DEVE retornar nada (NOne)
# object é a super classe de uma classe
class A:
    def __new__(cls):
        print('Antes de criar a inst')
        return super().__new__(cls)
    
    def __init__(self):
        print('SOu o init')

    def __repr__(self):
        return 'A()'
    

a = A()
print(a)