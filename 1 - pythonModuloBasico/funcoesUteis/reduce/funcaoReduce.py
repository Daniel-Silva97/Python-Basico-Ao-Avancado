"""
Função reduce

Não vem por padrão no python, precisa importar
"""
from functools import reduce

pessoas = [
    {'nome': 'Luiz', 'idade': 32},
    {'nome': 'Daniel', 'idade': 25},
    {'nome': 'Jessica', 'idade': 52},
    {'nome': 'Lucas', 'idade': 10},
    {'nome': 'Gabriel', 'idade': 15},
    {'nome': 'Otávio', 'idade': 40},
    {'nome': 'Sandra', 'idade': 15},
    {'nome': 'Claudimir', 'idade': 20},
    {'nome': 'Alex', 'idade': 21},
    {'nome': 'Murilo', 'idade': 29},
    {'nome': 'Beatriz', 'idade': 3},
]

# Usando reduce para somar as idades
somaIdade = reduce(lambda acumulador, idades: acumulador + idades['idade'], pessoas, 0)

print(somaIdade)

produtos = [
    {'nome': 'Produto 1', 'preço': 13},
    {'nome': 'Produto 2', 'preço': 5.50},
    {'nome': 'Produto 3', 'preço': 11.20},
    {'nome': 'Produto 4', 'preço': 3.90},
    {'nome': 'Produto 5', 'preço': 81.99},
    {'nome': 'Produto 6', 'preço': 99.99},
    {'nome': 'Produto 7', 'preço': 5.99},
    {'nome': 'Produto 8', 'preço': 1.99},
    {'nome': 'Produto 9', 'preço': 9.99},
    {'nome': 'Produto 10', 'preço': 10},
    {'nome': 'Produto 11', 'preço': 1.99},
]

# Usando o Reduce para somar os preços do dicionário
somaPrecos = reduce(lambda acumulador, item: acumulador+item['preço'], produtos, 0)

print(f'{round(somaPrecos, 2)}')

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#  Usando a função reduce para somar todos os valores dentro da lista
somaLista = reduce(lambda acumulador, itemDaLista: acumulador + itemDaLista, lista, 0)

print(somaLista)


