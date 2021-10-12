class Cliente:

	__slots__ = ['_nome', '_endereco', '_cpf', '_nascimento']
	def __init__(self, nome, cpf, endereco, nascimento):
		self._nome = nome
		self._cpf = cpf
		self._endereco = endereco
		self._nascimento = nascimento

	@property
	def nome(self):
		return self._nome
	
	@nome.setter
	def nome(self, nome):
		self._nome = nome

	@property
	def endereco(self):
		return self._endereco
	
	@endereco.setter
	def endereco(self, endereco):
		self._endereco = endereco

	@property
	def cpf(self):
		return self._cpf
	
	@cpf.setter
	def cpf(self, cpf):
		self._cpf = cpf
	
	@property
	def nascimento(self):
		return self._nascimento
	
	@nascimento.setter
	def nascimento(self, nascimento):
		self._nascimento = nascimento

	def imprimir(self):
		print("Nome: ", self.nome)
		print("endereco: ", self.endereco)
		print("CPF: ", self.cpf)
		print("Nasciemnto", self.nascimento)
