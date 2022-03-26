# https://rszalski.github.io/magicmethods/

class A:
    # Primeiro método chamado quando instanciamos a classe
    # def __new__(cls, *args, **kwargs):
    #     print('Eu sou o NEW')

    #  SINGLETON
    # if not hasattr(cls, '_jaexiste'):
    #     cls._jaexiste = super().__new__(cls)
    #
    # return cls._jaexiste

    # Assim que instancio a classe o init é chamado, aqui que crio os meus atributos
    # Antes da __init__ é chamado o __new__
    def __init__(self):
        print('Eu sou INIT')

    # Com o método call conseguimos fazer que a nossa classe possa ser chamada como função, o resto da classe não deixa
    # de funcionar
    def __call__(self, *args, **kwargs):
        return f'Argumentos enviados: {args} {kwargs}'

    # Posso alterar como a função len() se comporta se preciso retornar o tamanho da minha classe com um calculo
    # específico
    def __len__(self):
        return 55

    # Aqui é o retorno que o python traz quando tentamos printar uma instancia, podemos mudar o padrão.
    def __str__(self):
        return f'O que quero exibir quando essa classe se transformar em uma str'

    # Método que o Garbage Collector usa para coletar os objetos da memória
    def __del__(self):
        print('Objeto coletado.')

    # Toda a vez que configurarmos um atributo novo este método é chamado
    def __setattr__(self, key, value):
        self.__dict__[key] = f'{value} adicionei isso no seu valor'


# Instancia 1
a = A()
# Instância 2
b = A()
# Se eu estiver com o hasattr() descomentado, estas 2 instâncias ocuparão o mesmo endereço na memória.

# Chamando a classe como se fosse função (__call__)
variavel = a(1, 2)
print(variavel)
# Conferindo o hasattr()
print(a == b)
# Testando o método __str__
print(a)
# Testando a alteração do __len__
print(len(a))
