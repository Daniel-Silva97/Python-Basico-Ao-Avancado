"""
Classes Abstratas

São classes que não quero que seja instanciadas no código
"""
# Importando os métodos que utilizamos para criar classes Abstratas (ABC, abstractmethod)
from abc import ABC, abstractmethod


# Herdando ABC para informar que a classe é abstrata
class A(ABC):
    # Dizendo que o método é abstrato e não pode ser instanciado
    @abstractmethod
    def falar(self):
        pass


class B:
    @staticmethod
    def falar():
        print('B está falando...')

    pass


# ERRO, Não se pode instaciar classes ou métodos abstratos
# a = A()
# a.falar()

b = B()
b.falar()
