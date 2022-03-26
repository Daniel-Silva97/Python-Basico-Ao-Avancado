"""
while em Python

Utilizado para realizar ações enquanto uma condição for
verdadeira.

Requisitos: Entender condições e operadores

"""

x = 0 # Variável de controle

while x < 100:

    print(x)
    x += 1 # Atribuindo +1 a X

print("Acabou")


y = 0

while y < 10:
    z = 0
    while z < 5:
        print(f'{y},{z}')
        y+=1
    x+=1