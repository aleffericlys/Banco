import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from cliente import Cliente
from conta import Conta, Historico
from banco import Cadastro
from tela_operacoes import Tela_Operacoes
from tela_saque import Tela_Saque
from tela_transferencia import Tela_Transferencia
from tela_extrato import Tela_Extrato
from tela_cadastro_conta import TelaCadConta
from tela_cadastro_pessoa import TelaCadPessoa
from tela_incial import TelaInicial
from tela_login import TelaLogin

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

		self.tela_operacoes = Tela_Operacoes()
		self.tela_operacoes.setupUi(self.stack4)

		self.tela_transferencia = Tela_Transferencia()
		self.tela_transferencia.setupUi(self.stack1)

		self.tela_saque = Tela_Saque()
		self.tela_saque.setupUi(self.stack2)

		self.tela_extrato = Tela_Extrato()
		self.tela_extrato.setupUi(self.stack3)

		self.tela_inicial = TelaInicial()
		self.tela_inicial.setupUi(self.stack0) 

		self.tela_login = TelaLogin()
		self.tela_login.setupUi(self.stack5)

		self.tela_cadastro_pessoa = TelaCadPessoa()
		self.tela_cadastro_pessoa.setupUi(self.stack6)

		self.tela_cadastro_conta = TelaCadConta()
		self.tela_cadastro_conta.setupUi(self.stack7)


		self.QtStack.addWidget(self.stack0)
		self.QtStack.addWidget(self.stack1)
		self.QtStack.addWidget(self.stack2)
		self.QtStack.addWidget(self.stack3)
		self.QtStack.addWidget(self.stack4)
		self.QtStack.addWidget(self.stack5)
		self.QtStack.addWidget(self.stack6)
		self.QtStack.addWidget(self.stack7)

