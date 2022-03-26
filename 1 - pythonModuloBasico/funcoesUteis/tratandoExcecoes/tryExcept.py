"""
Tratamento de exceções com Try ... Except
"""

# Erro de NameError (Variável não declarada)
try:
    # a não declarado, irá dar erro
    print(a)
# except para casos de variável não declarada
except NameError as erro:
    print("Erro de declaração de variável", erro)


# Para qualquer exceção sem especificar pode usar o Exception, por exemplo:
try:
    # Criando um erro de indice propositalmente
    a = []
    print(a[1])
# Este Exception olha para todo e qualquer tipo de erro que pare o programa
except Exception as erro:
    print("Qualquer tipo de erro: ", erro)


try:
    # Criando um erro de indice propositalmente
    a = []
    print(a[1])
# Tratando o erro de indice
except IndexError as erro:
    print("Erro de indice: ", erro)

try:
    # Criando um erro de dicionario propositalmente
    a = {}
    print(a)
# Tratando o erro de indice
except (IndexError, KeyError) as erro:
    print("Erro de dicionário: ", erro)

else:
    print('Sempre executa se der certo, sem nenhum erro!')
    print(a)
finally:
    print('Este aqui sempre executa, independente do resultado do código')