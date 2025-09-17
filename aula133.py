# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÂO TEM modificadores de acesso
# MAs podemos seguir as seguintes convenções:
#  (sem underline) = public
#     pode ser usado em qualquer lugar
#  (_ um underline) = protected
#     não deve ser usado fora da classe
#     ou suas subclasses.
#  (__ dois underlines) = private
#     "name mangling" (desfiguração de nomes) em Python
#     só deve ser usado na classe que foi declarado.
class Foo:
    def __init__(self):
        self.public = 'isso é publico'
        self._protected = 'isso é protegido' # isso é uma convenção
        self.__exemplo = 'isso é privado'
        
    def metodo_publico(self):
        #self._metodo_protected()
        #print(self._protected)
        print(self.__exemplo)
        self.__metodo_private()
        return 'metodo_publico'
    
    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'
    
    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'


f = Foo()
#print(f.public)
print(f.metodo_publico())
