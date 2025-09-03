# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
#s1 = set()  # Vazio
#s1 = {'Luiz', 1, 2, 3} # Com dados
#print(s1)

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)
#l1 = [1, 2, 3, 3, 3, 3, 3, 3, 1]
#s1 = set(l1)
#l2 = list(s1)
#s1 = {1, 2, 3}
#print(4 not in s1)
#for numero in s1:
#    print(numero)

# Métodos úteis:
# add, update, clear, discard
#s1 = set()
#s1.add(1)
#s1.add(2)
#s1.add(3)
#s1.update([4, 5]) # pode ser passado varios valores
#s1.discard(5)
#s1.clear()  # limpa o set 
#print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos
s1 = {1, 2, 3}  
s2 = {2, 3, 4}

# União
print(s1 | s2)
print(s1.union(s2))

# Intersecção
print(s1 & s2)
print(s1.intersection(s2))

# Diferença
print(s1 - s2)
print(s1.difference(s2))

# Diferença simétrica
print(s1 ^ s2)
print(s1.symmetric_difference(s2))
