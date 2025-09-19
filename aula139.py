# super() é a super classe na sub classe
# Classe pincipal (Pessoa)
#  -> super class, base class, parent class
# Classes filhas (Cliente)
#  -> sub class, child class, derived class
#class MinhaString(str):
#    def upper(self):
#        print('CHAMOU UPPER')
#        retorno = super().upper()
#        print('Depois do return')
#        return retorno

#string = MinhaString('Luiz')
#print(string.upper())


class A:
    atributo_a = 'valor a'
    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor b'
    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'valor c'
    def metodo(self):
        super().metodo()
        print('C')

c = C()
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()