"""
* Sets em Python

* add(Adiciona), update(Atualiza), clear, discard
* union | (une)
* intersection & (Todos os elementos presentes nos dois sets)
* difference - (elementos apenas no set da esquerda)
* symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)
"""

# A criação dos sets é muito semelhante ao dicionário mas a diferença é que
# que não informamos chave, somente os valores, semelhante à lista.
# Não tenho indíces em set, portanto tenho de iterar em laços

set1 = {1, 2, 3, 4, 5}  # Aceita somente valores imutáveis

print(set1)

# Iterando em set
for v in set1:
    print(v)

# Adicionando valores em set
set1.add(7)
print(set1)

# Apagando valores no set
set1.discard(2)
print(set1)

# Alterando os sets
set1.update('Python')  # Ele itera sobre os elementos semelhante ao laço

# Não aceita elementos duplicados, então podemos usar da seguinte maneira
lista = [1, 1, 1, 1, 1, 2, 3, 3, 5, 6, 6, 6, 'Daniel', 'Daniel']
# Removendo os duplicados fazendo um CAST para set
# Set não respeita as ordens dos elementos, então ele reordena tudo no CAST
lista = set(lista)
print(lista)

# Após remover os duplicados, posso converter para lista novamente se necessário
lista = list(lista)
print(lista)

# Utilizando Union / Intersection / Difference / Symmetric Difference
set2 = {1, 2, 3, 4, 5, 7}
set3 = {1, 2, 3, 4, 5, 6}

# Unindo os sets com union
set4 = set2 | set3
# OU
# set4 = set2 union set3
print(set4)

# Intersecção, verificando os elementos presentes nos dois sets
set5 = set2 & set3
# OU  set5 = set2 intersection set3
print(set5)

# Irá retornar o elemento no set da esquerda que não está no set da direita
set6 = set2 - set3
# OU set6  = set2 difference set3
print(set6)

# Symmetric difference, ve os elementos dos dois sets e retorna os elementos que não se repetem nos dois
set7 = set2 ^ set3
print(set7)

# Quando tenho 2 listas com os mesmos valores mas em uma delas o
# valor está duplicado, mas quero validar se os valores são iguais
# faço o CAST para SET e valido se são iguais

# Lista com os mesmo valores, porém uma delas repete os dados
lista3 = ['Daniel', 'Maria', 'Jéssica']
lista4 = ['Daniel', 'Maria', 'Maria', 'Maria', 'Maria', 'Maria', 'Jéssica', 'Jéssica', 'Jéssica', 'Jéssica', 'Jéssica']
# # Verificando se as listas são diferentes antes do CAST
# print(lista3 != lista4)
# # Fazendo o CAST das listas
# lista3 = set(lista3)
# lista4 = set(lista4)
# # Verificando agora se as duas são diferentes
# print(lista3 != lista4)

# Se não quero modificar a minha lista original, posso criar uma condicional para validar
if set(lista3) == set(lista4):
    print('Lista 3 é igual Lista 4')
else:
    print('Lista 3 é diferente da Lista 4')
