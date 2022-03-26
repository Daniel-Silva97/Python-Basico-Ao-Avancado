"""
Problema parâmetros mutáveis em funções
Objetos mutáveis
Listas, dicionários

Objetos imutáveis
Tuplas, strings, números, boolean, None

"""


# Passando um valor mutável no parâmetro Lista,
# isso faz com que o sistema tenha um comportamento incorreto quando executado
# def listaClientes(clientes_iteravel, lista=[]):
#     lista.extend(clientes_iteravel)
#     return lista

# Para resolver usar None por exemplo que é um valor imutável
def listaClientes(clientes_iteravel, lista=None):
    # Se a lista retornar None, ou seja, não informei o parâmetro, então:
    if lista is None:
        # Converto ela em lista
        lista = []
    # Assim, minhas listas não unificam quando a função é chamada
    lista.extend(clientes_iteravel)
    return lista


clientes1 = listaClientes(['João', 'Maria', 'Eduardo'])
clientes2 = listaClientes(['Marcos', 'Jonas', 'Zico'])

print(clientes1)
print(clientes2)
