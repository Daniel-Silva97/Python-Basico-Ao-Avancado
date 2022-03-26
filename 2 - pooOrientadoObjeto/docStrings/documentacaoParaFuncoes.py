"""Documentação para funções

Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature
from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia,
looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of
the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32
and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC.

This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum,
"Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.

The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested.
Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact
original form, accompanied by English versions from the 1914 translation by H. Rackham.
"""

variavel = 'valor'


def soma(x, y):
    """Soma x e y"""
    return x + y


def multiplica(x, y, z):
    """Multiplica os valores x,y,z

    Multiplica os valores x, y e z, mas o programador pode omitir a variável Z se não for necessária.
    """
    if z:
        return x * y
    else:
        return x * y * z


variavel2 = 'Valor 2'
variavel3 = 'Valor 3'
variavel4 = 'Valor 4'


def soma2(x, y):
    """Soma X e Y

    Efetuará a soma de x e y e retornar o valor na tela para o usuário.

    :param x: Número 1
    :type x: int or float
    :param y: Número 2
    :type y: int or float
    :return: Retorna X + Y
    :type return: int or float
    """
    return x + y
