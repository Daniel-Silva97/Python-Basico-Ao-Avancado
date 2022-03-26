from zipfile import ZipFile
import os

caminho = r'C:\Workspaces\ws-python\3 - modulosPython\compactarDescompactarArquivos\arquivosparacompactar'

with ZipFile('arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminhoCompleto = os.path.join(caminho, arquivo)
        zip.write(caminhoCompleto, arquivo)


with ZipFile('arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)