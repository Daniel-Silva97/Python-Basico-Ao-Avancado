"""
Perguntas e Respostas usando dicionários
"""

perguntas = { # Primeiro dicionário agrupa todas as perguntas/respostas
    'Pergunta 1': {  # Segundo dicionário agrupa a pergunta e sua resposta
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {'a': '1', 'b': '4', 'c': '5', 'd': '6'},  # Terceiro dicionário agrupa as opções de resposta
        'resposta_certa': 'b'  # Onde informamos qual resposta é a certa
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3 * 2?',
        'respostas': {'a': '1', 'b': '4', 'c': '5', 'd': '6'},
        'resposta_certa': 'd'
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 8 * 2?',
        'respostas': {'a': '16', 'b': '1', 'c': '5', 'd': '6'},
        'resposta_certa': 'a'
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 10 - 5?',
        'respostas': {'a': '1', 'b': '4', 'c': '5', 'd': '6'},
        'resposta_certa': 'c'
    },
}

# Armazenando quantas respostas o usuário acertou
respostas_certas = 0

# Percorrendo o primeiro dicionário para acessar as perguntas
for perguntas_keys, perguntas_values in perguntas.items():
    print(f'{perguntas_keys}: {perguntas_values["pergunta"]}')
    print()
    # Percorrendo o terceiro dicionário para acessar as respostas
    for resposta_key, resposta_value in perguntas_values['respostas'].items():
        # Exibindo as opções do terceiro dicionário para o usuário escolher
        print(f'[{resposta_key}]: {resposta_value}')
    # Perguntando ao usuário a resposta dele
    resposta_usuario = input('Sua resposta: ')
    print()

    # Interagindo com usuário e gravando na variável quando ele acertar a resposta
    if resposta_usuario == perguntas_values['resposta_certa']:
        print('Você Acertou!!!!!!')
        respostas_certas += 1
    else:
        print('Você errou! :(')

# Contando quantas perguntas tem
qtd_perguntas = len(perguntas)
# Calculando a % de acerto
porcentagem_acerto = respostas_certas / qtd_perguntas * 100


print(f'Você acertou {respostas_certas} respostas!')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')
