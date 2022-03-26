"""
Comma Separated Values - CSV (Valores Separadors por vírgula)

É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de dados
clientes de e-mail, etc.
"""
import csv

with open('clientes.csv', 'r') as arquivo:
    # dados = csv.reader(arquivo)  # Gera um iterador
    dadosEmDicionario = [x for x in csv.DictReader(arquivo)]  # Gera um dicionário do CSV e convertemos pra lista
    # com List Comprehension, para poder acessar fora do gerador With Open()
    # next(dados)  # Pulando o cabeçalho da planilha no iterador
    # for dado in dados:
    #     print(dado)

    # for dict in dadosEmDicionario:
    #     print(dict['Nome'], dict['Sobrenome'], dict['E-mail'], dict['Telefone'])

with open('clientes2.csv', 'w') as arquivo: # Criando um arquivo com base no primeiro CSV
    """
    Denominando na variável escreve que
    delimitador deve ser vírgula,
    Cada valor que for incluso deve estar entre aspas duplas
    e que será feito isso em todos.
    """
    escreve = csv.writer(
        arquivo,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    #  Pegando o cabeçalho e incluindo no arquivo
    chaves = dadosEmDicionario[0].keys()
    chaves = list(chaves)
    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3]
        ]
    )

    for dado in dadosEmDicionario:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )
