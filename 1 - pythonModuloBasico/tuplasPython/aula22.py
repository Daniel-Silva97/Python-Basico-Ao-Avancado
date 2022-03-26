"""
Tuplas em Python
"""
# Criando uma tupla
tupla = (1, 2, 3, 'a', 'Daniel')
# OU
tupla2 = 1, 2, 3, 'a', 'Daniel'

# Mostrando elememtos da tupla
for v in tupla:
    print(v)

# Fatiamento Tuplas
print(tupla[2::])

# Convertendo a tupla em lista
tupla = list(tupla)
# Editando a lista
tupla[1] = 99
# Voltando pra tupla
tupla = tuple(tupla)
print(tupla)
