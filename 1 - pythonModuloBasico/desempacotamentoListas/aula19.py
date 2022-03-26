"""
Desempacotamento de listas em Python
"""

lista = ['João', 'Maria', 'Daniel', 'Danilo']

n1, n2, n3, n4 = lista  # Desempacotei a lista criando o número de variáveis equivalente ao número de elementos

print(n2)

# Se eu estiver com uma lista muito grande e não quiser criar uma variável para cada elemento, posso fazer da
# seguinte forma:
m1, m2, *resto_lista = lista

print(m2)
print(resto_lista)
