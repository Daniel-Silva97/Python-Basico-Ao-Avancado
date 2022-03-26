"""
Composição de classes
uma classe PERTENCE a outra
Neste caso se a classe "Pai" for deletada, todos os objetos criados a partir dela serão deletados juntos
"""


class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        # Usando a classe endereço para COMPOR o nome / idade que inclui
        self.enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    # Mostrando que quando o cliente é removido da memória, os seus endereços são apagados juntos
    def __del__(self):
        print(f'{self.nome} FOI APAGADO!')


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    # Exibindo os endereços sendo deletados
    def __del__(self):
        print(f'{self.cidade} / {self.estado} FOI APAGADO!')
