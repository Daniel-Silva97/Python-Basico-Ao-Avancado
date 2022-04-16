import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conexao = sqlite3.connect(arquivo)
        self.cursor = self.conexao.cursor()

    def inserir(self, nome, telefone):
        insert = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(insert, (nome, telefone))
        self.conexao.commit()

    def editar(self, nome, telefone, id):
        update = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(update, (nome, telefone, id))
        self.conexao.commit()

    def excluir(self, id):
        delete = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(delete, (id,))
        self.conexao.commit()

    def listar(self):
        select = 'SELECT * FROM agenda'
        self.cursor.execute(select)

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        select = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(select, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conexao.close()


if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    # agenda.inserir('Daniel', '111111')
    # agenda.inserir('Maria', '222222')
    # agenda.inserir('Matheus', '333333')
    # agenda.inserir('Rose', '444444')
    # agenda.inserir('Guilherme', '555555')
    # agenda.inserir('Ana', '666666')
    # agenda.editar('Francisco', '131313', 6)
    # agenda.inserir('Daniel Silva', '101010')
    # agenda.inserir('Daniel Souza', '202020')
    # agenda.inserir('Daniel Santos', '303030')
    # agenda.inserir('Carlos Daniel', '404040')
    # agenda.excluir(6)
    agenda.buscar('Daniel')
