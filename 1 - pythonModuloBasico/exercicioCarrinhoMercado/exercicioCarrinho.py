"""
Exercicio Carrinho - Somatório
"""

carrinho = []

carrinho.append(('Produto 1', 20))
carrinho.append(('Produto 2', 30))
carrinho.append(('Produto 3', 50))

# Resolver usando list comprehension o somatório dos valores
# desempacotando o carrinho separando em x e y e pegando somente o y para aplicar o sum
total = sum([float(y) for x, y in carrinho])
print(carrinho)
print(total)
