"""
Operadores relacionais

* == - Perguntando se um valor é igual a outro
* >  - Perguntando se um valor é maior que outro
* >= - Perguntando se um valor é maior/igual a outro
* <  - Perguntando se um valor é menor a outro
* <= - Perguntando se um valor é menor/igual a outro
* != - Perguntando se um valor é diferente de outro

O resultado das perguntas acima sempre será booleana, True or False

"""


#  Checar se pode pegar um empréstimo

name = input("Qual é o seu nome? ")
age = int(input("Qual a sua idade? "))

#  Limite para pegar o empréstimo
age_min = 18
age_max = 30

print()
if age>=age_min and age<=age_max:
    print(f'{name} pode pegar o empréstimo!')
elif age<age_min:
    print(f'{name} não tem idade miníma para solicitar o empréstimo!')
elif age>age_max:
    print(f'{name} ultrapassou a idade máxima para solicitar o empréstimo!')
else:
    print(f'{name} NÃO pode pegar o empréstimo!')