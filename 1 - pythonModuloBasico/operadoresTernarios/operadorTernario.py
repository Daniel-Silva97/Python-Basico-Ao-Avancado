"""
Operador Ternário
"""

#  Exemplo 1
logged_user = False

# MSG = Se logged_user == True msg1 senão msg2
msg = 'Usuário logado!' if logged_user else 'Usuário precisa logar.'

print(msg)

#  Exemplo 2
idade = input("Qual sua idade: ")
if not idade.isnumeric():
    print('Você precisa digitar números!')
else:
    idade = int(idade)
    maior_de_idade = (idade >= 18)
    msg = 'Pode Acessar!' if maior_de_idade else 'Não pode acessar'
    print(msg)
