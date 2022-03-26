#  Entrada de dados

name = input("Qual é o seu nome? ")
age = input("Qual é a sua idade? ")
birth_year = 2022 - int(age)
print()
print(f'{name} tem {age} anos.\n'
      f'{name} nasceu em {birth_year}.')
