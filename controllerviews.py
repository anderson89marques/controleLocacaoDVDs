__author__ = 'anderson'
from PyQt4 import QtCore, QtGui
from interfaces import (telaPrincipal, login,
                        cadastroCliente, cadastroFilme)
from controller import Controller
from banco.classesdb import *

"""
    Herda de tela, assim, quando for criar os métodos que forem tratar os signals,
    a classe não fica muito grande
"""
class TelaPrincipal(QtGui.QMainWindow, telaPrincipal.Ui_MainWindow):
    def __init__(self):
        super(TelaPrincipal, self).__init__()
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

        self.menuCadastro.setEnabled(False)
        self.actionFilme.setEnabled(False)
        self.actionCliente.setEnabled(False)

        self.move(100, 200)
        self.resize(1000, 1000)

    def fazerLogin(self):
        self.w = Login(self)
        self.w.control = self.control
        self.w.show()

    def cadastroCliente(self):
        print("cliente")
        self.cc = CadastroCliente()
        self.cc.control = self.control
        self.cc.show()

    def cadastroFilme(self):
        self.cf = CadastroFilme(self, self.control)
        self.cf.show()

"""
    Herda de login, assim, quando for criar os métodos que forem tratar os signals,
    a classe não fica muito grande
"""
class Login(QtGui.QWidget, login.Ui_Login):
    #Definindo um sinal que será conectado ao metodo close
    closeApp = QtCore.pyqtSignal()

    def __init__(self, mainwin):
        super(Login, self).__init__()
        self.setupUi(self)
        self.move(200, 200)
        self.control = None
        self.mainwindow = mainwin

        self.closeApp.connect(self.close)
        self.btenviarlogin.clicked.connect(self.logar)

    def logar(self):
        txl = self.logintx.text()
        txs = self.senhatx.text()
        l = self.control.login(txl, txs)
        if l:
            #QtGui.QMessageBox("login ok", "Login realizado com sucesso", QtGui.QMessageBox.)
            self.mainwindow.menuCadastro.setEnabled(True)
            self.mainwindow.actionFilme.setEnabled(True)
            self.mainwindow.actionCliente.setEnabled(True)
            self.mainwindow.menuLogin.setEnabled(False)
            self.mainwindow.actionFazer_login.setEnabled(False)

            self.closeApp.emit()
        print(txs)


"""
    Herda de cadatroFilme, assim, quando for criar os métodos que forem tratar os signals,
    a classe não fica muito grande
"""
class CadastroFilme(QtGui.QWidget, cadastroFilme.Ui_Form):
    #Definindo um sinal que será conectado ao metodo close
    closeApp = QtCore.pyqtSignal()

    def __init__(self, mainwin, ctrl):
        super(CadastroFilme, self).__init__()
        self.setupUi(self)
        self.move(200, 200)
        self.control = ctrl
        self.mainwindow = mainwin

        self.cfcodigo.setText(str(self.control.gerar_codigo_filme()))
        self.cfcodigo.setReadOnly(True)

        self.closeApp.connect(self.close)
        self.cfbtsalvar.clicked.connect(self.cadastrar_filme)

    def cadastrar_filme(self):
        dvd = Dvd(codigo=int(self.cfcodigo.text()),nome=self.cftitulo.text(),
                  genero=self.cfcategoria.text(), quantidade=int(self.cfquantidade.text()))
        print(dvd)
        self.control.cadastrar_filme(dvd)
        self.closeApp.emit()


"""
    Herda de cadatroClinte, assim, quando for criar os métodos que forem tratar os signals,
    a classe não fica muito grande
"""
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