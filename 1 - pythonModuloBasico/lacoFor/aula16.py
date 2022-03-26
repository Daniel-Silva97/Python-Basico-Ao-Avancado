"""
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
"""
texto = 'Python'
nova_string = ''

for letra in texto:
    print(letra)

print(f'###########################')
#  No range, o start e step vem com padrões 0 e 1, posso informar somente
#  o stop, mas se eu quiser que ele faça o range na ordem decrescente, devo
#  fazer igual exemplo abaixo
for numero in range(20, 10, -1):
    print(numero)

print(f'###########################')

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)