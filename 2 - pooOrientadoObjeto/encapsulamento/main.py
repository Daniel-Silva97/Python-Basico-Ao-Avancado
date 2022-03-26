"""
public, private, protected

No Pyhton não existe o mesmo conceito de encapsulamento criado em Java por exemplo
Por convenção, se não queremos que um atributo ou  método, seja modificado fora da Classe
usamos o '_' (underline) como base.

no exemplo abaixo criamos o dicionário 'dados' e como ele é a base dos métodos a seguir, não quero que o tipo dele
seja alterado por exemplo, de dicionário para String

para isso acrescento o '_'(underline) antes do nome do atributo, ficando:
_dado = Consigo acessar, mas o pycharm deixa de recomendar para alteração enquanto o programador coda.
__dado = Fortemente recomendado que não altere, neste caso o Python não altera o atributo da classe, mas renomeia e
e instacia um novo para casos que haja alteração
"""


class BaseDeDados:
    def __init__(self):
        # Utilizando "__" para dizer que recomendo não alterar/acessar este item fora da classe
        self.__dados = {}

    def inserirCliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def listaClientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apagaCliente(self, id):
        del self.__dados['clientes'][id]

    # Se eu quiser somente exibir os dados fora da classe, posso criar um Getter para isso
    @property
    def dados(self):
        return self.__dados


bd = BaseDeDados()

bd.inserirCliente(1, 'Otávio')
bd.inserirCliente(2, 'Miranda')
bd.inserirCliente(3, 'Rose')

bd.apagaCliente(3)

bd.listaClientes()

# Usando o Getter para acessar os valores
# Sem o setter não posso alterar o atributo dados
print(bd.dados)