class Main(QMainWindow, Ui_Main):
	_logado: Conta
	_pessoa: Cliente
	def __init__(self, parent = None):
		super(Main, self).__init__(parent)
		self.setupUi(self)

		self.banco = Cadastro()

		self.tela_inicial.pushButton.clicked.connect(self.botaoAcessarConta)
		self.tela_inicial.pushButton_2.clicked.connect(self.botaoCriarConta)
		self.tela_inicial.pushButton_3.clicked.connect(self.botaoDepositar)
		self.tela_inicial.pushButton_4.clicked.connect(sys.exit)

		self.tela_login.pushButton.clicked.connect(self.botaoLogin)

		self.tela_cadastro_pessoa.pushButton.clicked.connect(self.botaoProximo)

		self.tela_cadastro_conta.pushButton.clicked.connect(self.botaoCadastrar)
	
		self.tela_operacoes.pushButton.clicked.connect(self.abrirTelaTransferencia)
		self.tela_operacoes.pushButton_2.clicked.connect(self.abrirTelaSaque)
		self.tela_operacoes.pushButton_3.clicked.connect(self.abrirTelaExtrato)
		self.tela_operacoes.pushButton_5.clicked.connect(self.abrirTelaSaque)
		self.tela_operacoes.pushButton_5.clicked.connect(self.botaoSair)

		self.tela_transferencia.pushButton.clicked.connect(self.botaoTransferir)

		self.tela_saque.pushButton.clicked.connect(self.botaoSacar)
		
		self.tela_extrato.pushButton.clicked.connect(self.botaoVoltar)

	def botaoLogin(self):
		cpf = self.tela_login.lineEdit.text()
		senha = self.tela_login.lineEdit_2.text()
		if not(cpf == '' or senha == ''):
			if not(self.banco.login(cpf)) and not(self.banco.senha(senha)):
				QMessageBox.information(None, 'Login', 'CPF e Senha incorretos')
			elif not self.banco.login(cpf):
				QMessageBox.information(None, 'Login', 'CPF incorreto')
			elif not self.banco.senha(senha):
				QMessageBox.information(None, 'Login', 'Senha incorreta')
			else:
				self.tela_login.lineEdit.setText('')
				self.tela_login.lineEdit_2.setText('')
				self._logado = self.banco.busca(cpf)
				self.QtStack.setCurrentIndex(4)
			
		else:
			QMessageBox.warning(None, 'Login', 'Todos os campos devem ser preenchidos')

	def botaoAcessarConta(self):
		self.QtStack.setCurrentIndex(5)

	def botaoCriarConta(self):
		self.QtStack.setCurrentIndex(6)
	
	def botaoCadastrar(self):
		conta = self.tela_cadastro_conta.lineEdit.text()
		senha = self.tela_cadastro_conta.lineEdit_2.text()
		limite = self.tela_cadastro_conta.lineEdit_3.text()
		if self.banco.buscaC(conta) != None:
			QMessageBox.information(None, 'Conta', 'Numero de conta indisponível')
			self.tela_cadastro_conta.lineEdit.setText('')
		else:
			self.banco.cadastra(Conta(conta, self._pessoa, senha, limite= limite))
			QMessageBox.information(None, 'Conta', 'Conta cadastrada com sucesso')
			self.QtStack.setCurrentIndex(0)

	def botaoProximo(self):
		nome = self.tela_cadastro_pessoa.lineEdit.text()
		cpf = self.tela_cadastro_pessoa.lineEdit_2.text()
		endereco = self.tela_cadastro_pessoa.lineEdit_3.text()
		nascimento = self.tela_cadastro_pessoa.lineEdit_4.text()
		if self.banco.busca(cpf):
			QMessageBox.information(None, 'Cadastro', 'Pessoa já cadastrada')
		else:
			self.tela_cadastro_pessoa.lineEdit.setText('')
			self.tela_cadastro_pessoa.lineEdit_2.setText('')
			self.tela_cadastro_pessoa.lineEdit_3.setText('')
			self.tela_cadastro_pessoa.lineEdit_4.setText('')
			self._pessoa = Cliente(nome, cpf, endereco, nascimento)
			self.QtStack.setCurrentIndex(7)

	def botaoDepositar(self):
		pass

	def botaoTransferir(self):
		
		conta = self.tela_transferencia.lineEdit.text()
		valor = self.tela_transferencia.lineEdit_2.text()
		if not(conta == '' or valor == ''):
			conta_destino = self.banco.buscaC(conta)
			if conta_destino != None:
				if self._logado.transferir(conta_destino, valor):
					QMessageBox.information(None, 'Transferencia', 'Transferencia realizada com sucesso')
					self.tela_transferencia.lineEdit.setText('')
					self.tela_transferencia.lineEdit_2.setText('')
					self.QtStack.setCurrentIndex(4)
				else:
				 	QMessageBox.information(None, 'Transferencia', 'Transferência não pode ser realizada')
			# if (self.operacao.(c)):
			# else:
			# 	QMessageBox.information(None, 'POO2', 'O CPF informado já está cadastrado na base de dados!')
		else:
			QMessageBox.information(None, 'Transferencia', 'Preencha todos os campos')
		
		
	def botaoSacar(self):
		pass
		'''
		cpf = self.tela_busca.lineEdit.text()
		pessoa = self.cad.busca(cpf)
		if (pessoa != None):
			self.tela_busca.lineEdit_2.setText(pessoa.nome)
			self.tela_busca.lineEdit_3.setText(pessoa.endereco)
			self.tela_busca.lineEdit_4.setText(pessoa.nascimento)
		else:
			QMessageBox.information(None, 'POO2', 'CPF não encontrado!')
		'''

	def abrirTelaTransferencia(self):
		self.QtStack.setCurrentIndex(1)

	def abrirTelaSaque(self):
		self.QtStack.setCurrentIndex(2)

	def abrirTelaExtrato(self):
		self.QtStack.setCurrentIndex(3)

	def botaoVoltar(self):
		self.QtStack.setCurrentIndex(4)

	def botaoSair(self):
		self.QtStack.setCurrentIndex(0)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	show_main = Main()
	sys.exit(app.exec_())
