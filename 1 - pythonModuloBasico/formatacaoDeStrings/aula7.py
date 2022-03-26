"""
Formatação de Strings usando f Strings
"""


nome = 'Daniel da silva pedro'
idade = 25
altura = 1.75
e_maior = idade > 18
peso = 86
imc = peso / altura ** 2  # Cálculo


# Exercicio: Calcular IMC e exibir no print abaixo (Sem f strings)
print(nome, 'tem', idade, 'anos de idade e seu imc é de', imc)

#  Agora usando o a formatação de strings
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}')

#  Outro exemplo de format
print('{} tem {} anos de idade e seu IMC é {:.2f}'.format(nome, idade, imc))

#  Outra opção do format é:
print('{0}{2} tem {1}{0} anos de idade e seu IMC é {2}{1}'.format(nome, idade, imc))

"""
0, 1 e 2 representam a varíavel que coloquei no format, então nome será 0, idade será 1 e imc será 2, definindo os
numeros dessa forma posso colocar o conteúdo da variável em qualquer lugar no texto
"""

#  Podemos nomear as variáveis no format também, por exemplo
print('{n}{i} tem {im}{i} anos de idade e seu IMC é {im}{n}'.format(n=nome, i=idade, im=imc))
