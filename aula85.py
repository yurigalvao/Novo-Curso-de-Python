lista = []
for x in range(3): # para cada x eu tenho 3 y's 
    for y in range(3):
        lista.append((x, y))
print(lista)


lista = [(x, y) for x in range(3) for y in range(3)] # mesma coisa com list comprehension
print(lista)


lista = [[x for y in range(3)] for x in range(3)]
print(lista)
#https://youtu.be/1YbTDczvqco
# link do video de duvidas sobre list comprehension