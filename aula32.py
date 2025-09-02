"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
#numero = input('Digite um número: ')

#try:
#    numero = int(numero)
#    if numero % 2 == 0:
#        print(f'O numero {numero} é par.')
#    else:
#        print(f'O numero {numero} é ímpar.')
#except ValueError:
#    print('Não é um número inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
#horario = input('Que horas são?: ')
#bom_dia = range(0, 12)
#boa_tarde = range(12, 18)
#boa_noite = range(18, 24)
#try:
#    horario = int(horario)
#    if horario in bom_dia:
#        print('Bom dia!')
#    elif horario in boa_tarde:
#        print('Boa Tarde!')
#    elif horario in boa_noite:
#        print('Boa Noite!')
#except Exception:
#    print('Digite um Horário válido!')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
nome = input('Digite seu primeiro nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto.')
    elif tamanho_nome >= 5 and tamanho_nome <=6:
        print('Seu nome é normal.')
    else:
        print('Seu nome é muito grande.')
else:
    print('Digite mais de 1 letra.')

