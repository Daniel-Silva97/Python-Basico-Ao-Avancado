"""
List comprehension em python
"""

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Usando o list comprehension
# No caso abaixo criei um laço for para atirbuir a variavel os valores da
# lista1 tornando ela identica.
exemplo1 = [variavel for variavel in lista1]
print(exemplo1)

# Posso fazer calculos por exemplo
# Multiplicando os elementos da lista1 por 2 e atribuindo a variavel
exemplo2 = [variavel * 2 for variavel in lista1]
print(exemplo2)

# Criar uma tupla para cada elemento que armazene o valor do elemento e também um range(3) que pode ser 0, 1 ou 2
exemplo3 = [(v1, v2) for v1 in lista1 for v2 in range(3)]
print(exemplo3)

lista2 = ['Daniel', 'Maria', 'Ana']

# Substituindo a por @ usando list comprehension
exemplo4 = [v.replace('a', '@') for v in lista2]
print(exemplo4)


tupla1 = (
    ('chave', 'valor'),
    ('chave2', 'valor2')
)

# Invertendo as posições, valor no lugar de chave e vice-versa
exemplo5 = ((y, x) for x, y in tupla1)
exemplo5 = dict(exemplo5)
print(exemplo5)

# Pegando todos os números divisiveis por 2 em uma lista de 0 a 100
# Criando a lista
lista3 = range(100)
# List comprehension
exemplo6 = [v for v in lista3 if v % 2 == 0]
print(exemplo6)

# Usando if com mais de uma condição e else em list comprehension
exemplo7 = [v if v % 3 == 0 and v % 8 == 0 else f'{v} Não é divisível por 3 e por 8' for v in lista3]
print(exemplo7)