"""
Herança

Quando 2 ou mais classes utilizam os mesmos atributos para as suas operações, podemos usar
a herança para criar uma classe principal, e classes que herdam tudo que foi criado nessa classe.

Por exemplo:

Alunos e clientes terão atributos nome e idade em ambas
para evitar duplicidade podemos criar a class pessoa com esses atributos e usar
herança para incluir em Cliente e Aluno.
"""


# Classe Pessoa com todos os atributos (Denominada "SuperClasse")
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        # Para saber o nome da classe
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} está falando...')


# Para Herdar da classe Pessoa, basta incluir entre parênteses a classe principal conforme abaixo
# Denominada "SubClasse"
class Cliente(Pessoa):
    # Criando Funções que só podem ser utilizadas dentro da classe Cliente
    def comprar(self):
        print(f'{self.nomeclasse} está comprando...')


# Denominada "SubClasse"
class Aluno(Pessoa):
    # Criando Funções que só podem ser utilizadas dentro da classe Aluno
    def estudar(self):
        print(f'{self.nomeclasse} está estudando...')


"""
No caso acima a herança funciona assim:

Cliente e Aluno herdam tudo da classe pessoa mas também tem suas especificações como as funções 
comprar() e estudar().

Já a classe Pessoa não herda nada das classes Cliente e Aluno, mas também funciona 
indenpendentemente com suas funções.
"""