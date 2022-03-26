class Escritor:
    # Criando o inicializador (Construtor)
    def __init__(self, nome):
        # Criando um atributo nome privado
        self.__nome = nome
        self.__ferramenta = None

    # Criando um getter para nome
    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta


class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    @staticmethod
    def escrever():
        print('Caneta está escrevendo')


class MaquinaDeEscrever:
    @staticmethod
    def escrever():
        print('Máquina está escrevendo')
