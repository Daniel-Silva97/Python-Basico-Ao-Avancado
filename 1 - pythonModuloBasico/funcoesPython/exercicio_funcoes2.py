"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.
"""


def func1():
    return 10 + 6


def func2():
    return func1()


print(func2())

"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.
Faça a função1 executar duas funções que recebam um número diferente de argumentos.
"""


def funcaoMestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}!'


def falaOi(nome):
    return f'Oi {nome}'


executandoPrimeiraFuncao = funcaoMestre(falaOi, 'Daniel')
executandoSegundaFuncao = funcaoMestre(saudacao, 'Daniel', 'Bom dia')

print(executandoPrimeiraFuncao)
print(executandoSegundaFuncao)