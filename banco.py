from conta import Conta
from cliente import Cliente
import datetime
import mysql.connector as mysql

conexao = mysql.connect(
	host = "localhost", 
	db = "banco", 
	user = "root", 
	password = "Ericly$2", 
	auth_plugin = 'mysql_native_password')
cursor = conexao.cursor(buffered = True)
cursor.execute("SELECT DATABASE();")
linhas = cursor.fetchall()

# class Cadastro:

def busca(cpf):
	command = "SELECT * FROM contas WHERE titular = '{}'".format(cpf)
	cursor.execute(command)
	for i in cursor:
		return i
	return None

def buscaP(cpf):
	command = "SELECT * FROM clientes WHERE cpf = '{}'".format(cpf)
	cursor.execute(command)
	for i in cursor:
		return i
	return None

def buscaC(numero):
	command = "SELECT * FROM contas WHERE numero = '{}'".format(numero)
	cursor.execute(command)
	for i in cursor:
		return i
	return None


def login(cpf, senha):
	command = "SELECT * FROM contas WHERE titular = '{}' and senha = MD5('{}')".format(cpf, senha)
	cursor.execute(command)
	for i in cursor:
		return True
	return False
		

def createTables():

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
	
	cursor.execute("""
			CREATE TABLE IF NOT EXISTS clientes(
				nome VARCHAR(50) NOT NULL,
				cpf VARCHAR(11) PRIMARY KEY NOT NULL,
				endereco VARCHAR(120) NOT NULL,
				nascimento DATE
			);
		""")

def deposita(valor: float, destino: tuple, op = 0, emisor: str = None):
	if destino[2]+valor > destino[4]:
		return False
	else:
		command = "UPDATE contas SET saldo = {} WHERE numero = {}".format(str(destino[2] + valor), str(destino[0]))
		cursor.execute(command)
		conexao.commit()

		if op == 0:
			command = "UPDATE contas SET historico = '{}' WHERE numero = {}".format((destino[5]+"Deposito de {} dia {}\n".format(valor, datetime.datetime.now())), str(destino[0]))
			cursor.execute(command)
			conexao.commit()
	
		else:
			command = "UPDATE contas SET historico = '{}' WHERE numero = {}".format((destino[5]+"Tansferencia de {} recebida de {} dia {}\n".format(valor, emisor, datetime.datetime.now())), str(destino[0]))
			cursor.execute(command)
			conexao.commit()
	
		return True

def sacar(valor: float, conta: tuple, op = 0, pessoa : str = None):
	pass
	if float(conta[2]) < valor:
		return False
	else:
		command = "UPDATE contas SET saldo = {} WHERE numero = {}".format(str(conta[2] - valor), str(conta[0]))
		cursor.execute(command)
		conexao.commit()

		if op == 0:
			command = "UPDATE contas SET historico = '{}' WHERE numero = {}".format((conta[5]+"Saque de {} reais realizado com sucesso em: {}\n".format(valor, datetime.datetime.now())), conta[0])
			cursor.execute(command)
			conexao.commit()
	
		else:
			command = "UPDATE contas SET historico = '{}' WHERE numero = {}".format((conta[5]+"Transferencia de {} reais para {} realizada con sucesso em: {}\n".format(valor, pessoa, datetime.datetime.now())), str(conta[0]))
			cursor.execute(command)
			conexao.commit()
		   
		return True


def transferir(valor, remetente, nRem, destinatario, nDest):
	if remetente[2] >= valor and destinatario[4] >= valor+destinatario[2]:
		sacar(valor, remetente, 1, nDest)
		deposita(valor, destinatario, 1 ,nRem)
		return True
	else:
		return False

def criaConta(titular: str,senha, saldo = 0, limite = 1000):

	cursor.execute(
	"""
	INSERT INTO contas
	(titular, saldo, senha, limite, historico)
	VALUES
	(%s, %s, md5(%s), %s, %s)
	""", (titular, str(saldo), senha, str(limite), "data de abertura: {}\n".format(datetime.datetime.today())))
	conexao.commit()
	return True

def criaCliente(nome, cpf, endereco, nascimento):
	if buscaP(cpf) != None:
		return False
	cursor.execute(
	"""
	INSERT INTO clientes 
	(nome, cpf, endereco, nascimento) 
	VALUES
	(%s, %s, %s, %s)
	""", (nome, cpf, endereco, nascimento))
	conexao.commit()
	
	return True