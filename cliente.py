import mysql.connector as mysql

class Cliente:

	conexao = mysql.connect(
		host = "localhost",
		db = "banco", 
		user = "root",
		password = "Ericly$2", 
		auth_plugin = 'mysql_native_password')

	cursor = conexao.cursor(buffered = True)
	cursor.execute("USE banco;")
	cursor.execute("""
			CREATE TABLE IF NOT EXISTS clientes(
				nome VARCHAR(50) NOT NULL,
				cpf VARCHAR(11) PRIMARY KEY NOT NULL,
				endereco VARCHAR(120) NOT NULL,
				nascimento DATE
			);
		""")

	__slots__ = ['_nome', '_cpf', '_endereco', '_nascimento']
	def __init__(self, nome, cpf, endereco, nascimento):
		Cliente.cursor.execute(
        """
		INSERT INTO clientes 
		(nome, cpf, endereco, nascimento) 
		VALUES
		(%s, %s, %s, %s)
		""", (nome, cpf, endereco, nascimento))
		Cliente.conexao.commit()
		Cliente.conexao.close()