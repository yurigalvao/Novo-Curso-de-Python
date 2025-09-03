#from sys import path

#from aula99_package.modulo import soma_do_modulo
#from aula99_package.modulo import *
#print(*path, sep='\n')

#print(soma_do_modulo(5, 10))
#print(variavel)
#from aula99_package.modulo import soma_do_modulo, fala_oi

#print(__name__)
#fala_oi()

# todas as importações precisam ser relacionadas no main
from aula99_package import soma_do_modulo, fala_oi

print(soma_do_modulo(2, 3))
fala_oi()
