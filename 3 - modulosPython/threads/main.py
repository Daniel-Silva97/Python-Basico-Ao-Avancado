from time import sleep
from threading import Thread, Lock

# Criando uma subclasse de THREAD
# class Meuthread(Thread):
#     def __init__(self, texto, tempo):
#         self.texto = texto
#         self.tempo = tempo
#         # Recebendo o init da superclasse
#         super().__init__()
#
#     def run(self):
#         sleep(self.tempo)
#         print(self.texto)

"""
Aqui eu consigo definir vários processos rodando ao mesmo tempo em n Therads
Por padrão o Python sempre roda a Thread MAIN e se não for criada nenhuma outra
o código será executado em Top-Down, no exemplo abaixo instanciei:

Thread 1 - COnfigurada para executar 5 segundos após o código ser iniciado
Thread 2 - COnfigurada para executar 15 segundos após o código ser iniciado
Thread 3 - COnfigurada para executar 10 segundos após o código ser iniciado
Thread 4 - COnfigurada para executar 20 segundos após o código ser iniciado
Além da thread MAIN Que executará assim que iniciarmos o código

Com isso perceba que quando executo o código teremos todas essas theads rodando 
ao mesmo tempo e printando em tela de acordo com horário definido
"""


# t1 = Meuthread('Thread 1', 5)
# t1.start()
# t2 = Meuthread('Thread 2', 15)
# t2.start()
# t3 = Meuthread('Thread 3', 10)
# t3.start()
# t4 = Meuthread('Thread 4', 20)
# t4.start()

# ___MAIN___ aqui
# for i in range(20):
#     print(i)
#     sleep(1)


# ------------SEGUNDO METODO DE CRIAR THREADS-----------------------
# def vaiDemorar(texto, tempo):
#     sleep(tempo)
#     print(texto)
#
#
# t1 = Thread(target=vaiDemorar, args=('Olá Mundo!', 2))
# t1.start()

# Exemplos com N threads

# t2 = Thread(target=vaiDemorar, args=('Thread 2!', 4))
# t2.start()
#
# t3 = Thread(target=vaiDemorar, args=('Ainda não acabou, está é a Thread 3', 6))
# t3.start()
#
# t4 = Thread(target=vaiDemorar, args=('Este é o FIM! Thread 4', 8))
# t4.start()
#
# for i in range(10):
#     print(i)
#     sleep(1)


# Um método para esperar a thread concluir para executar outra ação
# t5 = Thread(target=vaiDemorar, args=('Olá Mundo!', 20))
# t5.start()
#
# while t5.is_alive():
#     print('Esperando a Thread!')
#     sleep(2)

# O comando t1.join() faz com a Thread se junte a MAIN , fazendo com que a MAIN espere ela concluir antes de executar


# Manipulando dados em Thread (exemplificando um possível problema)
class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        """LOCK
        Fará com que a Thread que acione a função em que eu usar o lock, execute somente a solicitação daquela Thread 
        até acabar, não deixará por exemplo que a MAIN e THREAD1 executem ao mesmo tempo a função comprarIngresso()
        
        a primeira que chegar executará tudo, e depois quando a thread acaba a próxima executa
        """
        self.lock = Lock()  # inicializando o Lock

    def comprarIngresso(self, quantidade):
        self.lock.acquire()  # Neste momento quando uma Thread acionar a função, ela será bloqueada
        # temporariamente para outras Threads
        if self.estoque < quantidade:
            print('Não temos ingressos suficientes!')
            self.lock.release()  # Como aqui tem o return, preciso executar este comando para liberar a função para
            # as próximas threads
            return

        sleep(1)  # para quebrar a Thread que criei abaixo

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingressos! '
              f'Ainda temos {self.estoque} disponíveis.')

        self.lock.release()  # Segunda saída da função, novamente liberando para outras threads


if __name__ == '__main__':
    ingressos = Ingressos(10)

    threads = []  # Criando uma lista de threads para executar no laço todas de uma vez
    for i in range(1, 20):
        t = Thread(target=ingressos.comprarIngresso, args=(i,))
        threads.append(t)  # Adicionando a thread a lista

    for t in threads:  # Inicializando as threads com o laço
        t.start()

    executando = True  # variável de controle
    while executando:
        executando = False  # Alterando para False para sair do laço quando o for abaixo deixar de ser verdadeiro

        for t in threads:
            if t.is_alive():  # verificando se a Thread está ativa
                executando = True
                break

    print(ingressos.estoque)  # Executo somente após as Threads acima finalizarem.
