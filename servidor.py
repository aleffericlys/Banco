import socket
import threading
from banco import *

from tela_extrato import TelaExtrato

tela = TelaExtrato()

class ClientThreading(threading.Thread):
	logado = tuple
	def __init__(self, clientAddress, clientSocket):
		threading.Thread.__init__(self)
		self.csocket = clientSocket
		print(f"Nova conexao: {clientAddress}")

	def run(self):
		print(f"Conectado de: {clientAddress}")
		while True:
			data = self.csocket.recv(1024)
			msg = data.decode()

			var = msg.split(sep = '|')
			# val = -1
			if var[0] == 'criar':
				createTables()
				if criaCliente(var[1], var[2], var[3], var[4]):
					criaConta(var[2], var[5])
					self.csocket.send("conta criada".encode())
				else:
					self.csocket.send("conta não criada".encode())

			elif var[0] == 'deposito':
				print(var)
				conta = buscaC(var[1])
				if deposita(float(var[2]), conta):
					self.csocket.send("depositado".encode())
				else:
					self.csocket.send("não depositado".encode())
			# val = soma(int(var[1]), int(var[2]))

			elif var[0] == 'sacar':
				conta = busca(var[1])
				if sacar(float(var[2]), conta):
					self.csocket.send("sacado".encode())
				else:
					self.csocket.send("não sacado".encode())
			# 	val = sub(int(var[1]), int(var[2]))

			elif var[0] == 'login':
				if login(var[1], var[2]):
					self.logado = buscaP(var[1])
					# msg = "{}|{}|{}|{}|{}|{}".format(self.logado[0],self.logado[1],self.logado[2],self.logado[3],self.logado[4],self.logado[5])
					self.csocket.send(f"logado|{var[1]}".encode())
				else:
					self.csocket.send("não logado".encode())
			# 	val = mult(int(var[1]), int(var[2]))
			
			elif var[0] == 'transfere':
				contaR = busca(var[2])
				contaRP = buscaP(contaR[1])
				contaD = buscaC(var[3])
				if contaD != None:
					contaDP = buscaP(contaD[1])
					if transferir(float(var[1]), contaR, contaRP[0], contaD, contaDP[0]):
						self.csocket.send("feito".encode())
				else:
					self.csocket.send("nada feito".encode())

			# 	val = div(int(var[1]), int(var[2]))
			# self.csocket.send((str(val)).encode())

			elif var[0] == 'extrato':
				contaN = buscaP(var[1])
				nConta = busca(var[1])
				manda = "{}|{}|{}|{}|{}".format(contaN[0], nConta[1], nConta[0], nConta[2], nConta[5])
				self.csocket.send(manda.encode())

			if msg == 'bye':
				break
		print(f"Client at {clientAddress} disconnected...")
	
if __name__ == '__main__':
	LOCALHOST = ''
	PORT = 7022
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server.bind((LOCALHOST, PORT))
	print("Servidor iniciado.")
	print("Aguardando nova conexão")
	while True:
		server.listen(1)
		clientSocket, clientAddress  = server.accept()
		newThread = ClientThreading(clientAddress, clientSocket)
		newThread.start()
