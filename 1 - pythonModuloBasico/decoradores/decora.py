from time import time
from time import sleep


# Função decoradora
def velocidade(funcao):
    # Função para calcular o tempo de execução da função demora
    def interna(*args, **kwargs):
        # Pegando o tempo antes de executar a função
        startTime = time()
        # executando a função
        resultado = funcao(*args, **kwargs)
        # Tempo após o final da execução
        end_time = time()
        # calculando o tempo de execução
        tempo = (end_time - startTime) * 1000
        # exibindo o tempo de execução da função
        print(f'A função executou em {tempo:.2f}ms.')
        return resultado
    return interna


# Decorador da função decoradora
@velocidade
def demora():
    for i in range(5):
        print(i)
        sleep(1)


demora()
