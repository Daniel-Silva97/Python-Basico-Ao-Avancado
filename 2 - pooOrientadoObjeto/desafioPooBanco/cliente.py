"""
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
"""


# Classe Pessoa inicializando os dados principais do Cliente (Nome , Idade)
class Pessoa:
    def __init__(self, _name, _idade):
        self._nome = _name
        self._idade = _idade

    # Getters
    @property
    def pessoa(self):
        return self._nome

    def idade(self):
        return self._idade


# Classe para inicializar o cliente e também vincular a conta com a função inserir_conta
class Cliente(Pessoa):
    def __init__(self, _nome, _idade):
        # Chamando nome e idade da SuperClasse
        super().__init__(_nome, _idade)
        self.conta = None

    def inserir_conta(self, conta):
        self.conta = conta


