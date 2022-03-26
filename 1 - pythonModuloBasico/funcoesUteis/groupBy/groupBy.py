"""
Group By
"""
from itertools import groupby, tee

alunos = [
    {'nome': 'Luiz', 'nota':'A'},
    {'nome': 'Daniel', 'nota':'B'},
    {'nome': 'Maria', 'nota':'C'},
    {'nome': 'Bruno', 'nota':'D'},
    {'nome': 'Carlos', 'nota':'E'},
    {'nome': 'Jessica', 'nota':'F'},
    {'nome': 'Lucas', 'nota':'B'},
    {'nome': 'Anderson', 'nota':'C'},
    {'nome': 'José', 'nota':'A'}
]

# Lambda para ordenar o dicionário
ordena = lambda item: item['nota']


# Ordenando os alunos pelas notas
alunos.sort(key=ordena)

# Conferencia da ordenação
# for aluno in alunos:
#     print(aluno)


alunosAgrupados = groupby(alunos, ordena)

for agrupamento, valoresAgrupados in alunosAgrupados:
    va1, va2 = tee(valoresAgrupados)

    print(f'Agrupamento {agrupamento}')

    for aluno in va1:
        print(f'\t{aluno["nome"]}')

    quantidade = len(list(va2))
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
    print()
