"""
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra - OK
    Contas têm agência, número da conta e saldo -OK
    Contas devem ter método para depósito - OK
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar) - OK
"""
from abc import abstractmethod


# SuperClasse que inicializa os dados Agencia, Conta e Saldo
class Conta:
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    # Função depositar para incluir saldo na conta do cliente
    def depositar(self, valor):
        self.saldo += valor
        # Aqui mostra os dados da conta após o deposito
        self.detalhes()

    # Função para apresentar os detalhes da conta
    def detalhes(self):
        print(f'Agencia: {self.agencia}\n'
              f'Conta: {self.conta}\n'
              f'Saldo: {self.saldo}\n')

    # Polimorfismo para definir o que este método fará em outras classes (ContaCorrente e ContaPoupanca)
    @abstractmethod
    def sacar(self, valor): pass


# Classe de Conta Corrente que herda de Conta
class ContaCorrente(Conta):
    # Criando atributo limite para incluir no método sacar
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    # Método para saque que veio da SuperClasse
    def sacar(self, valor):
        # Saque incluindo o limite para validação
        if valor < (self.saldo + self.limite):
            self.saldo -= valor
            self.detalhes()
        else:
            print(f'Saldo Insuficiente')
            self.detalhes()


# Conta Poupança herdando de Conta
class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor < self.saldo:
            self.saldo -= valor
            self.detalhes()
        else:
            print(f'Saldo Insuficiente')
            self.detalhes()
