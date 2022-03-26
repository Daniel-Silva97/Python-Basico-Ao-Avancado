"""
Faça uma lista de tarefas com as seguintes opções:
--> Adicionar Tarefas
--> Listar Tarefas
--> Opção de desfazer
--> Opção de refazer

Ex:
['Tarefa 1', 'Tarefa 2']
['Tarefa 1'] <-- Desfazer
['Tarefa 1', 'Tarefa 2'] <-- Refazer
"""


# Função para exibir as Tarefas no console
def listarTarefas(listar):
    for indice, tarefa in enumerate(listar):
        print()
        print(f'A tarefa {indice + 1} é: {tarefa}')


# Incluindo na lista a tarefa digitada
def adicionarTarefas(adicionar):
    listaTarefas.append(adicionar)


# Para desfazer a última operação
def desfazerOperacao(listaDeTarefas, refazerTarefas):
    # Se não houver nenhuma tarefa na lista, retorna esta mensagem
    if not listaDeTarefas:
        print(f'\t Nada a desfazer')
        return
    # Excluindo o último elemento da lista
    ultimaLista = listaDeTarefas.pop()
    # Igualando a lista de Refazer para caso queira voltar a operação
    refazerTarefas.append(ultimaLista)


# Refazendo a operação
def refazerOperacao(listaDeTarefas, refazerTarefas):
    # Se a lista de refazer estiver vazia
    if not refazerTarefas:
        print(f'\t Nada a refazer')
        return
    # Dropa o último refazer
    ultimoRefazer = refazerTarefas.pop()
    # Inclui na lista o ultimo incluido (refazendo)
    listaDeTarefas.append(ultimoRefazer)


# só cria essas listas se executar este arquivo
if __name__ == '__main__':
    listaTarefas = []
    refazerLista = []

while True:
    print()
    comando = input(f'Digite um dos comandos abaixo para nos dizer como deseja prosseguir:\n'
                    f'\t--> "1" para "Adicionar"\n'
                    f'\t--> "2" para "Listar"\n'
                    f'\t--> "3" para "Desfazer"\n'
                    f'\t--> "4" para Refazer\n\n'
                    f'Digite aqui: ')

    if int(comando) == 1:
        incluindoTarefa = input('Qual o nome da tarefa? ')
        adicionarTarefas(incluindoTarefa)
        continue
    elif int(comando) == 2:
        listarTarefas(listaTarefas)
        continue
    elif int(comando) == 3:
        desfazerOperacao(listaTarefas, refazerLista)
        continue
    elif int(comando) == 4:
        refazerOperacao(listaTarefas, refazerLista)
        continue
