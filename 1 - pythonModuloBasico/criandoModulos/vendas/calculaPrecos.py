"""
Para criar um pacote2 é só ir no diretório
Clicar com botão direito em cima da pasta --> New --> Python Package
Dentro dos pacotes podemos criar os módulos para codar.
"""
from pythonModuloBasico.criandoModulos.vendas.formataPrecos import precos


def aumento(valor, porcentagem, formata=False):
    r = valor + (valor * (porcentagem / 100))
    if formata:
        return precos.real(r)
    else:
        return r


def reducao(valor, porcentagem, formata=False):
    r = valor - (valor * (porcentagem / 100))
    if formata:
        return precos.real(r)
    else:
        return r


"""
Funções serão utilizadas no arquivo "main.py"
"""
