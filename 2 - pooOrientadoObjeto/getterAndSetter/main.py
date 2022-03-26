"""
GETTER = Obter um valor
SETTER = Configurar um valor (=)
"""


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def descontoPercentual(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter
    @property
    def nome(self):
        return self._nome

    @property
    def preco(self):
        # Por convenção, para não por o mesmo nome da variável criada na classe, colocamos um '_' (underline) antes do
        # nome da variável
        return self._preco

    # Setter
    @nome.setter
    def nome(self, dado):
        # Deixando somente a primeira letra maiúscula
        self._nome = dado.title()

    # Criar o decorador com nomeVariavel.setter, sempre por padrão usar o nome da variável que o setter será responsável
    @preco.setter
    # Recebendo além do self, o valor que vou tratar do preço
    def preco(self, valor):
        # Dentro do setter, posso realizar o tratamento de dados.
        # Convertendo string para número
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        # Uso a variável do getter para tratar
        self._preco = valor


p1 = Produto('CAMISETA', 50)
p1.descontoPercentual(10)
print(p1.nome, p1.preco)

p2 = Produto('CANECA', 'R$10')
p2.descontoPercentual(10)
print(p2.nome, p2.preco)
