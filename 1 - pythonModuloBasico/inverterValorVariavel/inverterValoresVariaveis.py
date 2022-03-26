"""
Inverter os valores de variáveis
"""

x = 10
y = 'Daniel'
z = 'Silva'

x, y = y, x  # Atribuindo a X o valor de Y e atribuindo ao Y o valor de X

print(f'X = {x} e Y = {y}')

x, y, z = z, x, y  # O mesmo com 3 variáveis

print(f'X = {x} e Y = {y} e Z = {z}')
