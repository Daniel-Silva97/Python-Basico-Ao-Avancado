"""
Herança Múltipla
"""


# SuperClasse
class A:
    def falar(self):
        print('Falando... Estou em A')


# Subclasse que herda de A, sem relacionamento com C e D
class B(A):
    def falar(self):
        print('Falando... Estou em B')


# SubClasse que herda de A, sem relacionamento com B e D
class C(A):
    def falar(self):
        print('Falando... Estou em C')


# Herança múltipla, SubClasse que herda de B e C, que herdam de A
"""
Nesta classe, se eu chamar a função falar(), ela existe na classe B e C.

O Python trata da seguinte forma, define a prioridade de acordo com o informado no parênteses da esquerda pra direita.
então:
class D(B, C)

Se existir função nas duas, ele usará a de B neste caso.
"""


class D(B, C):
    pass


