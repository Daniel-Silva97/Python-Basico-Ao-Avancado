"""
Expressões LAMBDA (funções anonimas)
"""


#  Função comum
def funcao(arg1, arg2):
    return arg1 * arg2


var = funcao(2, 2)
print(var)

# Expressão lambda que faz a mesma coisa
a = lambda arg1, arg2: arg1 * arg2
print(a(2, 2))


# Quando usar LAMBDA?
# Exemplo:
lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8]
]

#  Usando lambda dentro do parâmetro key para passar o indice um da lista (Valores 6, 7 ...) como base para ordernar
lista.sort(key=lambda item: item[1], reverse=True)
print(lista)

# Outra forma de ordernar mas sem modificar a variável
print(sorted(lista, key=lambda i: i[0], reverse=True))
