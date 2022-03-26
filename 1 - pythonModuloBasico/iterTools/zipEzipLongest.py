
"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""
from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']

# Zip cria um gerador quando executado, une somente até o tamanho da menor lista
cidadesEstados = zip(indice, cidades, estados)

# Iterando nesse gerador
for v in cidadesEstados:
    print(v)


# Une os dados sempre olhando para a maior lista, se não achar o par informa None
cidadesEstadosLongest = zip_longest(cidades, estados, fillvalue='Estado não encontrado na lista menor')

# Iterando nesse gerador
for v in cidadesEstadosLongest:
    print(v)