from contaCorrente import ContaCorrente
from contaPoupanca import ContaPoupanca


print("Conta Poupança")
contaPoupanca = ContaPoupanca(1111, 2222, 0)
contaPoupanca.detalhesConta()
contaPoupanca.depositar(10)
contaPoupanca.sacar(5)
contaPoupanca.sacar(5)
contaPoupanca.sacar(1)

print()

print("Conta corrente")

contaCorrente = ContaCorrente(agencia=1234, conta=5678, saldo=0, limite=100)
contaCorrente.depositar(100)
contaCorrente.sacar(250)
contaCorrente.sacar(500)
contaCorrente.depositar(1000)
