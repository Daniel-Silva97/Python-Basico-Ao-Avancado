
"""
Função Filter
"""

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

# Filtrando todos os produtos com preço maior que 50
novosProdutos = filter(lambda produto: produto['preço'] > 50, produtos)

for produto in novosProdutos:
    print(produto)


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


# Posso usar função no Filter
def filtrar(pessoa):
    if pessoa['idade'] >= 18:
        return True
    else:
        return False


novasPessoas = filter(filtrar, pessoas)

for pessoat in novasPessoas:
    print(pessoat)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Usando o Filter para filtrar numeros maiores que 6
novaLista = filter(lambda x: x > 5, lista)

print(list(novaLista))


