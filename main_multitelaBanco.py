import sys
import socket

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from cliente import Cliente
from conta import Conta
from banco import *
from tela_operacoes import TelaOperacoes
from tela_saque import TelaSaque
from tela_transferencia import TelaTransferencia
from tela_extrato import TelaExtrato
from tela_cadastro_pessoa import TelaCadPessoa
from tela_incial import TelaInicial
from tela_login import TelaLogin
from tela_deposito import TelaDeposito


class Ui_Main(QtWidgets.QWidget):
	def setupUi(self, Main):
		Main.setObjectName('Main')
		Main.resize(640, 480)

		self.QtStack = QtWidgets.QStackedLayout()

		self.stack0 = QtWidgets.QMainWindow()
		self.stack1 = QtWidgets.QMainWindow()
		self.stack2 = QtWidgets.QMainWindow()
		self.stack3 = QtWidgets.QMainWindow()
		self.stack4 = QtWidgets.QMainWindow()
		self.stack5 = QtWidgets.QMainWindow()
		self.stack6 = QtWidgets.QMainWindow()
		self.stack7 = QtWidgets.QMainWindow()

		self.tela_operacoes = TelaOperacoes()
		self.tela_operacoes.setupUi(self.stack4)

		self.tela_transferencia = TelaTransferencia()
		self.tela_transferencia.setupUi(self.stack1)

		self.tela_saque = TelaSaque()
		self.tela_saque.setupUi(self.stack2)

		self.tela_extrato = TelaExtrato()
		self.tela_extrato.setupUi(self.stack3)

		self.tela_inicial = TelaInicial()
		self.tela_inicial.setupUi(self.stack0) 

		self.tela_login = TelaLogin()
		self.tela_login.setupUi(self.stack5)

		self.tela_cadastro_pessoa = TelaCadPessoa()
		self.tela_cadastro_pessoa.setupUi(self.stack6)

		self.tela_deposito = TelaDeposito()
		self.tela_deposito.setupUi(self.stack7)

		self.QtStack.addWidget(self.stack0)
		self.QtStack.addWidget(self.stack1)
		self.QtStack.addWidget(self.stack2)
		self.QtStack.addWidget(self.stack3)
		self.QtStack.addWidget(self.stack4)
		self.QtStack.addWidget(self.stack5)
		self.QtStack.addWidget(self.stack6)
		self.QtStack.addWidget(self.stack7)

