# ENUM - Enumerações
from enum import Enum, auto


# Criando a classe que herda de Enum
class Directions(Enum):
    # auto() irá gerar valores automaticos começando do 1, pois não vou usar, só preciso da direção
    right = auto()
    left = auto()
    up = auto()
    down = auto()


# Teste básico para checar a direção
def move(direction):
    if not isinstance(direction, Directions):
        raise ValueError('Cannot move in this direction')
    return f'Moving {direction.name}'


if __name__ == '__main__':
    print(move(Directions.right))
    print(move(Directions.left))
    print(move(Directions.up))
    print(move(Directions.down))
    # print(move('qualquer lugar'))
