from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    # Getters
    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    # Setter
    @saldo.setter
    def saldo(self, saldo):
        if not isinstance(saldo, (int, float)):
            raise ValueError('Valor precisa ser númerico!')
        self._saldo = saldo

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor do depósito precisa ser númerico!')
        self.saldo += valor
        self.detalhesConta()

    # Método abstrato que não utilizarei aqui, pois cada conta tem as suas especificações de saque, aqui estou
    # dizendo que todas precisam ter sua função
    @abstractmethod
    def sacar(self, valor):
        pass

    def detalhesConta(self):
        print(f'Agência: {self.agencia}', end=' ')
        print(f'Conta: {self.conta}', end=' ')
        print(f'Saldo: {self.saldo}')