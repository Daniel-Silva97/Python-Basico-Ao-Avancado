"""
Operador OR
"""


nome = input("Qual o seu nome: ")

#  Sem usar o operador OR

if nome:
    print(nome)
else:
    print('Você não digitou nada!')

# Simplificando com OR

print(nome or 'Você não digitou nada!')

#  Exemplo 2
a = 0  # Retorna False
b = None  # False
c = False  # False
d = []  # False
e = {}  # False
f = 22  # True
g = 'Daniel'  # True

#  Armazenando primeiro valor True em uma variável com OR
variavel = a or b or c or d or e or f or g

print(variavel)