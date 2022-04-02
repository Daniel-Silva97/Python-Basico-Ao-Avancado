"""
Pilhas e Filas
Pilha (stack) - LIFO - last in, first out
    Exemplo: Pilha de livros que são adicionados um sobre o outro.

Fila (queue) - FIFO - first in, first out.
    Exemplo: uma fila de banco
Filas podem ter efeitos colaterais em desempenho, porque a cada item alterado,
todos os indices são modificados.
"""
# Pilhas exemplo
# livros = list()
# livros.append('Livro 1')  # 1 - Primeiro a ser incluido
# livros.append('Livro 2')  # 2
# livros.append('Livro 3')  # 3
# livros.append('Livro 4')  # 4
# livros.append('Livro 5')  # 5 - Primeiro a ser removido
# livro_removido = livros.pop()  # 5
# livro_removido = livros.pop()  # 4
# print(livros, livro_removido)

""" Deque

Irá gerenciar a fila na lista, pois como removo o primeiro item da lista e não
o último, todos os dados da fila andam um indice pra frente. Por exemplo


Indice- [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Lista - [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Removi o 1, então

Indice- [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Lista - [2, 3, 4, 5, 6, 7, 8, 9, 10]

Como isso pode gerar um problema de desempenho devido toda essa alteração,
o deque gerencia as alterações automaticamente quando ocorre uma remoção

"""
from collections import deque
from time import sleep

# Filas Exemplos
# fila = deque()
# fila.append('Daniel')
# fila.append('Marcelo')
# fila.append('Alex')
# fila.append('Maria')
# fila.append('Ana')
# fila.append('Jessica')
# fila.append('Lucas')
#
# print(f'{fila.popleft()} saiu da fila.')
# for num, nome in enumerate(fila):
#     if num == 0:
#         num += 1
#         continue
#     print(num, nome)


"""Parâmetro maxlen
Este parâmetro controla o tamanho da fila, como informei 5 a lista
só terá ATÉ 5 elementos, e quando incluo um sexto elemento, acontecerá 
o seguinte:

listaatual - [1, 2, 3, 4, 5]
Incluo o '6'
O maxlen tratará removendo o 1 e incluindo o 6, ficando:
listaNova - [2, 3, 4, 5, 6]
"""
filaComTamanhoMaximo = deque(maxlen=5)
filaComTamanhoMaximo.extend([1, 2, 3, 4])
filaComTamanhoMaximo.append(5) # Antigi o tamanho máximo da lista
print(filaComTamanhoMaximo)
filaComTamanhoMaximo.append(6) # Ultrapassei o limite
# logo:
print(filaComTamanhoMaximo)

catraca = deque(maxlen=10)

for pessoa in range(100):
    catraca.append(pessoa)
    sleep(1)
    print(catraca)



