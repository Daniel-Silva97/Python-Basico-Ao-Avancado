"""
Polimorfismo é o princípio que permite que classes derivadas de uma mesma
superclasse tenham métodos iguais (de mesma assinatura) mas comportamentos
diferentes.

Mesma assinatura = Mesma quantidade e tipo de parâmetros.
"""

from abc import ABC, abstractmethod


# Superclasse abstrata
class A(ABC):
    # Método abstrato que me forçara criar nas subclasses a operação de acordo com a situação
    @abstractmethod
    def fala(self, msg):
        pass


# Subclasse 1
class B(A):
    # Criando o método obrigatório aqui e passando a situação 1 (Polimorfismo)
    def fala(self, msg):
        print(f'B está falando de {msg}')


# Subclasse 2
class C(A):
    # Criando o método obrigatório aqui e passando a situação 2 (Polimorfismo)
    def fala(self, msg):
        print(f'C está falando de {msg}')


b = B()
c = C()

b.fala('Futebol')
c.fala('Polimorfismo')
