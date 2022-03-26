"""
Tipos de dados

str - String - textos "Assim" 'Assim'
int - inteiro - Números 10 - 20 - 30
float - real/ponto flutuante Números com ponto - 10.6 - 20.4 - 343.23
bool  - booleano/lógico - true or false

"""

#  Para saber o tipo do dado usar a função type()

print('Luiz', type('Luiz'))
print(10, type(10))
print(10.5, type(10.5))
print(10 == 14, type(10 == 14))

#  Convertendo os tipos em python

print('luiz', type('luiz'), bool('luiz'))

#  Exercício

#  String (Nome)
print('Daniel da silva Pedro', type('Daniel da silva Pedro'))

#  Int (Idade)
print(25, type(25))

#  Float (Altura)
print(1.75, type(1.75))

#  Bool Comparar se é maior de 18 anos
print(25 > 18, type(25 > 18))
