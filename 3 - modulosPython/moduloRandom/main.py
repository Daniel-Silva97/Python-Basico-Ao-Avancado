import random


# Gera um número inteiro entre A e B
import string

inteiro = random.randint(10, 20)
print(inteiro)

# Gera um número aleatório usando a função range()
inteiro2 = random.randrange(900, 1000, 10)
print(inteiro2)

# Gera um número de ponto flutuante entre A e B
pontoFlutuante = random.uniform(10, 20)
print(pontoFlutuante)

# Gera um número de ponto flutuante entre 0 e 1
pontoFlutuante2 = random.random()
print(pontoFlutuante2)

nomes = ['Luiz', 'Daniel', 'Maria', 'Rose', 'Jenny', 'Felipe']
# Choice pega um valor aleatório da lista
sorteio = random.choice(nomes)
print(sorteio)
# Pega 2 ou mais valores da lista podendo repetir as vezes
sorteio2 = random.choices(nomes, k=2)
print(sorteio2)

# Pega 2 ou mais valores da lista sem repetir
sorteio3 = random.sample(nomes, 2)
print(sorteio3)

# Para embaralhar uma lista aleatóriamente
random.shuffle(nomes)
print(nomes)

# Gerando senha aleatória
letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%¨&*()'
geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=20))
print(senha)

