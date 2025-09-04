# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
caminho_arquivo = 'C:\\Users\\yurig\\OneDrive\\Área de Trabalho\\novo curso de python\\venv\\Scripts\\Activate.ps1' # caminho completo de arquivo
caminho_arquivo += 'aula116.txt'

#arquivo = open(caminho_arquivo, 'w') abrir e criar o arquivo, passo o caminho do arquivo e abro e fecho o arquivo
#arquivo.close()

with open('aula116.txt', 'w+') as arquivo:  #abre e fecha o arquivo
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    print(arquivo.read())

with open('aula116.txt', 'r') as arquivo:
    print(arquivo.read())