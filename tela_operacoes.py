# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_operacoes.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Tela_Operacoes(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 40, 151, 41))
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 120, 131, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.pushButton.setFont(font1)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(250, 190, 131, 31))
        self.pushButton_2.setFont(font1)
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(250, 330, 131, 31))
        self.pushButton_4.setFont(font1)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(250, 260, 131, 31))
        self.pushButton_3.setFont(font1)
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(250, 400, 131, 31))
        self.pushButton_5.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Opera\u00e7\u00f5es", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Transfer\u00eancia", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Saque", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Hist\u00f3rico", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Extrato", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
    # retranslateUi

def main():
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Tela_Operacoes()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()