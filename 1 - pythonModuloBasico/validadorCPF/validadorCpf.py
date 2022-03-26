"""
CPF = 168.995.350-09
CPF = 16899535009
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""

#  Nesta variável ficarão os 9 primeiros digitos do CPF
primeiroBloco = ''

#  Nesta variável ficarão os 2 últimos digitos do CPF
segundoBloco = ''

# Laço para validar se o cliente digitou o CPF no formato 00000000000 ou 000.000.000-00
while True:
    #  Pessoa digita o CPF
    cpfDigitadoPeloUsuario = input("Digite seu CPF: ")

    #  Validando se a pessoa digitou somente números (00000000000)
    if cpfDigitadoPeloUsuario.isnumeric():
        #  Se sim, verifica se é Maior/Menor que 11 digitos
        if len(cpfDigitadoPeloUsuario) > 11 or len(cpfDigitadoPeloUsuario) < 11:
            print(f'Atenção! CPF Digitado não possui 11 dígitos\n'
                  f'Digite novamente!')
            continue
        # Se tiver 11 dígitos, então ele separa os 2 digitos finais do restante
        else:
            #  Excluindo os dois últimos dígitos
            primeiroBloco = cpfDigitadoPeloUsuario[:-2:]

            #  Salvando os dois últimos digitos
            segundoBloco = cpfDigitadoPeloUsuario[-2::]

    # Validando se:
    # * Tem o caractere '-' no final do CPF e se antes de haverá 11 digitos (contando com os '.')
    elif '-' not in cpfDigitadoPeloUsuario[-3::] or len(cpfDigitadoPeloUsuario[:-3:]) > 11 \
            or len(cpfDigitadoPeloUsuario[:-3:]) < 11:  # FIM da condição
        print("Digite seu CPF no formato '000.000.000-00' ")
        continue
    # Primeiro separa o dado usando o '-' depois adiciona cada bloco do CPF para uma variável, remove os pontos do
    # primeiro bloco
    else:
        separandoDado = cpfDigitadoPeloUsuario.split('-')
        primeiroBloco = separandoDado[0]
        segundoBloco = separandoDado[1]
        primeiroBloco = primeiroBloco.replace('.', '')

    # Contador que será utilizado para percorrer o array da variável primeiroBloco
    percorreArray = 0

    # Valor da soma do resultado do laço abaixo
    somaDigito = 0

    for r in range(10, 1, -1):
        #  Primeira parte do cáculo pedido no exercício
        multplicaDigito1 = int(primeiroBloco[percorreArray]) * r
        #  Armazenado a soma dos resultados
        somaDigito += multplicaDigito1
        percorreArray += 1

    # Efetuando o cálculo para descobrir o primeiro digito do CPF
    primeiroDigito = 11 - (somaDigito % 11)

    # Validando se o resultado foi maior que 9 para atribuir 0 no lugar
    if primeiroDigito > 9:
        primeiroDigito = 0

    # Concantenando o primeiro digito ao primeiro bloco do CPF
    primeiroBloco += str(primeiroDigito)

    somaDigito2 = 0
    percorreArray2 = 0

    # Mesma lógica laço for para o primeiro digito
    for r2 in range(11, 1, -1):
        multiplicaDigito2 = int(primeiroBloco[percorreArray2]) * r2
        somaDigito2 += multiplicaDigito2
        percorreArray2 += 1

    segundoDigito = 11 - (somaDigito2 % 11)

    if segundoDigito > 9:
        segundoDigito = 0

    resultadoCalculo = str(primeiroDigito) + str(segundoDigito)

    if segundoBloco == resultadoCalculo:
        print('CPF Válido!')
    else:
        print('CPF inválido!')
