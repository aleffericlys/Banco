import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication
from cliente import Cliente

from conta import Conta, Historico
from tela_operacoes import Tela_Operacoes
from tela_saque import Tela_Saque
from tela_transferencia import Tela_Transferencia
from tela_extrato import Tela_Extrato
from tela_cadastro_conta import Tela_Cadastro_Conta
from tela_cadastro_pessoa import Tela_Cadastro_Pessoa
from tela_incial import Tela_Inicial
from tela_login import Tela_Login

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
        self.tela_operacoes.setupUi(self.stack0)

        self.tela_transferencia = Tela_Transferencia()
        self.tela_transferencia.setupUi(self.stack1)

        self.tela_saque = Tela_Saque()
        self.tela_saque.setupUi(self.stack2)

        self.tela_extrato = Tela_Extrato()
        self.tela_extrato.setupUi(self.stack3)

        self.tela_cadastro_conta = Tela_Cadastro_Conta()
        self.tela_cadastro_conta.setupUi(self.stack4)

        self.tela_cadastro_pessoa = Tela_Cadastro_Pessoa()
        self.tela_cadastro_pessoa.setupUi(self.stack5)

        self.tela_incial = TelaInicial()
        self.tela_incial.setupUi(self.stack6)

        self.tela_login = TelaLogin()
        self.tela_login.setupUi(self.stack7)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)

class Main(QMainWindow, Ui_Main):
    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
    
        self.tela_operacoes.pushButton.clicked.connect(self.abrirTelaTransferencia)
        self.tela_operacoes.pushButton_2.clicked.connect(self.abrirTelaSaque)
        self.tela_operacoes.pushButton_3.clicked.connect(self.abrirTelaExtrato)
        self.tela_operacoes.pushButton_5.clicked.connect(self.abrirTelaSaque)

        self.tela_transferencia.pushButton.clicked.connect(self.botaoTransferir)
        self.tela_saque.pushButton.clicked.connect(self.botaoSacar)
        self.tela_extrato.pushButton.clicked.connect(self.botaoVoltar)
        self.tela_operacoes.pushButton_5.clicked.connect(self.botaoSair)

    def botaoTransferir(self):
        pass
        '''
        conta_destino = self.tela_transferencia.lineEdit.text()
        valor = self.tela_transferencia.lineEdit_2.text()
        if not(conta_destino == '' or valor == ''):
            c = Conta.transferir(conta_destino, valor)
            if (self.operacao.(c)):
                QMessageBox.information(None, 'POO2', 'Cadastro realizado com sucesso!')
                self.tela_cadastro.lineEdit.setText('')
                self.tela_cadastro.lineEdit_2.setText('')
                self.tela_cadastro.lineEdit_3.setText('')
                self.tela_cadastro.lineEdit_4.setText('')
            else:
                QMessageBox.information(None, 'POO2', 'O CPF informado já está cadastrado na base de dados!')
        else:
            QMessageBox.information(None, 'POO2', 'Todos os valores devem ser preeenchidos!')
    
        self.QtStack.setCurrentIndex(0)
        '''
        
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
        self.QtStack.setCurrentIndex(0)

    def botaoSair(self):
        sys.exit()


def main():
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
