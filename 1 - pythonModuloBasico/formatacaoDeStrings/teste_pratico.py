"""
* Criar váriáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* Criar uma váriável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

from datetime import date

name = input("Digite seu nome:")
age = int(input("Digite sua idade:"))
height = float(input("Digite sua altura:"))
weight = float(input("Digite seu peso:"))
current_year = date.today().year
birth_year = current_year - age
imc = weight / height ** 2

print(f'Olá {name},')
print(f'Seu ano de nascimento é {birth_year}, portanto agora em {current_year} você completará {age} anos de idade')
print(f'Com altura de {height} e peso {weight} kg, seu IMC é de {imc:.2f}')
