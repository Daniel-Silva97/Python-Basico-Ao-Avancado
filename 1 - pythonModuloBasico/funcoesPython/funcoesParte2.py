"""
Funções em Python - return (Parte 2)
"""


def divisao(n1, n2):
    if n1 == 0 or n2 == 0:
        return

    return n1 / n2


divide = divisao(2, 2)

if divide:
    print(divide)
else:
    print('Conta inválida!')
