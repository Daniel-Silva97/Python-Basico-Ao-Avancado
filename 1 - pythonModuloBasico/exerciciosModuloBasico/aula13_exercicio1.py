"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero1 = 0

while True:
    try:
        numero1 = int(input("Digite um número: "))
    except ValueError:
        print("Número inválido, digite novamente!")
        continue
    if numero1 < 0:
        print("Número não pode ser negativo!")
        continue
    else:
        break
if numero1 % 2 == 0:
    print("Número Par!")
else:
    print("Número ímpar")






