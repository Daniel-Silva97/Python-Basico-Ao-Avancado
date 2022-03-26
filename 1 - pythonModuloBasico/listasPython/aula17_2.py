"""
FOR / ELSE em Python
"""

variavel = ['Daniel', 'Danilo', 'Lucas', 'Jéssica']

for valor in variavel:
    if valor.startswith('L'): # startswith checa se a string começa com determinada letra
        print('Começa com L', valor)
    else:
        print('Não começa com L', valor)


