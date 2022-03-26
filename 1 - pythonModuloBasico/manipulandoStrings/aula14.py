"""
Formatando valores com modificadores (metódos format e F strings)

:s - Texto (strings)
:d - Inteiros (int)
:f - Número de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d, f)

> - Esquerda
< - Direita
^ - Centro
"""


num1 = 10
#  num2 = 3

#  divisao = num1 / num2

#  Colocando o resultado com 2 casas decimais
#  Usando método format
# print( '{:.2f}'.format(divisao))

#  Usando F strings
#  print(f'{divisao:.2f}')



#  Usando o último exemplo da descrição onde posso definir a
#  quantidade de casas que quero a esquerda, direita ou centro

print(f'{num1:0<10}') #  Adicionando casas à direita do num1
print(f'{num1:0>10}') #  Adicionando casas à esquerda do num1
print(f'{num1:0^10}') #  Colocando num1 no centro de n zeros


name = 'Daniel Silva'

print(f'{name:#^40}')

nomeFormatado = '{:@>50}'.format(name)

print(nomeFormatado)