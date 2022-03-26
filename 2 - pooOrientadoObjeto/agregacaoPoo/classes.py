"""
Agregação é quando uma classe é inclusa em uma Segunda classe e essa classe precisa
dela para funcionar
"""


# Nesta Classe temos um caso de agregação, na qual ela pode existir sem a Classe Produtos, mas toda sua lógica depende
# dela, então aqui temos classes agregadas
class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
