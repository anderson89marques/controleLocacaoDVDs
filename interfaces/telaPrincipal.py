# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaPrincipal.ui'
#
# Created: Wed Oct 15 15:13:42 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 60, 791, 491))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(_fromUtf8("background-image: url(:/imagens/linguagens2.png);"))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuLogin = QtGui.QMenu(self.menubar)
        self.menuLogin.setObjectName(_fromUtf8("menuLogin"))
        self.menuCadastro = QtGui.QMenu(self.menubar)
        self.menuCadastro.setObjectName(_fromUtf8("menuCadastro"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionFazer_login = QtGui.QAction(MainWindow)
        self.actionFazer_login.setEnabled(True)
        self.actionFazer_login.setObjectName(_fromUtf8("actionFazer_login"))
        self.actionFilme = QtGui.QAction(MainWindow)
        self.actionFilme.setObjectName(_fromUtf8("actionFilme"))
        self.actionCliente = QtGui.QAction(MainWindow)
        self.actionCliente.setObjectName(_fromUtf8("actionCliente"))
        self.menuLogin.addAction(self.actionFazer_login)
        self.menuCadastro.addAction(self.actionFilme)
        self.menuCadastro.addAction(self.actionCliente)
        self.menubar.addAction(self.menuLogin.menuAction())
        self.menubar.addAction(self.menuCadastro.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuLogin.setTitle(_translate("MainWindow", "login", None))
        self.menuCadastro.setTitle(_translate("MainWindow", "Cadastro", None))
        self.actionFazer_login.setText(_translate("MainWindow", "Fazer login", None))
        self.actionFilme.setText(_translate("MainWindow", "Filme", None))
        self.actionCliente.setText(_translate("MainWindow", "Cliente", None))

import img

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

