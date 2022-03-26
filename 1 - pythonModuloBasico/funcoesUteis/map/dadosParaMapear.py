"""
Map em python
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Retorna um iterador map
novaLista = map(lambda x: x * 2, lista)

print(lista)
print(list(novaLista))


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


# Aumentando o preço do produto em 5%
def aumentaPreco(p):
    p['preço'] = round(p['preço'] * 1.05, 2)
    return p


novos_produtos = map(aumentaPreco, produtos)

for produto in novos_produtos:
    print(produtos)


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


# Aumentando a idade em 20%
def aumentaIdade(i):
    i['idade'] = round(i['idade'] * 1.20)
    return i


nomes = map(aumentaIdade, pessoas)

for pessoa in nomes:
    print(pessoa)