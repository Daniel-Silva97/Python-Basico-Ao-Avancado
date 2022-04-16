import sqlite3

# Criando a conexão com base de dados
conexao = sqlite3.connect('basededados.db')

# Criando o cursor da Base de dados
cursor = conexao.cursor()

# Criando uma tabela
# cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome TEXT,'
#                'peso REAL'
#                ')')
# Inserindo valores na tabela, prevenindo o SQL Injection
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 60))  # Exemplo com Tuplas
# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
#                {'nome': 'João', 'peso': 60})  # Exemplo com Dicionários
# cursor.execute('INSERT INTO clientes VALUES (:id, :nome, :peso)',
#                {'id': None, 'nome': 'Mário', 'peso': 80})  # Exemplo com Dicionários

# Executando os comandos no banco
# conexao.commit()


# Update de um valor no banco
# cursor.execute('UPDATE clientes SET nome=:nome WHERE id=:id',
#                {'nome': 'Joana', 'id': 2})

# Deletando um dado
# cursor.execute('DELETE FROM clientes WHERE id=:id',
#                {'id': 2})

conexao.commit()


# Executando um select no banco
cursor.execute('SELECT * FROM clientes')

# Percorrendo todas as linhas retornadas do banco com fetchall()
for linha in cursor.fetchall():
    # Desempacotando os valores em variáveis
    identificador, nome, peso = linha
    print(identificador, nome, peso)

# Fechando o objeto do cursor
cursor.close()
# Fechando o objeto de conexão
conexao.close()
