"""
No Python, o comportamento dos operadores é definido por métodos especiais
Vamos alterar o comportamento de operadores com classes definidas pelo usuário

Operador    Método          Operação
------------------------------------------------------
+           __add__         adição
-           __sub__         subtração
*           __mul__         multiplicação
/           __div__         divisão
//          __floordiv__    divisão inteira
%           __mod__         Módulo
**          __pow__         Potência
+           __pos__         Positivo
-           __neg__         Negativo
<           __lt__          Menor que
>           __gt__          Maior que
<=          __le__          Menor ou igual a
>=          __ge__          Maior ou igual a
==          __eq__          Igual a
!=          __ne__          Diferente de
<<          __lshift__      Deslocamento para a esquerda
>>          __rshift__      Deslocamento para a direita
&           __and__         E bit-a-bit
|           __or__          OU bit-a-bit
^           __xor__         OU exclusivo bit-a-bit
~           __inv__         inversão
"""


class Retangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Alterando como o print irá exibir o Objeto
    def __repr__(self):
        return f"<class 'Retangulo'({self.x}, {self.y})>"

    # Alterando o formato como o Operador '+' irá calcular o objeto
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Retangulo(novo_x, novo_y)

    def getArea(self):
        return self.x * self.y

    # Ajustando para verificar se um retângulo é menor que o outro
    def __lt__(self, other):
        a1 = self.getArea()
        a2 = other.getArea()

        if a1 < a2:
            return True
        else:
            return False

    # Ajustando para verificar se um retângulo é maior que o outro
    def __gt__(self, other):
        a1 = self.getArea()
        a2 = other.getArea()

        if a1 > a2:
            return True
        else:
            return False

    # Ajustando para verificar se um retângulo é igual ao outro (x, y)
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


r1 = Retangulo(10, 20)
r2 = Retangulo(10, 20)

# Alterando o comportamento da soma aqui, usando o que foi colocado no método __add__
r3 = r1 + r2

# Alterando o comportamento da exibição aqui, usando o __repr__
print(r3)

# Alterando o comportamento do '>' usando o que foi passado no __gt__
print(r3 > r1)

# Alterando o comportamento do '<' usando o que foi passado no __lt__
print(r3 < r1)

# Alterando o comportamento do '==' usando o que foi passado no __eq__
print(r1 == r2)
