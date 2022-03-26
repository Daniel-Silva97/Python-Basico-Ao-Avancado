"""
Levantando exceções com Raise
"""


# função para dividir números
def divide(n1, n2):
    try:
        return n1 / n2
    # Se eu não informar o raise aqui no except, o outro except não receberá o erro
    except ZeroDivisionError as errors:
        print(f'Erro da primeira except: {errors}')
        # Para ver o segundo except ter problema comentar o "raise"
        raise


try:
    print(divide(2, 0))
# Sem o raise do primeiro try ... except aqui retornaria None
except ZeroDivisionError as error:
    print(f'Erro da segunda except: {error}')

