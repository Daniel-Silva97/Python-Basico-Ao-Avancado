"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
# """
# # Indices 0    1    2    3    4     5
# lista = ['A', 'B', 'C', 'D', 'E', 10.5]
# #        -6   -5   -4   -3   -2   -1
#
# lista[5] = 'Alterando'  # Alterando um item da lista via Indice
# print(lista[0:3])  # Listando em tela os itens do indice 0 ao 2, não inclui o 3
# print(lista[:3])  # Mesmo comando do acima, mas sem mencionar o inicio (Padrão 0)
# print(lista[-1])  # último item da lista
# print(lista[::2])  # Pega do primeiro item da lista da seguinte forma: exibe, não exibe, exibe ...


lista1 = [1, 2, 3]
print(lista1)

lista2 = [4, 5, 6]
print(lista2)

lista3 = lista1 + lista2  #  Concatenado as duas listas em uma nova variável
print(lista3)

lista1.extend(lista2)  # Lista1 receberá os valores de lista 2
print(lista1)

lista2.append('Adicionando')  # Adicionando um item ao final da lista
print(lista2)

lista1.insert(0, 'Adicionando') # insert(indice, valor) adicionando um valor em qualquer lugar da lista
print(lista1)

lista2.pop()  # Removendo o último item da lista
print(lista2)

del(lista3[3:5]) # Removendo um trecho da lista neste caso do item 3 e 4, o último não é excluído
print(lista3)

print(max(lista3))  # Imprime o maior valor da lista
print(min(lista3))  # Imprime o menor valor da lista

"""
Criando uma lista usando range

Necessário usar o comando list para criar a lista porque somente a função range
retorna um objeto iterável, e a variável lista4 ficaria com o valor = "range(1, 10)" se não 
colocar a função list para percorrer pelo objeto do range, ai retorna todos os valores possíveis dentro
da lista igual o exemplo abaixo.

"""
lista4 = list(range(1, 10))
print(lista4)

#  Iteragindo com a lista

for valor in lista4:
    print(valor)
# OU
somar = 0
for valor in lista4:
    somar += valor
print(somar)


lista5 = ['String', 10.5, 10, True]

for valor in lista5:
    print(type(valor))