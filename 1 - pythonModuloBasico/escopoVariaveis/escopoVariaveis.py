"""
Escopo de variáveis em Pyhton
"""
#  Escopo Global - Acessível em todos os locais
variavel = 'valor'


def func():
    print(variavel)


def func2():
    # Escopo local - Acessível somente nesta função, apesar de ter o mesmo nome
    # Python cria outra variável dentro do código, ou seja não é a mesma variável do
    # escopo global
    variavel = 'Outro valor'
    print(variavel)


func()
func2()
print(variavel)
