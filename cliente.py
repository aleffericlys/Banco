import mysql.connector as mysql

class Cliente:

	conexao = mysql.connect(
		host = "localhost", 
		db = "banco", 
		user = "root",
		password = "7650FNAF", 
		auth_plugin = 'mysql_native_password')

	cursor = conexao.cursor(buffered = True)
	cursor.execute("SELECT DATABASE();")
	cursor.execute("""
			CREATE TABLE IF NOT EXISTS clientes(
				nome VARCHAR(50) NOT NULL,
				cpf VARCHAR(11) NOT NULL PRIMARY KEY,
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
		
		self._nome = nome
		self._cpf = cpf
		self._endereco = endereco
		self._nascimento = nascimento

	@property
	def nome(Nome):
		Cliente.cursor.execute("SELECT nome FROM clientes WHERE nome = (%s)", (Nome))
		linhas = Cliente.cursor.fetchone()
		for linha in linhas:
			return linha

	@nome.setter
	def set_nome(self, nome):
		self._nome = nome
		Cliente.cursor.execute("UPDATE clientes SET nome = (%s)", (self._nome))

	@property
	def endereco(self):
		Cliente.cursor.execute("SELECT endereco FROM clientes", (self._endereco))
		return self._endereco
	
	@endereco.setter
	def endereco(self, endereco):
		self._endereco = endereco
		Cliente.cursor.execute("UPDATE clientes SET endereco = (%s)", (self._endereco))

	@property
	def cpf(self):
		Cliente.cursor.execute("SELECT cpf FROM clientes", (self._cpf))
		for linha in Cliente.linhas:
			return linha[1]
	
	@cpf.setter
	def cpf(self, cpf):
		self._cpf = cpf
		Cliente.cursor.execute("UPDATE cliente SET cpf = (%s)", (self._cpf))

	
	@property
	def nascimento(self):
		Cliente.cursor.execute("SELECT nascimento FROM clientes", (self._nascimento))
		return self._nascimento
	
	@nascimento.setter
	def nascimento(self, nascimento):
		self._nascimento = nascimento
		Cliente.cursor.execute("UPDATE cliente SET nascimento = (%s)", (self._nascimento))

	def imprimir(self):
		print("Nome: ", self.nome)
		print("endereco: ", self.endereco)
		print("CPF: ", self.cpf)
		print("Nasciemnto", self.nascimento)
