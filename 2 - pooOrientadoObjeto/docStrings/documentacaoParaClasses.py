class Teste:
    """Documentação para classes

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

    atributo1 = 'Atributo 1'
    atributo2 = 'Atributo 2'

    def __init__(self, x, y):
        """Inicializando o método

        :param x: Teste Doc 1
        :param y: Teste Doc 2
        """
        self.x = x
        self.y = y

    @staticmethod
    def retornaTexto(x):
        """ Função para exibir texto

        : param x: Texto informado
        : return: Retorna este texto

        : raises TypeError: Precisa ser uma String
        : raises ValueError: Precisa ter menos de 100 caracteres
        """
        if isinstance(x, str):
            raise TypeError('Precisa ser uma String')

        if len(x) > 100:
            raise ValueError('Precisa ter menos de 100 caracteres')

        return x
