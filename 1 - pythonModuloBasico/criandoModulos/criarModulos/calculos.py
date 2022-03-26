import math

PI = math.pi


def dobra_lista(lista):
    return [x*2 for x in lista]


def multiplica(lista2):
    r = 1
    for r in lista2:
        r *= 1
    return r


# Se irei importar esse arquivo em outro lugar para usar como módulo, essa condicional serve para que no outro arquivo
# Não execute os comandos no local em que importei
# Só serão executados os comandos abaixo se eu abrir esse arquivo 'calculos.py' e executá-lo
if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    print(dobra_lista(lista))
    print(multiplica(lista))
    print(PI)
