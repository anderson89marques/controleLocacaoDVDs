__author__ = 'anderson'
from PyQt4 import QtCore, QtGui
from interfaces import (telaPrincipal, login,
                        cadastroCliente, cadastroFilme)
from controller import Controller

class TelaPrincipal(QtGui.QMainWindow, telaPrincipal.Ui_MainWindow):
    def __init__(self):
        super(TelaPrincipal,self).__init__()
        self.setupUi(self)

        self.w = None
        self.cc = None
        self.cf = None
        self.control = Controller()
        self.control.gerar_banco()
        self.control.cadastro_locadora()

        self.actionFazer_login.triggered.connect(self.fazerLogin)
        self.actionCliente.triggered.connect(self.cadastroCliente)
        self.actionFilme.triggered.connect(self.cadastroFilme)

        self.move(100, 200)
        self.resize(1000, 1000)

    def fazerLogin(self):
        print("login")
        self.w = Login()
        self.w.control = self.control
        self.w.show()

    def cadastroCliente(self):
        print("cliente")
        self.cc = CadastroCliente()
        self.cc.control = self.control
        self.cc.show()

    def cadastroFilme(self):
        print("filme")
        self.cf = CadastroFilme()
        self.cf.control = self.control
        self.cf.show()


class Login(QtGui.QWidget, login.Ui_Login):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.move(200, 200)
        self.control = None

        self.closeApp.connect(self.close)
        self.btenviarlogin.clicked.connect(self.logar)

    def logar(self):
        txl = self.logintx.text()
        txs = self.senhatx.text()
        l = self.control.login(txl, txs)
        if l:
            #QtGui.QMessageBox("login ok", "Login realizado com sucesso", QtGui.QMessageBox.)
            pass
        print(txl)

class CadastroFilme(QtGui.QWidget, cadastroFilme.Ui_Form):
    def __init__(self):
        super(CadastroFilme, self).__init__()
        self.setupUi(self)
        self.move(200, 200)
        self.control = None

class CadastroCliente(QtGui.QWidget, cadastroCliente.Ui_Form):
    def __init__(self):
        super(CadastroCliente, self).__init__()
        self.setupUi(self)
        self.move(200, 200)
        self.control = None

import sys

app = QtGui.QApplication(sys.argv)
t = TelaPrincipal()
t.show()
sys.exit(app.exec_())