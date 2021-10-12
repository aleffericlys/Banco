import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from conta import Conta, Historico
from tela_operacoes import Tela_Operacoes
from tela_saque import Tela_Saque
from tela_transferencia import Tela_Transferencia
from tela_extrato import Tela_Extrato

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()

        self.tela_inicial = Tela_Operacoes()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_cadastro = Tela_Transferencia()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_busca = Tela_Saque()
        self.tela_busca.setupUi(self.stack2)

        self.tela_busca = Tela_Extrato()
        self.tela_busca.setupUi(self.stack3)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)

class Main(QMainWindow, Ui_Main):
    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
    
        self.operacao = Conta()
        self.tela_operacoes.pushButton.clicked.connect(self.abrirTelaTransferencia)
        self.tela_operacoes.pushButton_2.clicked.connect(self.abrirTelaSaque)
        self.tela_operacoes.pushButton_3.clicked.connect(self.abrirTelaExtrato)
        self.tela_operacoes.pushButton_5.clicked.connect(self.abrirTelaSaque)

        self.tela_transferencia.pushButton.clicked.connect(self.botaoTransferir)
        self.tela_saque.pushButton.clicked.connect(self.botaoSacar)
        self.tela_extrato.pushButton.clicked.connect(self.botaoVoltar)
        self.tela_operacoes.pushButton_5.clicked.connect(self.botaoSair)

    def botaoCadastrar(self):
        nome = self.tela_cadastro.lineEdit.text()
        endereco = self.tela_cadastro.lineEdit_2.text()
        cpf = self.tela_cadastro.lineEdit_3.text()
        nascimento = self.tela_cadastro.lineEdit_4.text()
        if not(nome == '' or endereco == '' or cpf == '' or nascimento == ''):
            p = Pessoa(nome, endereco, cpf, nascimento)
            if (self.cad.cadastrar(p)):
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
        
    def botaoBuscar(self):
        cpf = self.tela_busca.lineEdit.text()
        pessoa = self.cad.busca(cpf)
        if (pessoa != None):
            self.tela_busca.lineEdit_2.setText(pessoa.nome)
            self.tela_busca.lineEdit_3.setText(pessoa.endereco)
            self.tela_busca.lineEdit_4.setText(pessoa.nascimento)
        else:
            QMessageBox.information(None, 'POO2', 'CPF não encontrado!')
    
    def botaoVoltar(self):
        self.QtStack.setCurrentIndex(0)

    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)

    def abrirTelaBusca(self):
        self.QtStack.setCurrentIndex(2)

def main():
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
