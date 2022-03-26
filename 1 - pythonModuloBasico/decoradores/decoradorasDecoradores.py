"""
Funções decoradoras e decoradores
"""


def master(funcao):
    # Função decoradora
    # *args e **kwargs inclusos para evitar o erro de parâmetros
    def slave(*args, **kwargs):
        print('Agora estou decorada!')
        # *args e **kwarg inclusos aqui também
        funcao(*args, **kwargs)
    return slave


# Decorador
@master
def falaOi():
    print('Oi')


@master
# Quando a função recebe parâmetros, a função decoradora deve ter o parâmetro *args e **kwargs
# para funcionar sem erros igual exemplo abaixo:
def outraFuncao(msg):
    print(msg)


outraFuncao('Olá, eu sou o Daniel!')
