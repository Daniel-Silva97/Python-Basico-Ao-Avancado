"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

# Resolução exclusiva do Python usando Zip
lista_soma = [x + y for x, y in zip(lista_a, lista_b, )]
print(lista_soma)


from itertools import zip_longest

# Resolvendo usando zip_longest
zipLongest_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(zipLongest_soma)

# Resolução em outras linguagens
lista_somas = []
for i in range(len(lista_b)):
    lista_somas.append(lista_a[i] + lista_b[i])
print(lista_somas)
