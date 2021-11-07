import datetime
from cliente import Cliente
import mysql.connector as mysql

class Conta:

	conexao = mysql.connect(host = "localhost", db = "banco", user = "root", password = "7650FNAF")
	cursor = conexao.cursor(buffered = True)
	cursor.execute("SELECT DATABASE();")
	linha = cursor.fetchone()
	cursor.execute("""
		CREATE TABLE IF NOT EXISTS contas(
			numero integer AUTO_INCREMENT PRIMARY KEY,
			titular text NOT NULL,
			saldo float NOT NULL,
			senha VARCHAR(32) NOT NULL,
			limite float NOT
		);
		""")

	_numeroContas = 0
	__slots__ = ['_numero', '_titular', '_saldo', '_senha', '_limite', '_historico' ]
	def __init__(self, numero, titular : Cliente, senha, saldo: float = 0, limite: float = 1000):
		Conta.cursor.execute(
        """
		INSERT INTO contas 
		(titular, saldo, senha, limite) VALUES 
		(%s, %f, MD5(%s), %f)
		""", (titular, saldo, senha, limite))

		self._numero = numero
		self._titular = titular
		self._senha = senha
		self._saldo = saldo
		self._limite = limite
		self._historico = Historico()
		Conta._numeroContas += 1


	@staticmethod
	def get_total_contas():
		return Conta._numeroContas

	@property
	def numero(self):
		Conta.cursor.execute("SELECT numero FROM contas", (self._numero))
		return self._numero

	@property
	def saldo(self):
		Conta.cursor.execute("SELECT saldo FROM contas", (self._saldo))
		return self._saldo

	@property
	def titular(self):
		Conta.cursor.execute("SELECT titular FROM contas", (self._titular))
		return self._titular
	
	@titular.setter
	def titular(self, titular):
		self._titular = titular
		Conta.cursor.execute("UPDATE contas SET titular = (%s)", (self._titular))

	@property
	def limite(self):
		Conta.cursor.execute("SELECT limite FROM contas", (self._limite))
		return self._limite
	
	@limite.setter
	def limite(self, limite):
		self._limite = limite
		Conta.cursor.execute("UPDATE contas SET limite = (%f)", (self._limite))
	
	def deposita(self, valor, op = 0, pessoa : Cliente = None):
		if self._saldo+valor > self._limite:
			return False
		else:
			if op == 0:
				self._historico.transacoes.append("Deposito de {} reais realizado em: {}".format(valor, datetime.datetime.now()))
			else:
				self._historico.transacoes.append("Transferencia de {} reais de {} recebida em: {}".format(valor, pessoa.nome, datetime.datetime.now()))
				self._saldo += valor
				Conta.cursor.execute("UPDATE contas SET saldo = (%f) LIMIT 1", (self._saldo))
			return True
	

	def sacar(self, valor, op = 0, pessoa : Cliente = None):
		if self._saldo < valor:
			return False
		else:
			if op == 1:
				self._historico.transacoes.append("transferencia de {} reais para {} realizado con sucesso em: {}".format(valor, pessoa.nome, datetime.datetime.now()))
			else:
				self._historico.transacoes.append("Saque de {} reais realizado con sucesso em: {}".format(valor, datetime.datetime.now()))
				self._saldo -= valor
				Conta.cursor.execute("UPDATE contas SET saldo = (%f) LIMIT 1", (self._saldo))
			return True
	
	def extratos(self):
		# self._titular.imprimir()
		# print("Conta: {}\nsaldo: {} \nlimite: {}".format(self._numero, self._saldo, self._limite))
		return self._historico.historico

	def transferir(self, destino, valor):
		if self.saldo >= valor and destino.limite >= valor+destino.saldo:
			self.sacar(valor, 1, destino.titular)
			destino.deposita(valor, 1, self.titular)
			return True
		else:
			return False


class Historico:
	def __init__(self):
		self.dataDeAbertura = datetime.datetime.today()
		self.transacoes = []
		self.transacoes.append(self.dataDeAbertura)

	@property
	def historico(self):
		return self.transacoes
	
	def imprimir(self):
		print("data de abertura: {}".format(self.dataDeAbertura))
		print("transações: ")
		for i in self.transacoes:
			print(i)
