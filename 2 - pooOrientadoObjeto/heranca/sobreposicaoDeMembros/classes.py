"""
Sobreposição de membros
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


# Exemplo de Sobreposição
# Esta subclasse herda tudo da classe Cliente que posteriormente herda tudo da classe Pessoa
# Portanto, ela consegue utilizar tudo que houver nas 3 classes
class ClienteVIP(Cliente):

    # Utilizando o construtor da classe Pessoa, mas acrescentando novos atributos
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    # Suponhamos que quero usar a função falar, mas não no formato apresentado na classe Pessoa
    # Podemos usar a "Sobreposição" que é criar dentro da classe o formato que desejo que seja utilizado para essa
    # classe em específico.
    def falar(self):
        # Quando quero que ainda assim, o código da SuperClasse seja executada, posso usar o comando super().function()
        # para chamar ela dentro da função, neste caso ela perguntaria o passo 2, como em Cliente não tem, busca na
        # classe Pessoa
        super().falar()

        # Chamando a função usando o nome da Classe diretamente
        Pessoa.falar(self)
        print(f'{self.nome} {self.sobrenome}')


"""
No formato acima, quando a função falar() for chamada, o python irá buscar na seguinte ordem pela função:

    1 - Existe a função falar() na classe ClienteVIP? 
        "Sim" - Utilizo ela
        "Não" - Próximo passo
    
    2 - Existe a função falar() na classe Cliente? 
        "Sim" - Utilizo ela
        "Não" - Próximo passo     
    
    3 - Existe a função falar() na classe Pessoa? 
        "Sim" - Utilizo ela


No caso acima EXISTE na classe ClienteVIP, então ela sobrepõe a função da classe Pessoa e é executada.        
"""
