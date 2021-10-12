from conta import Conta

class Cadastro:
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


	def busca(self, numero):
		for conta in self._lista_contas:
			if numero == conta.numero:
				return conta
		
		return None

	def login(self, cpf):
		for conta in self._lista_contas:
			if cpf == conta.titular.cpf:
				return True
			
		return False

	def senha(self, senha):
		for conta in self._lista_contas:
			if senha == conta.senha:
				return conta
			
		return False