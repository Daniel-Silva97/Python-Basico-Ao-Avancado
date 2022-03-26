import random
from random import randint
numeroUsuario = ''

while True:
    try:
        numeroUsuario = int(input("Me diga um número: "))
        break
    except ValueError:
        print("Isto não é um valor válido! Digite novamente")
        continue

numeroMaquina = random.randint(1, 10)
resultado = numeroUsuario + numeroMaquina

escolha = input("Você quer Par ou Impar: ")

if escolha == 'Par' and resultado % 2 == 0:
    print(f'{resultado} é Par! '
          f'O Usuário venceu!')
elif escolha == 'Ímpar' and resultado % 2 != 0:
    print(f'{resultado} é Impar! '
    f'O Usuário venceu!')
else:
    print(f"A máquina venceu")



