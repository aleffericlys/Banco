import datetime
from cliente import Cliente
import mysql.connector as mysql

class Conta:

	conexao = mysql.connect(
		host = "localhost",
		user = "root",
		db = "banco",
		password = "7650FNAF", 
		auth_plugin = 'mysql_native_password')

	cursor = conexao.cursor(buffered = True)
	cursor.execute("USE banco;")
	cursor.execute("""
		CREATE TABLE IF NOT EXISTS contas(
			numero integer AUTO_INCREMENT UNIQUE PRIMARY KEY,
			titular VARCHAR(32),
			saldo float NOT NULL,
			senha VARCHAR(32) NOT NULL,
			limite float NOT NULL,
			historico text,
			CONSTRAINT fk_titular FOREIGN KEY (titular) REFERENCES clientes (cpf)
		);
		""")

	_numeroContas = 0
	__slots__ = ['_numero', '_titular', '_saldo', '_senha', '_limite', '_historico']
	def __init__(self, titular: str,senha, saldo = 0, limite = 1000):

		Conta._numeroContas += 1

		Conta.cursor.execute(
        """
		INSERT INTO contas
		(titular, saldo, senha, limite, historico)
		VALUES
		(%s, %s, md5(%s), %s, %s)
		""", (titular, str(saldo), senha, str(limite), "data de abertura: {}\n".format(datetime.datetime.today())))
		Conta.conexao.commit()
		Conta.conexao.close()