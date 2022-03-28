from zipfile import ZipFile
import os

caminho = r'C:\Workspaces\ws-python\3 - modulosPython\compactarDescompactarArquivos\arquivosparacompactar'

# Gerando o arquivo ZIP com permissao para escrita
with ZipFile('arquivo.zip', 'w') as zip:
    #  Navegando pela pasta com listdir para não entrar em subpastas
    for arquivo in os.listdir(caminho):
        caminhoCompleto = os.path.join(caminho, arquivo)  # Pegando Caminho do arquivo + nome do arquivo aqui
        zip.write(caminhoCompleto, arquivo)  # colocando no arquivo ZIP sem colocar no nome do arquivo o caminho
        # por isso a variável arquivo ali (caminhocompleto = Onde pegar o arquivo, arquivo = nome do arquivo dentro
        # do zip)

# Lendo os arquivos dentro do ZIP
with ZipFile('arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)
