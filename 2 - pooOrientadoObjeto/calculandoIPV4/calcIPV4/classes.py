import re


class CalcIPv4:
    def __init__(self, ip, mascara=None, prefixo=None):
        self.ip = ip
        self.mascara = mascara
        self.prefixo = prefixo

        self._setBroadcast()
        self._setRede()

    # Getters
    @property
    def ip(self):
        return self._ip

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def rede(self):
        return self._rede

    @property
    def mascara(self):
        return self._mascara

    @property
    def prefixo(self):
        return self._prefixo

    # Setters
    @ip.setter
    def ip(self, valor):
        # Usando a função validaIp para checar se é válido, se não retorna erro
        if not self._validaIp(valor):
            raise ValueError('IP Inválido')
        self._ip = valor
        self._ipBin = self.ipToBin(valor)

    @mascara.setter
    def mascara(self, valor):
        # Se não for instanciado com máscara então retorna nada
        if not valor:
            return

        # Se instanciado com Máscara então checa se a Máscara é válida, senão retorna erro
        if not self._validaIp(valor):
            raise ValueError('Máscara Inválida')
        self._mascara = valor

        # Convertendo a Máscara para binário usando a função ipToBin
        self._mascara_bin = self.ipToBin(valor)

        if not hasattr(self, 'prefixo'):
            self.prefixo = self._mascara_bin.count('1')

    @prefixo.setter
    def prefixo(self, valor):
        # Se não instaciar com prefixo então não faz nada
        if not valor:
            return

        # Verificando se o prefixo digitado é um valor inteiro
        if not isinstance(valor, int):
            raise TypeError('Prefixo precisa ser inteiro')

        # E se ele tem até 32bits
        if valor <= 0 or valor > 32:
            raise TypeError('Prefixo ter até 32 bits')

        self._prefixo = valor

        # Convertendo o prefixo para binário, para isso pego o prefixo informado quando instancio e multiplico pela
        # string '1', depois disso preencho o que faltar para completar 32Bits com zeros a direita usando a função
        # ljust
        if not hasattr(self, 'mascara'):
            self._mascara_bin = (valor * '1').ljust(32, '0')

        # Convertendo o binário de volta para IP
        self.mascara = self.binToIp(self._mascara_bin)

    # Função para validar se o IP/Máscara é válido
    @staticmethod
    def _validaIp(ip):

        # Usando expressão regular para validar se só tem números [0-9] e se tem 3 caracteres {1,3}, separados por '.'
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )

        if regexp.search(ip):
            return True

    # Convertendo o IP para binário aqui
    @staticmethod
    def ipToBin(ip):
        # Criando uma lista separando os blocos pelo '.'
        blocos = ip.split('.')
        # Após separar os blocos na lista, uso o List Comprehension para converter em binário
        # Na list ocorre o seguinte, percorro a lista item a item e uso a função BIN() para converter em binário
        # Depois uso o fatiamento ([2:]) para remover os dois primeiros caracteres de cada item após a conversão
        # porque a função BIN retorna com '0b' na frente
        # depois uso a função ZFILL(), para auto completar com zeros quando tiver menos 8 caracteres no item.
        blocos_binarios = [bin(int(item))[2:].zfill(8) for item in blocos]
        # Unificando o resultado usando a função Join
        return ''.join(blocos_binarios)

    # Convertendo binário para IP
    @staticmethod
    def binToIp(ip):
        # Criando váriável de controle para usar no List comprehension
        n = 8
        # Criando a lista separando em blocos de 8 bits os valores binários, transformo em inteiro usando int e após
        # converter o binário em inteiro, converto novamente para String
        blocos = [str(int(ip[i:n + i], 2)) for i in range(0, 32, n)]
        return '.'.join(blocos)

    def _setBroadcast(self):
        # Quantidade de bits disponível para Hosts
        host_bits = 32 - self.prefixo
        self._broadcastBin = self._ipBin[:self.prefixo] + (host_bits * '1')
        self._broadcast = self.binToIp(self._broadcastBin)
        return self._broadcast

    def _setRede(self):
        # Quantidade de bits disponível para Hosts
        host_bits = 32 - self.prefixo
        self._redeBin = self._ipBin[:self.prefixo] + (host_bits * '0')
        self._rede = self.binToIp(self._redeBin)
        return self._rede

    # Função para saber quantos IP's tenho disponível, já removendo o Broadcast e a Máscara
    def getNumeroIps(self):
        return 2 ** (32 - self.prefixo) - 2
