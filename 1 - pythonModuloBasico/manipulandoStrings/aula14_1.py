"""
Manipulando Strings

* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs type, print, etc ..

Essas Funções podem ser usadas diretamente em cada tipo.

"""
#  Positivos   [01234568]
texto = 'Python S2'
#  Negativos  [-987654321]
#  Acessando uma letra da variável por meio dos indices
print(texto[1])

#  Removendo a barra na hora de mostrar em tela
url = 'https://google.com.br/'
#  Fatiamento de Stings utiliza ':' para dizer onde quero que comece
#  e onde quero que termine, por exemplo:
#  Pegar do indice 1 : 6 Até o indice 5 (o ultimo é sempre -1)
#  Removendo a barra e pegando o resto desde o início
print(url[:-1])

novaString = texto[2:6]  # Fatiamento pegando do indice 3 ao 5

print(novaString)

#  Pegando do caractere 0 e pulando de 2 em 2 casas até o caracatere 6
#  Exiba em tela
print(texto[0:6:2])
