"""
Funções em python (Parte 1)
"""


def saudacao(msg='Olá', nome='Usuário!'): # Definindo uma mensagem padrão em casos que os parâmetros não são recebidos
    print(msg, nome)


saudacao() # Utilizando o padrão definido quando criei a função
saudacao(nome='Zezinho!') # Quando temos padrão podemos definir somente um dos parâmetros
saudacao('Olá', 'Daniel!')
saudacao('Oi', 'Daniel!')
saudacao('Hello', 'João!')
saudacao('Olá', 'Maria!')
