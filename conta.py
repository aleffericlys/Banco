import datetime
from cliente import Cliente

class Conta:
	_numeroContas = 0
	__slots__ = ['_numero', '_titular', '_saldo', '_limite', '_historico' ]
	def __init__(self, numero, titular : Cliente, saldo, limite = 1000):
		self._numero = numero
		self._titular = titular
		self._saldo = saldo
		self._limite = limite
		self._historico = Historico()
		Conta._numeroContas += 1


	@staticmethod
	def get_total_contas():
		return Conta._numeroContas

	@property
	def numero(self):
		return self._numero
	
	@numero.setter
	def numero(self, numero):
		self._numero = numero

	@property
	def saldo(self):
		return self._saldo
	
	@saldo.setter
	def saldo(self, saldo):
		self._saldo = saldo

	@property
	def titular(self):
		return self._titular
	
	@titular.setter
	def titular(self, titular):
		self._titular = titular

	@property
	def limite(self):
		return self._limite
	
	@limite.setter
	def limite(self, limite):
		self._limite = limite
	
	def deposita(self, valor):
		if self._saldo+valor > self._limite:
			self._historico.transacoes.append("Deposito de {} reais não realizado em: {}".format(valor, datetime.datetime.now()))
			print("limite exedido!!")
			return False
		else:
			self._historico.transacoes.append("Deposito de {} reais realizado em: {}".format(valor, datetime.datetime.now()))
			self._saldo += valor
			return True
	

	def sacar(self, valor):
		if self._saldo < valor:
			self._historico.transacoes.append("Saque de {} reais não realizado realizado em: {}".format(valor, datetime.datetime.now()))
			print("não há _saldo disponível")
			return False
		else:
			self._historico.transacoes.append("Saque de {} reais realizado con sucesso em: {}".format(valor, datetime.datetime.now()))
			print("Operação reaizada com sucesso")
			self._saldo -= valor
			return True
		
	
	def extratos(self):
		self._titular.imprimir()
		print("Conta: {}\nsaldo: {} \nlimite: {}".format(self._numero, self._saldo, self._limite))
		self._historico.imprimir()

	def transferir(self, destino, valor):
		if self.sacar(valor):
			if destino.deposita(valor):
				self._historico.transacoes.append("transferencia de {} reais realizada con sucesso em: {}".format(valor, datetime.datetime.now()))
				print("Operação realizada com sucesso!")
				return True
			else:
				self._historico.transacoes.append("transferencia de {} reais não realizada em: {}".format(valor, datetime.datetime.now()))
				print("Operação não pode ser realizada")
				self.deposita(valor)
				return False
		else:
			return False


class Historico:
	def __init__(self):
		self.dataDeAbertura = datetime.datetime.today()
		self.transacoes = []
	
	def imprimir(self):
		print("data de abertura: {}".format(self.dataDeAbertura))
		print("transações: ")
		for i in self.transacoes:
			print(i)
