from conta import Conta
from cliente import Cliente
import mysql.connector as mysql

class Cadastro:

	conexao = mysql.connect(host = "Banco", db = "banco", user = "root", password = "7650FNAF", auth_plugin = 'mysql_native_password')
	cursor = conexao.cursor(buffered = True)
	cursor.execute("SELECT DATABASE();")
	linhas = cursor.fetchall()

	__slots__ = ['_lista_contas']
	def __init__(self):
		self._lista_contas = []

	def cadastra(self, conta: Conta):
		saida = self.busca(conta.numero)
		if (saida == None):
			self._lista_contas.append(conta)
			return True
		else:
			return False


	def busca(self, cpf):
		return Cadastro.cursor.execute("SELECT * FROM contas WHERE cpf = (%s)", cpf)
	
	def buscaC(self, numero):
		return Cadastro.cursor.execute("SELECT * FROM contas WHERE numero = (%s)", numero)

	def login(self, cpf):
		for conta in self._lista_contas:
			if Cadastro.cursor.execute("SELECT * FROM contas WHERE cpf = (%s)", cpf):
				return True 

	def senha(self, senha: str):
		for conta in self._lista_contas:
			if senha == conta.senha:
				return True
			
		return False