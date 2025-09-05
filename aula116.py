# Criando arquivos com Python + Context Manager with
# Usamos a fun��o open para abrir
# um arquivo em Python (ele pode ou n�o existir)
# Modos:
# r (leitura), w (escrita), x (para cria��o)
# a (escreve ao final), b (bin�rio)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# M�todos �teis
# write, read (escrever e ler)
# writelines (escrever v�rias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o m�dulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o m�dulo json, mas:
# json.dump = Gera um arquivo json
# json.load
#caminho_arquivo = 'C:\\Users\\yurig\\OneDrive\\�rea de Trabalho\\novo curso de python\\venv\\Scripts\\Activate.ps1' # caminho completo de arquivo
#caminho_arquivo += 'aula116.txt'

#arquivo = open(caminho_arquivo, 'w') abrir e criar o arquivo, passo o caminho do arquivo e abro e fecho o arquivo
#arquivo.close()

#with open('aula116.txt', 'w+') as arquivo:  #abre e fecha o arquivo
#    arquivo.write('Linha 1\n')
#    arquivo.write('Linha 2\n')
#    print(arquivo.read())

#with open('aula116.txt', 'r') as arquivo:
#    print(arquivo.read())
caminho_arquivo = 'aula116.txt'

with open(caminho_arquivo, 'w+', encoding='utf-8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Print 123')
    