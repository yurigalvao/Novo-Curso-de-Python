import importlib

import aula98_m

print(aula98_m.variavel)

for i in range(10):
    importlib.reload(aula98_m) # Recarrega o módulo se caso preciso quando muda alguma variavel ou outro dado no módulo importado
    print(i)

print('Fim')