# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Tue Oct 28 23:31:07 2014
#      by: PyQt4 UI code generator 4.11.1
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

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName(_fromUtf8("Login"))
        Login.resize(400, 283)
        self.btenviarlogin = QtGui.QPushButton(Login)
        self.btenviarlogin.setGeometry(QtCore.QRect(250, 200, 98, 31))
        self.btenviarlogin.setObjectName(_fromUtf8("btenviarlogin"))
        self.layoutWidget = QtGui.QWidget(Login)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 10, 321, 181))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.logintx = QtGui.QLineEdit(self.layoutWidget)
        self.logintx.setObjectName(_fromUtf8("logintx"))
        self.horizontalLayout.addWidget(self.logintx)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setEnabled(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.senhatx = QtGui.QLineEdit(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.senhatx.sizePolicy().hasHeightForWidth())
        self.senhatx.setSizePolicy(sizePolicy)
        self.senhatx.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.senhatx.setEchoMode(QtGui.QLineEdit.Password)
        self.senhatx.setObjectName(_fromUtf8("senhatx"))
        self.horizontalLayout_2.addWidget(self.senhatx)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(_translate("Login", "Form", None))
        self.btenviarlogin.setText(_translate("Login", "Enviar", None))
        self.label.setText(_translate("Login", "Locadora LANNA", None))
        self.label_2.setText(_translate("Login", "Login:", None))
        self.label_3.setText(_translate("Login", "Senha:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Login = QtGui.QWidget()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())

