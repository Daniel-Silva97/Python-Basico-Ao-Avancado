"""
Como criar, Ler, Escrever e Apagar os arquivos

https://docs.python.org/3/library/functions.html#open
"""

# Criando o arquivo abc.txt com permissão de escrita(w) e escrita e leitura(+)
# file = open('abc.txt', 'w+')

# Escrevendo linhas dentro do arquivo
# file.write('Linha 1\n')
# file.write('Linha 2\n')
# file.write('Linha 3\n')

# Voltando para o início do arquivo
# file.seek(0, 0)

# Após voltar para o início do arquivo, posso ler as linhas que criei
# print('Lendo linhas: ')
# print(file.read())
# print('#########################')

# file.seek(0, 0)
# Lendo linha a linha
# print(file.readline(), end='')
# print(file.readline(), end='')
# print(file.readline(), end='')

# print('#########################')
# file.seek(0, 0)
# Cria uma lista onde percorre todas as linhas
# print(file.readlines())
# Posso percorrer a lista usando um laço
# print('#########################')
# file.seek(0, 0)
# for linha in file.readlines():
# print(linha, end='')

# Após editar o tudo no arquivo, obrigatório fechar o arquivo
# file.close()


# Outra forma de poder criar arquivo é usando o try ... finally
# try:
#     # Criando o arquivo
#     file = open('abc.txt', 'w+')
#     # Modificando o arquivo
#     file.write('Linha')
#     file.seek(0)
#     # Lendo o arquivo
#     print(file.read())
# finally:
#     # Fechando o arquivo
#     file.close()

# Forma Python de manipular os arquivos
# Criando o arquivo
with open('abc.txt', 'w+') as file:
    # Manipulando o arquivo
    file.write('Linha 1 \n')
    file.write('Linha 2 \n')
    file.write('Linha 3 \n')

    # Exibindo o arquivo
    file.seek(0)
    print(file.read())

# Desta forma não preciso usar o file.close(), assim que executar tudo ele fechará o arquivo para mim


# Para remover o arquivo
import os

os.remove('abc.txt')


# Criando arquivo JSON
import json

# Gerando o dicionário que vou converter em JSON
dicionario = {
    'Pessoa 1': {
        'nome': 'Luiz',
        'idade': 25
    },
    'Pessoa 2': {
        'nome': 'Rose',
        'idade': 30
    }
}

# Criando o JSON
dicionarioParaJson = json.dumps(dicionario, indent=True)

# Transportando para um arquivo
with open('testeJson.json', 'w+') as file:
    file.write(dicionarioParaJson)


