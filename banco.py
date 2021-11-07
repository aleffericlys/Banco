from conta import Conta
from cliente import Cliente
import mysql.connector as mysql

class Cadastro:

	conexao = mysql.connect(host = "Banco", db = "banco", user = "root", password = "7650FNAF")
	cursor = conexao.cursor()
	cursor.execute("SELECT DATABASE();")

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
		for conta in self._lista_contas:
			if cpf == conta.titular.cpf:
				return conta
		
		return None
	
	def buscaC(self, numero):
		for conta in self._lista_contas:
			if numero == conta.numero:
				return conta
		
		return None

	def login(self, cpf):
		for conta in self._lista_contas:
			if cpf == conta.titular.cpf:
				return True
			
		return False

	def senha(self, senha: str):
		for conta in self._lista_contas:
			if senha == conta.senha:
				return True
			
		return False