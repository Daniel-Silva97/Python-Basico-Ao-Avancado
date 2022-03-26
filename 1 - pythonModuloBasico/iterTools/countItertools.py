"""
Count - Itertools

Contador automático do python
"""

from itertools import count

# Count() não tem fim, gera um contador infinito
contador = count()


# Loop infinito
for valor in contador:
    print(valor)

    # Para parar o laço infinito
    if valor >= 10:
        break


# Criando um contador que comece a partir de algum número
contadorComNumeroInicial = count(start=5)

# Loop infinito
for valor in contadorComNumeroInicial:
    print(valor)

    # Para parar o laço infinito
    if valor >= 10:
        break

# Criando contador que pule numeros, por exemplo de 2 em 2,
# funciona com float também e número negativo
contadorPulaSequencial = count(step=2)

# Loop infinito
for valor in contadorPulaSequencial:
    print(valor)

    # Para parar o laço infinito
    if valor > 10:
        break

