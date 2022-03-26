"""
str - String
"""
"""
Quando for utilizar '   ' no texto abrir a string com "" para não confundir o interpretador do python sobre
onde abre e onde encerra o campo texto, por exemplo:
"""
print("Essa é uma 'string' (str).")

"""
O Mesmo vale para " ", iniciar com ' ' o texto para não confundir o interpretador
"""
print('Essa é uma "string" (str).')

"""
Se ainda assim deseja usar "" para abrir o campo string e também usar na frase, colocar o caractere ( \ ) faz com que
o python ignore o próximo caractere, por exemplo:
"""
print("Essa é uma \"string\" (str).")

#  OU

print('Essa é uma \'string\' (str).')

"""
Para dizer ao Python que o que está dentro da string não deve ser executado,
Mesmo que um comando válido, iniciar a String com um 'r'(raw) antes, por exemplo
"""

# Mesmo com o comando de quebra de linha (\n) ele foi exibido como texto por causa do r (raw)
print(r"Este é um texto \n (str).")
