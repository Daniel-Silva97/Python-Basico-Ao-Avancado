"""
Quebrar a string abaixo em uma lista com grupos de 0123456789
"""

string = '0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'


# Criando os indices iniciais e finais da string
n = 10  # Indice final
# List comprehension para pegar os ranges da string que separam o elemento 0123456789 conforme exemplo abaixo
comp = [(i, i+n) for i in range(0, len(string), n)]
print(comp)

"""
Indices
0123456789  0123456789  0123456789  0123456789  0123456789  0123456789  0123456789  0123456789  0123456789  0123456789
0 a 10      10 a 20     20 a 30     30 a 40     40 a 50     50 a 60     60 a 70     70 a 80     80 a 90     90 a 100
"""

# Para montar os grupos de 0123456789 basta modificar um pouco a variável que criamos acima
lista = [string[i:i+n] for i in range(0, len(string), n)]
print(lista)
()
"""
Ao invés de tupla, troco para indice inicial/final da string para fatiamento dos grupos
"""
retorno = '.'.join(lista)
print(retorno)
