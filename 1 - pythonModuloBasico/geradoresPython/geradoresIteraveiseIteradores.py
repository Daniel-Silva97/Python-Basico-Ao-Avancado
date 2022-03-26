"""
Geradores, Iteradores e Iteráveis
"""
from datetime import time

lista = [0, 1, 2, 3, 4, 5]

#  Verificando se objeto é iterável
print(hasattr(lista, '__iter__'))

"""
Iterável - te retorna todos os valores e não 1 por vez, você pode iterar mas precisa de um laço ou alguma funcionalidade
pra isso
Iterador - Irá te retorna um valor de cada vez usando o método Next

Por exemplo:

"""
iteravel = [0, 1, 2, 3, 4, 5]
print(iteravel)

iterador = iter([0, 1, 2, 3, 4, 5])
print(next(iterador))
print(next(iterador))
print(next(iterador))

"""
Geradores nos enviam os dados conforme eles forem gerados  ou solicitados
em um tipo de operação chamado Lazy Evaluation.

Ele funciona com uma iterador, então podemos usar a função next e iter

Por exemplo
"""
import time


def gerador():
    for n in range(100):
        yield n
        time.sleep(0.1)


g = gerador()

for v in g:
    print(v)


"""Iteradores e geradores só podem ser consumidos uma única vez"""