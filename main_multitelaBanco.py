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
from tela_extrato import TelaExtrato
from tela_cadastro_conta import TelaCadConta
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
		self.stack8 = QtWidgets.QMainWindow()

		self.tela_operacoes = Tela_Operacoes()
		self.tela_operacoes.setupUi(self.stack4)

		self.tela_transferencia = Tela_Transferencia()
		self.tela_transferencia.setupUi(self.stack1)

		self.tela_saque = Tela_Saque()
		self.tela_saque.setupUi(self.stack2)

		self.tela_extrato = TelaExtrato()
		self.tela_extrato.setupUi(self.stack3)

		self.tela_inicial = TelaInicial()
		self.tela_inicial.setupUi(self.stack0) 

		self.tela_login = TelaLogin()
		self.tela_login.setupUi(self.stack5)

		self.tela_cadastro_pessoa = TelaCadPessoa()
		self.tela_cadastro_pessoa.setupUi(self.stack6)

		self.tela_cadastro_conta = TelaCadConta()
		self.tela_cadastro_conta.setupUi(self.stack7)

		self.tela_deposito = TelaDeposito()
		self.tela_deposito.setupUi(self.stack8)

		self.QtStack.addWidget(self.stack0)
		self.QtStack.addWidget(self.stack1)
		self.QtStack.addWidget(self.stack2)
		self.QtStack.addWidget(self.stack3)
		self.QtStack.addWidget(self.stack4)
		self.QtStack.addWidget(self.stack5)
		self.QtStack.addWidget(self.stack6)
		self.QtStack.addWidget(self.stack7)
		self.QtStack.addWidget(self.stack8)

class Main(QMainWindow, Ui_Main):
	_logado: Conta
	_pessoa: Cliente
	def __init__(self, parent = None):
		super(Main, self).__init__(parent)
		self.setupUi(self)

		self.banco = Cadastro()

		self.tela_inicial.pushButton.clicked.connect(self.botaoAcessarConta)
		self.tela_inicial.pushButton_2.clicked.connect(self.botaoCriarConta)
		self.tela_inicial.pushButton_3.clicked.connect(self.botaoDeposito)
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

		self.tela_deposito.pushButton.clicked.connect(self.botaoDepositar)
		self.tela_deposito.pushButton_2.clicked.connect(self.botaoSair)

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

	def botaoDeposito(self):
		self.QtStack.setCurrentIndex(8)
	
	def botaoCadastrar(self):
		conta = self.tela_cadastro_conta.lineEdit.text()
		senha = self.tela_cadastro_conta.lineEdit_2.text()
		limite = float(self.tela_cadastro_conta.lineEdit_3.text())
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
		conta = self.tela_deposito.lineEdit.text()
		valor = self.tela_deposito.lineEdit_2.text()
		if not(conta == '' or valor == ''):
			conta_destino = self.banco.buscaC(conta)
			if conta_destino != None:
				if conta_destino.deposita(float(valor)):
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
			conta_destino = self.banco.buscaC(conta)
			if conta_destino != None:
				if self._logado.transferir(conta_destino, valor):
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
		if self._logado.sacar(valor):
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
		historico = self._logado.extratos()
		self.tela_extrato.listWidget.clear()
		self.tela_extrato.listWidget.addItem("Cliente: {}".format(self._logado.titular.nome))
		self.tela_extrato.listWidget.addItem("CPF: {}".format(self._logado.titular.cpf))
		self.tela_extrato.listWidget.addItem("Numero da conta: {}".format(self._logado.numero))
		self.tela_extrato.listWidget.addItem("Saldo: {}".format(self._logado.saldo))
		self.tela_extrato.listWidget.addItem("Limte: {}".format(self._logado.limite))
		self.tela_extrato.listWidget.addItem("data de abertura: {}".format(historico[0]))
		self.tela_extrato.listWidget.addItem("Transações:")
		for i in historico[1:]:
			self.tela_extrato.listWidget.addItem("\t{}".format(i))
		self.QtStack.setCurrentIndex(3)

	def botaoVoltar(self):
		self.QtStack.setCurrentIndex(4)

	def botaoSair(self):
		self.QtStack.setCurrentIndex(0)


if __name__ == "__main__":
	app = QApplication(sys.argv)
	show_main = Main()
	sys.exit(app.exec_())
