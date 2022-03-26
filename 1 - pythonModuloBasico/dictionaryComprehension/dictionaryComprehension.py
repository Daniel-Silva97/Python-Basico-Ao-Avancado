"""
Dictionary comprehension
"""

lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]

# Usando o dictionary comprehension para converter a lista em dicionário
dicionario = {x: y for x, y in lista}
print(dicionario)
