"""
EM PYTHON TUDO É UM OBJETO: incluindo classes
Metaclasses são as "classes" que criam classes.
type é uma metaclasse(!!!???)
"""

# Criando a Metaclasse herdando do type
class MetaClasse(type):
    # Definindo o new com os dados da classe
    def __new__(metaclasse, nomeclasse, classespai, namespace):
        # Quando o nome da Classe for A, ele printa o nome no console
        if nomeclasse == 'A':
            print(nomeclasse)
            return type.__new__(metaclasse, nomeclasse, classespai, namespace)

        # Validando se existe a função b_funcao na classe que está chamando a função presente na classe A
        if 'b_fala' not in namespace:
            print(f'Você precisa criar o métodob_fala em {nomeclasse}')
        # Validando se foi criado o método ao invés do atributo
        else:
            if not callable(namespace['b_fala']):
                print('Método b_fala precisa ser método e não atributo')

        return type.__new__(metaclasse, nomeclasse, classespai, namespace)


class A(metaclass=MetaClasse):
    def fala(self):
        self.b_fala()


class B(A):
    # pass

    @staticmethod
    def b_fala():
        print('Oi')
