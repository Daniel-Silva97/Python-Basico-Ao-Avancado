from datetime import datetime
from random import randint

# Por convenção utiliza PascalCase no nome da classe
class Pessoa:
    # Variável da classe
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    # Método em classes é simplesmente uma função dentro da classe:
    def __init__(self, nome, idade, comendo=False, falando=False):
        # Variáveis da instância
        # self utilizamos para que possamos acessar essas variáveis de qualquer método dentro da classe, com
        # ele posso criar vários métodos e acessar normalmente pois estará no escopo da classe
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.falando:
            print(f'{self.nome} está falando e não pode comer!')
            return

        # acessando as variáveis com Self em outro método
        if self.comendo:
            print(f'{self.nome} está comendo!')
            return

        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def pararComer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo!')
            return

        print(f'{self.nome} parou de comer!')
        self.comendo = False

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} está comendo e não falando!')
            return
        if self.falando:
            print(f'{self.nome} já está falando!')
            return

        print(f'{self.nome} está falando de {assunto}!')
        self.falando = True

    def pararFalar(self):
        if not self.falando:
            print(f'{self.nome} não está falando!')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def anoDeNascimento(self):
        return f'{self.nome} nasceu em {self.ano_atual - self.idade}'

    # Método de classe é ligado somente a classe e não a instância,
    # utilizamos o @classmethod para dizer quando é um método de classe
    # e por convenção, ao invés de self utilizamos cls
    @classmethod
    def criarPorAnoNascimento(cls, nome, ano):
        idade = cls.ano_atual - ano
        return cls(nome, idade)

    # staticmethod, basiscamente é uma função que não precisaria estar na classe, mas para organização de código é
    # passada dentro da classe, não passamos parâmetros nela se quisermos.
    @staticmethod
    def gerarId():
        rand = randint(10000, 19999)
        return rand

