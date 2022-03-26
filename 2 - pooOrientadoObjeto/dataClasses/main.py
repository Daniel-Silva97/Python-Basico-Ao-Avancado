"""
O que são dataclasses? O módulo Dataclasses fornece um decorador e funções
para criar automaticamente métodos, como __init__(), __repr__(), __eq__ (etc)
em classes definidas pelo usuário.
Basicamente, dataclasses são syntax sugar para criar classes normais.
Foi originalmente descrito na PEP 557.
Adicionado na versão 3.7 do Python.
Leia a documentação: https://docs.python.org/pt-br/3/library/dataclasses.html
"""

from dataclasses import dataclass
from dataclasses import field
from dataclasses import asdict, astuple


# Podemos passar parâmetro no decorador para informar quais métodos não deseje que ele
# crie automaticamente, no exemplo abaixo não quero que ele manipule o método __eq__
@dataclass(eq=False, repr=True, frozen=False, init=True, order=False)
# eq - Método para checar se são iguais
# repr - Método para mudar como exibe no print() por exemplo quando quero ver a instância
# frozen - Torna a classe imutável quando igual a True, não consigo modificar nada nela
# init - incializador, já faz automaticamente quando True
# order - permitir ordenar as instâncias com sort() por exemplo,
class Pessoa:
    # Dataclass já cria o init automaticamente, se quiser somente declarar os atributos novos não preciso do __init__
    nome: str
    sobrenome: str = field(repr=False)  # Usando o field para não apresentar quando o repr for chamado


p1 = Pessoa('Daniel', 'Silva')
p2 = Pessoa('Daniel', 'Silva')
print(p1 == p2)  # Aqui como informei que não quero que o dataclass manipule o __eq__, retornará false
print(p1)  # Aqui podemos ver o método __repr__ manipulado pela dataclass
print(p1.nome)
print(p1.sobrenome)
print(asdict(p1))  # Convertendo a classe em Dicionário
print(astuple(p1))  # Convertendo a classe em Tupla
