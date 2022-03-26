from classes import Escritor, Caneta, MaquinaDeEscrever

# Atribuindo um nome ao Escritor
escritor = Escritor('Joãozinho')
print(escritor.nome)
# Atribuindo uma marca a caneta
caneta = Caneta('Bic')
print(caneta.marca)
# Chamando a classe MaquinaDeEscrever
maquina = MaquinaDeEscrever()
maquina.escrever()


# Conectando as classes através do atributo ferramenta na classe Escritor
# Associando ao escritor por meio do atributo ferramenta toda a classe caneta, que criei com váriável 'caneta'
escritor.ferramenta = caneta
escritor.ferramenta.escrever()

# Com a associação acima, mesmo que posteriormente eu excluísse a classe Escritor, eu poderia utilizar
# as Classes Caneta e Maquina de escrever sem problemas posteriormente
