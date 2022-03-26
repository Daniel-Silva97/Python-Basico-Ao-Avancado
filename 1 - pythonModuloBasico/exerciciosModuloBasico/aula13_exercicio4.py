# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou
# igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"
diaSemana = ""
controle = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
correcaoDia = ["Terca", "Sabado"]

while diaSemana not in controle:
    diaSemana = input("Digite um dia da semana: ").capitalize()

    if diaSemana == correcaoDia[0]:
        diaSemana = "Terça"
        continue
    elif diaSemana == correcaoDia[1]:
        diaSemana = "Sábado"
        continue

if diaSemana == controle[5] or diaSemana == controle[6]:
    print("Hoje é dia de descanso!")
else:
    print("Você precisa trabalhar!")