class Main(QMainWindow, Ui_Main):
	_logado: str
	_pessoa: tuple

	ip = "localhost"
	port = 7022
	addr = ((ip, port))
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect(addr)

	def __init__(self, parent = None):
		super(Main, self).__init__(parent)
		self.setupUi(self)

		self.tela_inicial.pushButton.clicked.connect(self.botaoAcessarConta)
		self.tela_inicial.pushButton_2.clicked.connect(self.botaoCriarConta)
		self.tela_inicial.pushButton_3.clicked.connect(self.botaoDeposito)
		self.tela_inicial.pushButton_4.clicked.connect(self.desconectar)

		self.tela_login.pushButton.clicked.connect(self.botaoLogin)
		self.tela_login.pushButton_2.clicked.connect(self.botaoSair)

		self.tela_cadastro_pessoa.pushButton.clicked.connect(self.botaoCadastrar)
		self.tela_cadastro_pessoa.pushButton_2.clicked.connect(self.botaoSair)

		self.tela_operacoes.pushButton.clicked.connect(self.abrirTelaTransferencia)
		self.tela_operacoes.pushButton_2.clicked.connect(self.abrirTelaSaque)
		self.tela_operacoes.pushButton_3.clicked.connect(self.abrirTelaExtrato)
		self.tela_operacoes.pushButton_4.clicked.connect(self.botaoSair)

		self.tela_transferencia.pushButton.clicked.connect(self.botaoTransferir)
		self.tela_transferencia.pushButton_2.clicked.connect(self.botaoVoltar)

		self.tela_saque.pushButton.clicked.connect(self.botaoSacar)
		self.tela_saque.pushButton_2.clicked.connect(self.botaoVoltar)
		
		self.tela_extrato.pushButton.clicked.connect(self.botaoVoltar)

		self.tela_deposito.pushButton.clicked.connect(self.botaoDepositar)
		self.tela_deposito.pushButton_2.clicked.connect(self.botaoSair)

	def botaoLogin(self):
		cpf = self.tela_login.lineEdit.text()
		senha = self.tela_login.lineEdit_2.text()
		if not(cpf == '' or senha == ''):
			self.client_socket.send(f"login|{cpf}|{senha}".encode())
			retorno = self.client_socket.recv(1024).decode().split(sep = '|')
			if retorno[0] != 'logado':
				QMessageBox.information(None, 'Login', 'CPF ou Senha incorretos')
			else:
				self.tela_login.lineEdit.setText('')
				self.tela_login.lineEdit_2.setText('')
				self._logado = retorno[1]
				self.QtStack.setCurrentIndex(4)
		else:
			QMessageBox.warning(None, 'Login', 'Todos os campos devem ser preenchidos')

	def botaoAcessarConta(self):
		self.QtStack.setCurrentIndex(5)

	def botaoCriarConta(self):
		self.QtStack.setCurrentIndex(6)

	def botaoDeposito(self):
		self.QtStack.setCurrentIndex(7)
	
	def botaoCadastrar(self):
		nome = self.tela_cadastro_pessoa.lineEdit.text()
		cpf = self.tela_cadastro_pessoa.lineEdit_2.text()
		endereco = self.tela_cadastro_pessoa.lineEdit_3.text()
		nascimento = self.tela_cadastro_pessoa.lineEdit_4.text()
		senha = self.tela_cadastro_pessoa.lineEdit_5.text()
		
		self.client_socket.send(f"criar|{nome}|{cpf}|{endereco}|{nascimento}|{senha}".encode())
		retorno = self.client_socket.recv(1024).decode()
		if retorno != 'conta criada':
			QMessageBox.information(None, 'Cadastro', 'Pessoa já cadastrada')
		else:
			QMessageBox.information(None, 'Conta', 'Conta cadastrada com sucesso')
			self.tela_cadastro_pessoa.lineEdit.setText('')
			self.tela_cadastro_pessoa.lineEdit_2.setText('')
			self.tela_cadastro_pessoa.lineEdit_3.setText('')
			self.tela_cadastro_pessoa.lineEdit_4.setText('')
			self.tela_cadastro_pessoa.lineEdit_5.setText('')
			self.QtStack.setCurrentIndex(0)

	def botaoDepositar(self):
		conta = self.tela_deposito.lineEdit.text()
		valor = self.tela_deposito.lineEdit_2.text()
		if not(conta == '' or valor == ''):
			self.client_socket.send(f"deposito|{conta}|{valor}".encode())
			retorno = self.client_socket.recv(1024).decode()
			if retorno == 'depositado':
				QMessageBox.information(None, 'Deposito', 'Deposito realizado com sucesso')
				self.tela_deposito.lineEdit.setText('')
				self.tela_deposito.lineEdit_2.setText('')
				self.QtStack.setCurrentIndex(0)
			else:
				 	QMessageBox.information(None, 'Deposito', 'limite insuficiente')
		else:
			QMessageBox.information(None, 'Deposito', 'Preencha todos os campos')

	def botaoTransferir(self):
		conta = self.tela_transferencia.lineEdit.text()
		valor = float(self.tela_transferencia.lineEdit_2.text())
		if not(conta == '' or valor == ''):
			self.client_socket.send(f"transfere|{valor}|{self._logado}|{conta}".encode())
			retorno = self.client_socket.recv(1024).decode()
			if retorno == 'feito':
				QMessageBox.information(None, 'Transferência', 'Transfêrencia realizada com sucesso')
				self.tela_transferencia.lineEdit.setText('')
				self.tela_transferencia.lineEdit_2.setText('')
				self.QtStack.setCurrentIndex(4)
			else:
				QMessageBox.information(None, 'Transferência', 'Transferência não pode ser realizada')
		else:
			QMessageBox.information(None, 'Transferencia', 'Preencha todos os campos')
		
		
	def botaoSacar(self):
		valor = float(self.tela_saque.lineEdit.text())
		self.client_socket.send(f"sacar|{self._logado}|{valor}".encode())
		retorno = self.client_socket.recv(1024).decode()
		if retorno == 'sacado':
			QMessageBox.information(None, 'Saque', 'Saque realizado com sucesso')
			self.tela_transferencia.lineEdit.setText('')
			self.QtStack.setCurrentIndex(4)
		else:
			QMessageBox.information(None, 'Saque', 'Saldo insuficiente')
			self.tela_transferencia.lineEdit.setText('')

	def abrirTelaTransferencia(self):
		self.QtStack.setCurrentIndex(1)

	def abrirTelaSaque(self):
		self.QtStack.setCurrentIndex(2)

	def abrirTelaExtrato(self):
		self.client_socket.send(f"extrato|{self._logado}".encode())
		recebido = self.client_socket.recv(10240).decode()
		ext = recebido.split(sep = "|")
		self.tela_extrato.listWidget.clear()
		self.tela_extrato.listWidget.addItem("Nome: {}".format(ext[0]))
		self.tela_extrato.listWidget.addItem("CPF: {}".format(ext[1]))
		self.tela_extrato.listWidget.addItem("Numero da conta: {}".format(ext[2]))
		self.tela_extrato.listWidget.addItem("Saldo: {}".format(ext[3]))
		self.tela_extrato.listWidget.addItem("Transações:")
		self.tela_extrato.listWidget.addItem("{}".format(ext[4]))
		self.QtStack.setCurrentIndex(3)

	def botaoVoltar(self):
		self.QtStack.setCurrentIndex(4)

	def botaoSair(self):
		self.QtStack.setCurrentIndex(0)
		
	def desconectar(self):
		self.client_socket.send("bye".encode())
		self.client_socket.close()
		sys.exit()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	show_main = Main()
	sys.exit(app.exec_())
