"""
Split, join, Enumerate em Python
* Split - Dividir um string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list / iteráveis
"""

string = "O Brasil é o país do futebol, terra do Rei Pelé!"

lista1 = string.split(' ')  # Usando o [SPACE] para separar as palavras em elementos da lista
print(lista1)

lista2 = string.split(',')  # Usando a vírgula para separar as frases em elementos da lista
print(lista2)

#  Contando quantos vezes a palavra apareceu na lista
for valor in lista1:
    print(f'A palavra "{valor}" apareceu {lista1.count(valor)} vezes nessa lista!')


# Usando o JOIN
lista3 = ' '.join(lista1)  # Junta os elementos da lista separando por espaços
print(lista3)

#  Usando o Enumerate
for indice, valor in enumerate(lista1):  # Indice será coincidente com o resultado do enumerate que inicia do 0, e valor
    # será referente ao elemento da lista
    print(valor, indice, lista1[indice])

#  Enumerate gera uma tupla com o indice e o valor de acordo com o dado iterável que a função foi utilizada
