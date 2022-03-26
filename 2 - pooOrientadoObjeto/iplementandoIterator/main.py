# Iplementando iterador

# Criando a lógica existente na lista, MANUALMENTE
class MinhaLista:
    # Inicializando a lista e o indice
    def __init__(self):
        self.__items = []
        self.__index = 0

    # Lógica para adicionar +1 item a lista quando chamado
    def add(self, dado):
        self.__items.append(dado)

    # Função para buscar o item na lista usando o indice, por exemplo lista[0] ou lista[1]
    def __getitem__(self, index):
        return self.__items[index]

    # Usado para as iterações nos laços por exemplo
    def __iter__(self):
        return self

    # Outra função para as iterações de laços, porém aqui tratamos exceções como IndexError por exemplo
    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration

    # Retorno quando chamado via print()
    def __str__(self):
        return f'{self.__class__.__name__}({self.__items})'

    # Adicionando itens na lista
    def __setitem__(self, index, value):
        if index >= len(self.__items):
            self.__items.append(value)
        self.__items[index] = value

    def __delitem__(self, index):
        try:
            del self.__items[index]
        except IndexError:
            raise IndexError('Não existe valores a serem deletados neste indice')


if __name__ == "__main__":
    lista = MinhaLista()
    lista.add('Daniel')
    lista.add('Maria')

    for valor in lista:
        print(valor)

    print(lista)
    lista[0] = 'João'
    print(lista)

    lista[2] = 'Funciona'
    print(lista)

    del lista[2]
    print(lista)
