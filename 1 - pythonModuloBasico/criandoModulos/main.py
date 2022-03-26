# Importando um módulo dentro do pacote2 vendas que criei
# import vendas.calculaPrecos

# Outras 2 formas de importar
# from vendas import calculaPrecos
from vendas.calculaPrecos import aumento, reducao

preco = 49.90
# Chamando a função que criei sem formatar em R$
precoComAumento = aumento(preco, 10)
# Chamando a função formatando em R$
precoComAumentoFormatado = aumento(preco, 10, True)
# Chamando a função que criei sem formatar em R$
precoComReducao = reducao(preco, 20)
# Chamando a função formatando em R$
precoComReducaoFormatado = reducao(preco, 20, True)

print(preco)
print(precoComAumento)
print(precoComAumentoFormatado)
print(precoComReducao)
print(precoComReducaoFormatado)
