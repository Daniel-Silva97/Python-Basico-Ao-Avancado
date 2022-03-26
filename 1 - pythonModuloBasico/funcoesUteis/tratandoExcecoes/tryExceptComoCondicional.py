"""
Try .. Except como condicional em python
"""


# Converter a string vinda do input para INT
def converteNumero(valor):
    # Em casos que o valor for inteiro, ele vai tentar
    try:
        valor = int(valor)
        return valor
    except ValueError:
        # Em casos que o valor tiver casa decimal, ele usa esta linha
        try:
            valor = float(valor)
            return valor
        except ValueError:
            # Aqui se nenhum try der certo ele retorna None
            pass


while True:
    # Chamando a função no input
    numero = converteNumero(input('Digite um número: '))
    # Se retornar o None (em casos que nada deu certo) então:
    if numero is None:
        print('Este valor não é número!')
    # Se der certo executa aqui
    else:
        print(numero * 5)
