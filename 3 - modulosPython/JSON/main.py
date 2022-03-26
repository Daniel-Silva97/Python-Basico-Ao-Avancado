"""
JavaScript Object Notatio - JSON

JSON (JavaScript Object Notation) é um formato de troca de dados entre
sistemas e programas muito leve e de fácil utilização. Muito utilizado
em API's

DUMPS / Dump
Convertendo tipo de dados de Python para JSON
######################
Python          JSON
dict	        object
list, tuple	    array
str	            string
int, float  	number
True        	true
FALSE	        False
None	        null

LOADS / Load
Convertendo tipo de dados de JSON para Python
######################
JSON	        Python
object	        dict
array	        list
string	        str
number (int)	int
number (real)	float
true	        True
false	        False
null	        None

"""

from dados import *
import json


# Convertendo dicionário para JSON
dadosEmJSON = json.dumps(clientes_dicionario, indent=4)
# print(dadosEmJSON)


# Convertendo JSON em dicionário
dadosEmDicionario = json.loads(clientes_json)
# for chave, valor in dadosEmDicionario.items():
#     print(chave)
#     print(valor)

# Pegou o dicionario, criou um arquivo .json e converteu o dicionario em JSON
with open('clientes.json', 'w') as arquivo:
    json.dump(clientes_dicionario, arquivo, indent=4)

# Pegou o arquivo, leu as informações e converteu o JSON em dicionario, salvando em uma variável
with open('clientes.json', 'r') as arquivo:
    dados = json.load(arquivo)

# for chave, valor in dados.items():
#     print(chave)
#     print(valor)