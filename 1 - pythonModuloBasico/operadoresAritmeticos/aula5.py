"""
Operadores Aritméticos

São eles:

+, -, *, /, //, **, %, ()

"""

print('Multiplicação', 10 * 10)  # Multiplicação
print('Adição', 10 + 10)  # Adição
print('Subtração', 10 - 10)  # Subtração
print('Divisão', 10 / 3)  # Divisão

print('Divisão inteira', 10.5 // 3)  # Divisão Inteira
print('Potenciação/Exponenciação', 2 ** 3)  # Potenciação/Exponenciação
print('Módulo da divisão (Resto)', 12 % 7)  # Módulo da divisão (Resto)

# () Para alterar a precedência do cálculo

print(2 + 5 * 10)  # Multiplicação antes da soma
print((2 + 5) * 10)  # Alterando a precedência para soma antes da Multiplicação
