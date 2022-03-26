# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma
# lista

numeros = (2, 10, 13, 26)
lista = []


for controle in numeros:
    calculo = controle * 2
    lista.append(calculo)
    print(lista)

for teste in range(100, 151):
    if teste % 2 == 0:
        print(teste)
  