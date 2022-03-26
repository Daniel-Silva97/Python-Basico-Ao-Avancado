from classes import *

cliente1 = Cliente('Daniel', 25)
print(cliente1.nome)
# Aqui consigo visualizar qual classe está chamando a função falar na SuperClasse (Pessoa)
cliente1.falar()
cliente1.comprar()

aluno1 = Aluno('Maria', 24)
print(aluno1.nome)
# Aqui consigo visualizar qual classe está chamando a função falar na SuperClasse (Pessoa)
aluno1.falar()
aluno1.estudar()
