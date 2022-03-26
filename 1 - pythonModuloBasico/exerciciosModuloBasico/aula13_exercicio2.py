"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.:
Bom dia 0 - 11
Boa tarde - 12 - 17
Boa noite 18 - 23
"""

horarioCompleto = ""
hora = ""
minuto = ""

while True:
    horarioCompleto = input("Digite o horário: ")

    if ":" not in horarioCompleto:
        print("Horário inválido!")
        continue
    else:
        hora = horarioCompleto.split(":")[0]
        minuto = horarioCompleto.split(":")[1]
    if not hora.isdigit():
        print("Horário inválido")
        continue
    elif not minuto.isdigit():
        print("Horário inválido")
        continue
    else:
        hora = int(hora)
        minuto = int(minuto)
    if 0 < hora > 23:
        print("Horário permitdo somente de 0 a 23:59!")
        continue
    else:
        break

if 0 <= hora <= 11:
    print("Bom dia!")
elif 12 <= hora <= 17:
    print("Boa tarde!")
elif 18 <= hora <= 23:
    print("Boa noite!")
