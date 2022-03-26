"""
Quando defino um padrão para um parâmetro, todos os parâmetros após 
ele devem ser definidos um default também, senão o programa apresentará
erro.
"""

# def func(a1, a2, a3, a4, a5, nome=None, a6):
#     print(a1, a2, a3, a4, a5, nome, a6)
#
# var = func(1, 2, 3, 4, 5, nome='Daniel', 6)


#  Após definir padrão o sistema seguirá normalmente
# def func(a1, a2, a3, a4, a5, nome=None, a6=None):
#     print(a1, a2, a3, a4, a5, nome, a6)
#     # Sobre retornar dados a variável
#     return nome, a6
#
#
# # Quando definido o padrão tenho que vincular ao parâmetro responsável senão apresenta erro
# # Errado
# # var = func(1, 2, 3, 4, 5, nome='Daniel', 6)
#
# # Correto
# func(1, 2, 3, 4, 5, nome='Daniel', a6=6)
#
# # Se eu quiser que a função retorne um valor pra minha váriavel devo utilizar
# # "return" para dizer o que eu quero que a função atribua a variável
# # Ele cria uma tupla com os valores que eu informar no return
# var = func(1, 2, 3, 4, 5, nome='Daniel', a6=6)
#
# #  Visualizar a tupla da variável
# print(var)

"""
Funções (def) em Python - *args **kwargs -

*args - qualquer argumento enviado a função
**kwargs - Qualquer argumento nomedo enviado a função
"""


#  Quando eu não sei quantos argumentos irei usar na função, posso utilizar o args
#  Args sempre me gerará uma tupla com os argumentos

def func2(*args, **kwargs):
    print(args)
    #  pegando o 1 argumento da da Tupla
    print(args[0])
    #  Pegando o ultimo argumento da Tupla
    print(args[-1])
    #  Pegando o tamanho da tupla
    print(len(args))
    # Para converter o args de Tupla em lista
    lista = list(args)
    lista[0] = 20
    print(lista)

    #  Separando os valores da tupla em um laço
    for v in args:
        print(v)
    # Printando só os argumentos nomeados
    print(kwargs.get('nome'))


# Chamando a função
func2(1, 2, 3, 4, 5, 6, nome='Daniel', sobrenome='Silva')
