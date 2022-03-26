from classes import Cliente, Endereco

cliente1 = Cliente('Daniel', 25)
cliente1.insere_endereco("Jundiaí", "SP")
cliente1.insere_endereco("Fortaleza", "CE")
print(cliente1.nome)
cliente1.lista_enderecos()
print()

cliente2 = Cliente('Maria', 25)
cliente2.insere_endereco("São Paulo", "SP")
cliente2.insere_endereco("Salvador", "BA")
print(cliente2.nome)
cliente2.lista_enderecos()
print()

cliente3 = Cliente('Maria', 25)
cliente3.insere_endereco("Paraty", "RJ")
cliente3.insere_endereco("Porto Alegre", "RS")
print(cliente3.nome)
cliente3.lista_enderecos()
print()

print('################# FIM DO CODIGO ###################')

"""
Após finalizar o código, aqui a memória está sendo limpa excluíndo os objetos criados, portanto ao limpar os clientes 
os endereços serão excluídos juntos

usando a função __del no arquivo classes para exibir isto

Garbage Collector do Python faz o trabalho de apagar
"""