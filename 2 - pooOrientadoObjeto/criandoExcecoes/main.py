"""
Criando exceções (Tratamento de Erros)
"""


class TaErradoError(Exception):
    pass


def testar():
    raise TaErradoError('Ensinando a tratar Erros desconhecidos')


try:
    testar()
except TaErradoError as error:
    print(f'Erro: {error}')
