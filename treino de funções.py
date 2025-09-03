# EXERCICIO FUNÇÕES
#def area_triangle(base, height):
#    return (base * height) / 2

#area = area_triangle(5, 10)
#print(f'A área do triângulo é: {area}')


#def somar_lista(numbers):
#    total = 0
#    for number in numbers:
#        total += number
#    return total

#soma = somar_lista([1, 2, 3, 4, 5])
#print(f'A soma da lista é: {soma}')


def calcular_valor_total(dict):
    total = 0
    for item in dict.values():
        total += item
    return total

dicionario = calcular_valor_total({'item1': 10, 'item2': 20, 'item3': 30})
print(f'O valor total é: {dicionario}')
