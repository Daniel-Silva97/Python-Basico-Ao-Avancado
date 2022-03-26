"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudação e nome.
"""


def saudacao(saudacao='Olá', nome='Usuário'):
    print(saudacao, nome)


print('Exercício 1')
saudacao()
saudacao('Olá', 'Daniel!')
print()

"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.
"""


def soma(n1, n2, n3):
    print(n1 + n2 + n3)


print('Exercício 2')
soma(1, 2, 3)
print()

"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual
(ex. 10%). Retorne (return) o valor do primeiro número somado do aumento do percentual do mesmo.
"""


def calcula(n1, perc1):
    perc1 = perc1 / 100
    resultado = n1 + (n1 * perc1)
    return resultado


exercicio3 = calcula(50, 5)
print('Exercício 3')
print(exercicio3)
print()

"""
Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz.
Se o parâmetro da função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário
retorne o número enviado.
"""


def exercicio(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return 'FizzBuzz'
    if numero % 3 == 0:
        return 'fizz'
    if numero % 5 == 0:
        return 'buzz'

    return numero


print('Exercício 4')
print(exercicio(7))
