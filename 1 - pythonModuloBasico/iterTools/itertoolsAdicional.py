"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem Importa
Ambos não repetem os valores únicos
Produto - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product

pessoas = ['Daniel', 'Jessica', 'Maria', 'Marcos', 'Bruna', 'Fabricio', 'Rose']

# Combinando elementos com combinations
# (Variavel, quantidade de elementos)
# Não repete como no permutations.
for grupo in combinations(pessoas, 2):
    print(grupo)

# Aqui ele traz todas as combinações, mesmo que repetida, por exemplo:
# ('Daniel', 'Rose')
# ('Rose', 'Daniel')
for grupo in permutations(pessoas, 2):
    print(grupo)


# Criam combinações e repetem valores
for grupo in product(pessoas, repeat=2):
    print(grupo)