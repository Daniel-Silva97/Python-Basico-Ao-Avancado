import sys
import os

# Sys.argvs grava em uma lista sendo que o primeiro elemento é o nome do arquivo e após isso, as outras posições
# são argumentos passados pelo usuário via terminal por exemplo
argumentos = sys.argv
# Captando a quantidade de argumentos passados
qtd_argumentos = len(argumentos)

# Verificando se o único argumento é o nome do arquivo, para retornar a msg abaixo
if qtd_argumentos <= 1:
    print('Faltando Argumentos:')
    print('-a', 'Para listar todos os arquivos nesta pasta', sep='\t')
    print('-d', 'Para listar todos os diretórios nesta pasta', sep='\t')
    print('-ad', 'Para listar todos os diretórios nesta pasta', sep='\t')
    sys.exit()  # Fechando o comando para liberar o terminal após exibir a msg

# Tratando quando argumento -a
soArquivos = False
if '-a' in argumentos:
    soArquivos = True
# Tratando quando argumento -d
soDiretorios = False
if '-d' in argumentos:
    soDiretorios = True
# Tratando quando argumento -ad
if '-ad' in argumentos:
    soDiretorios = True
    soArquivos = True

# Navegando pela pasta onde o script tá para listar se necessário
for arquivo in os.listdir('.'):
    # Listando só arquivos
    if soArquivos:
        if os.path.isfile(arquivo):
            print(arquivo)
    # Listando só pastas
    if soDiretorios:
        if os.path.isdir(arquivo):
            print(arquivo)
