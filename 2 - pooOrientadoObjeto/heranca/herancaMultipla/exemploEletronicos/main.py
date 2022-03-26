from smartphone import Smartphone

smartphone = Smartphone('Galaxy S10')
smartphone.desligar()
smartphone.conectar()  # "Galaxy S10 não está ligado"
smartphone.ligar()
smartphone.conectar()  # "Galaxy S10 está conectado!"
smartphone.conectar()  # "Galaxy S10 já está conectado"
smartphone.conectar()  # "Galaxy S10 já está conectado"
smartphone.desligar()
smartphone.conectar()  # "Galaxy S10 não está ligado"
smartphone.ligar()
