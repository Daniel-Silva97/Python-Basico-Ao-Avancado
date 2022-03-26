import os
from utils import formataTamanho

while True:
    caminhoProcura = input('Digite um caminho: ')
    termo_procura = input('Qual o nome do arquivo? ')
    contador = 0
    # Para Pasta raiz, as pastas dentro dela e arquivos, faça:
    for raiz, diretorios, arquivos in os.walk(caminhoProcura):
        # Para cada arquivo na pasta raiz
        for arquivo in arquivos:
            # Só executa somente se o termo de busca estiver no nome do arquivo
            if termo_procura in arquivo:
                try:
                    contador += 1
                    # Pegando o caminho do arquivo + seunome.extensao
                    caminhoCompleto = os.path.join(raiz, arquivo)
                    # Separando o nome do arquivo da extensão
                    nomeArquivo, extensaoArquivo = os.path.splitext(arquivo)
                    # Pegando o tamanho do arquivo em bytes
                    tamanhoArquivo = os.path.getsize(caminhoCompleto)

                    print()
                    print('Encontrei o arquivo:', arquivo)
                    print('Caminho:', caminhoCompleto)
                    print('Nome:', nomeArquivo)
                    print('Extensão', extensaoArquivo)
                    print('Tamanho:', tamanhoArquivo)
                    print('Tamanho Formatado:', formataTamanho(tamanhoArquivo))
                except PermissionError as e:
                    print('Sem Permissão')
                except FileNotFoundError as e:
                    print('Arquivo não encontrado')
                except Exception as e:
                    print('Erro desconhecido', e)

    print()
    print(f'{contador} arquivo(s) encontrados')
