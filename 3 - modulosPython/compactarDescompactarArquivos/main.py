from zipfile import ZipFile
import os

caminho = r'DIRETORIO_A_COMPACTAR'

# Gerando o arquivo ZIP com permissao para escrita
with ZipFile('arquivo.zip', 'w') as compactando:
    #  Navegando pela pasta com listdir para não entrar em subpastas
    for arquivo in os.listdir(caminho):
        caminhoCompleto = os.path.join(caminho, arquivo)  # Pegando Caminho do arquivo + nome do arquivo aqui
        compactando.write(caminhoCompleto, arquivo)  # colocando no arquivo ZIP sem colocar no nome do arquivo o caminho
        # por isso a variável arquivo ali (caminhocompleto = Onde pegar o arquivo, arquivo = nome do arquivo dentro
        # do zip)

# Lendo os arquivos dentro do ZIP
with ZipFile('arquivo.zip', 'r') as lendo:
    for arquivo in lendo.namelist():
        print(arquivo)

# Descompactando os itens
with ZipFile('arquivo.zip', 'r') as descompactando:
    descompactando.extractall('descompactado')
