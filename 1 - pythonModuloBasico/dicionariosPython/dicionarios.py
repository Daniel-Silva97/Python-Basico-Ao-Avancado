"""
Dicionários em python

Semelhante as listas, a diferença é que no dicionário é possível controlar o indice e o valor
"""
#  Criando o dicionário
dicionario1 = {'chave1': 'Valor da chave'}  # Método mais usado
# Outra forma de criar o dicionário
dicionario2 = dict(chave2='Valor da chave', chave3='Valor da outra chave')

#  Adicionando uma nova chave
dicionario1['Nova chave'] = 'Valor da nova chave'

print(dicionario1['chave1'])

# Posso nomear como chave qualquer valor imutável
dicionario3 = {
    'str': 'String',
    123: 'Números',
    (1, 2, 3, 4): 'Tupla'
}
#  Quando não encontrada a chave no dicionário, se não estiver dentro de condicionais o código irá para
#  Sempre tratar com condicionais para caso não encontrar a chave não travar o código
if dicionario3.get('str') is not None:
    print(dicionario3.get('nova_chave'))
print(123)

# Atualizando dados em um dicionário
dicionario1.update({'Nova': 'Novo Valor'})

# Removendo do dicionário
del dicionario1['Nova chave']

#  Checando se existe o valor no dicionário pela chave
print('str' in dicionario3)
print('str' in dicionario3.keys())

# Checando se existe o valor no dicionário pelo valor
print('Novo Valor' in dicionario1.values())

# Consultando o tamanho do dicionário (em Pares Chave/Valor)
print(len(dicionario1))

# Iterando os valores do dicionário

# Acessando somente as chaves
for keys in dicionario3:
    print(keys)

# OU
for keys in dicionario2.keys():
    print(keys)

# Acessando os valores do dicionário
for values in dicionario3.values():
    print(values)

# Acessando Chaves e Valores do dicionário
for dic in dicionario3.items():
    print(dic)  # Imprime chave e valor em tuplas
    print(dic[0], dic[1])  # Imprime chave e valor separados

# Dicionário dentro de dicionários

clientes = {
    'cliente1': {
        'nome': 'Daniel',
        'sobrenome': 'Silva',
    },
    'cliente2': {
        'nome': 'Maria',
        'sobrenome': 'Eduarda',
    },
}

# Iterando o dicionário acima
for clientes_keys, clientes_values in clientes.items():
    print(f'Exibindo {clientes_keys}')
    for dados_keys, dados_values in clientes_values.items():
        print(f'\t{dados_keys} = {dados_values}')


# Quando atribuimos um dicionário a uma váriável em python
# Se alterarmos o valor na váriavel o dicionário também será alterado, por exemplo
d1 = {1: 'a', 2: 'b', 3: 'c'}
v = d1

v[1] = 'Daniel'
# Ambos apontam para o mesmo local em memória
print(f'Dicionário {d1}')
print(f'Variável {v}')

# Se quero copiar sem alterar o dicionário principal, devo usar:
v1 = d1.copy()  # Criando uma cópia rasa do dicionário
v1[1] = 'Maria'

print(f'Dicionário {d1}')
print(f'Variável {v1}')

# CAST em dicionário
# Pode ser feito somente com dados que tenham 'Chave' e 'Valor'
# Por exemplo

# Listas
lista = [
    ['a1', 1],
    ['a2', 2],
    ['a3', 3],
]

converteLista = dict(lista)
print(converteLista)

# Tuplas
tupla = (
    ('a1', 1),
    ('a2', 2),
    ('a3', 3),
)

converteTupla = dict(tupla)
print(converteTupla)

# Eliminando um item especifico usando pop
converteTupla.pop('a3')
print(converteTupla)

# Eliminando o último item independete de qual seja
converteLista.popitem()
print(converteLista)

# adicionando um dicionário um no outro
dicionario3.update(dicionario2)
print(dicionario3)