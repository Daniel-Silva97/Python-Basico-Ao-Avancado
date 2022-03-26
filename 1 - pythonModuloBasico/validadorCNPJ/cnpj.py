"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segundo digito
"""

import re


def validaCNPJ(cnpj):
    cnpj = removerCaracteresEspeciais(cnpj)
    cnpj = removerDigitos(cnpj)
    cnpj = formatarCNPJ(calculaSegundoDigito(calcularPrimeiroDigito(cnpj)))
    return cnpj


# Usando expressão regular para remover a ponutação do CNPJ e deixar somente números
def removerCaracteresEspeciais(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


# Remover os últimos 2 dígitos do CNPJ para realizar os cálculos
def removerDigitos(cnpj):
    return cnpj[:-2]


# Calculando o primeiro dígito
def calcularPrimeiroDigito(validacao1):
    # Nesta váriável armazenarei a soma
    resultado = 0
    # Esta usarei para armazenar o numero que devo multiplicar
    calculo = 5
    # Calculando primeira parte do bloco CNPJ (5432)
    for numero in validacao1:
        resultado += calculo * int(numero)
        calculo -= 1
        if calculo == 1:
            calculo = 9
            break

    # Usarei este indice para calcular do 4 digito em diante do CNPJ
    indice = 4
    # Calculando segunda parte do bloco CNPJ (98765432)
    while validacao1:
        # Aqui vou somando ao resultado do primeiro bloco os valores que vou calculando do segundo bloco
        resultado += calculo * int(validacao1[indice])
        # Acrescento um para percorrer a string
        indice += 1
        # Reduzo o cálculo para bater com a validação
        calculo -= 1
        # Quando cálculo chegar a 1, encerro a conta
        if calculo == 1:
            break

    # Calculando o primeiro dígito do CNPJ
    resultado = 11 - (resultado % 11)

    # SE o resultado for MAIOR que 9, converte para 0 o dígito, senão concatena com o CNPJ
    if resultado >= 10:
        resultado = 0
        validacao1 += str(resultado)
    else:
        validacao1 += str(resultado)

    return validacao1


def calculaSegundoDigito(validacao2):
    # Nesta váriável armazenarei a soma
    resultado = 0
    # Esta usarei para armazenar o numero que devo multiplicar
    calculo = 6
    # Calculando primeira parte do bloco CNPJ (65432)
    for numero in validacao2:
        resultado += calculo * int(numero)
        calculo -= 1
        if calculo == 1:
            calculo = 9
            break

    # Usarei este indice para calcular do 5 digito em diante do CNPJ
    indice = 5
    # Calculando segunda parte do bloco CNPJ (98765432)
    while validacao2:
        # Aqui vou somando ao resultado do primeiro bloco os valores que vou calculando do segundo bloco
        resultado += calculo * int(validacao2[indice])
        # Acrescento um para percorrer a string
        indice += 1
        # Reduzo o cálculo para bater com a validação
        calculo -= 1
        # Quando cálculo chegar a 1, encerro a conta
        if calculo == 1:
            break

    # Calculando o primeiro dígito do CNPJ
    resultado = 11 - (resultado % 11)

    # SE o resultado for MAIOR que 9, converte para 0 o dígito, senão concatena com o CNPJ
    if resultado >= 10:
        resultado = 0
        validacao2 += str(resultado)
    else:
        validacao2 += str(resultado)

    return validacao2


def formatarCNPJ(cnpj):
    return "%s.%s.%s/%s-%s" % (cnpj[0:2], cnpj[2:5], cnpj[5:8], cnpj[8:12], cnpj[12:14])


