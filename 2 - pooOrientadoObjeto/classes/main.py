from pessoa import Pessoa

# Criando objetos
p1 = Pessoa('Daniel', 25)
p2 = Pessoa('Maria', 20)

# Chamando o método da classe para testar
# p1.comer('Maçã')
# p1.pararComer()
# p1.pararComer()
# p1.comer('Laranja')
# p1.falar('POO')
# p1.pararComer()
# p1.falar('POO')
# p1.comer('Laranja')
# p1.falar('JAVA')
# p1.pararFalar()
# p1.pararFalar()

# Mostrando como os objetos agem indenpendente um do outro
p1.comer('Laranja')
p2.comer('Abacaxi')


print(p1.anoDeNascimento())
print(p2.anoDeNascimento())
p3 = Pessoa.criarPorAnoNascimento('Danilo', 2005)
print(p3.nome, p3.idade)


# Chamando o método estático
print(p1.gerarId())