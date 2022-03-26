"""
Iterando strings com While

*   Índices
*   0123456789.......................33
"""
#INDICE [0123456789......................33]
frase = "o rato roeu a roupa do rei de roma"
tamanhoFrase = len(frase)
contador = 0
nova_string = ''
#  Exibindo a letra que está no Indice usando o contador como base
# while contador <= tamanhoFrase:
#     print(frase[contador], contador)
#     contador += 1

#  Atribuindo a uma nova variável a frase armazenada uma letra por vez
while contador < tamanhoFrase:
    nova_string += frase[contador]
    print(nova_string)  # Vendo o que acontece a cada loop
    contador += 1
print(nova_string)
