"""
Gerenciadores de contexto
"""

# Sem Gerenciador de contexto preciso do arquivo.close()

# arquivo = open('abc.txt', 'w')
# arquivo.write('Alguma coisa')
# arquivo.close()


# Com Gerenciador de contexto não preciso do arquivo.close()
# with open('abc.txt', 'w') as arquivo:
#     arquivo.write('Alguma coisa')


# Criando um Gerenciador de contexto
# class Arquivo:
#     # Inicializador para inicializar os atributos
#     def __init__(self, arquivo, modo):
#         print('Abrindo o arquivo')
#         self.arquivo = open(arquivo, modo)
#
#     def __enter__(self):
#         print('Retornando o arquivo')
#         return self.arquivo
#
#     # exc_type, exc_val e exc_tb são parãmetros que armazenam quando há alguma execeção no código
#     # O tipo, valor e traceback
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('Fechando o arquivo')
#         self.arquivo.close()
#         # Mostrando o que é armazenado em caso de exceção
#         print(exc_tb)
#         print(exc_val)
#         print(exc_type)
#
#
# with Arquivo('abc.txt', 'w') as arquivo:
#     arquivo.write('Alguma coisa')
#     # Forçando exceção
#     sadjaksjda.write('erro')


"""
Segundo formato para criar Gerenciadores de contexto
"""

from contextlib import contextmanager


# Uso este decorador para informar que a função será um Gerenciador de contexto
@contextmanager
def abrir(arquivo, modo):
    try:
        print('Abrindo Arquivo')
        arquivo = open(arquivo, modo)
        # Usando yield para que a função não pare aqui, como seria com return, assim ela fará os próximos passos
        yield arquivo
    finally:
        print('Fechando o arquivo')
        arquivo.close()


with abrir('abc.txt', 'w') as arquivo:
    arquivo.write('Linha 1 \n')
    arquivo.write('Linha 2 \n')
    arquivo.write('Linha 3 \n')

"""
Quando uso o método 1 (CLASSE) para criar o gerenciador de contexto
preciso informar os métodos __enter__ e __exit__ para que o gerenciador funcione
corretamente

Já no método 2, preciso criar a função usando o yield para ela funcionar corretamente e 
com o decorador @contextmanager

Os gerenciadores de contexto só funcionarão se chamados por meio do "with"
"""