import pymysql.cursors
from contextlib import contextmanager  # Para encerrar a conexão após rodar os comandos


# Criando o gerenciador de contexto para encerrar a conexão automaticamente
@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='mestre',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        conexao.close()


# Inserindo uma linha
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         insert = 'INSERT INTO clientes(nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
#         cursor.execute(insert, ('Jack', 'Daniels', 25, 88))
#         conexao.commit()


# Inserindo Várias linhas
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         insert = 'INSERT INTO clientes(nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
#         dados = [
#             ('MURIEL', 'FIGUEIREDO', '19', '55'),
#             ('MARIA', 'EDUARDA', '22', '70'),
#             ('JOSE', 'MARCOS', '25', '43'),
#         ]
#         cursor.executemany(insert, dados)
#         conexao.commit()


# Deletando uma linha
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         delete = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(delete, (6,))
#         conexao.commit()

# Deletando várias linhas
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         delete = 'DELETE FROM clientes WHERE id in (%s, %s, %s)'
#         cursor.execute(delete, (7, 8, 9))
#         conexao.commit()

# Deletando usando BETWEEN
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         delete = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#         cursor.execute(delete, (10, 12))
#         conexao.commit()

# Usando o UPDATE
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         update = 'UPDATE clientes SET nome = %s WHERE id = %s'
#         cursor.execute(update, ('JOANA', 5))
#         conexao.commit()

with conecta() as conexao:  # Para fechar a conexão
    with conexao.cursor() as cursor:  # Para fechar o cursor
        cursor.execute('SELECT * FROM clientes ORDER BY id DESC LIMIT 100')
        resultado = cursor.fetchall()
        for linha in resultado:
            print(linha['id'], linha['nome'], linha['sobrenome'], linha['idade'], linha['peso'], )
