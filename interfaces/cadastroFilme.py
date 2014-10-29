# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cadastroFilme.ui'
#
# Created: Sun Oct 19 18:15:55 2014
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(478, 347)
        self.cfbtsalvar = QtGui.QPushButton(Form)
        self.cfbtsalvar.setGeometry(QtCore.QRect(140, 300, 98, 27))
        self.cfbtsalvar.setObjectName(_fromUtf8("cfbtsalvar"))
        self.cfbtcancelar = QtGui.QPushButton(Form)
        self.cfbtcancelar.setGeometry(QtCore.QRect(260, 300, 98, 27))
        self.cfbtcancelar.setObjectName(_fromUtf8("cfbtcancelar"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 40, 321, 29))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setSpacing(32)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setMargin(3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.cfcodigo = QtGui.QLineEdit(self.layoutWidget)
        self.cfcodigo.setObjectName(_fromUtf8("cfcodigo"))
        self.horizontalLayout_5.addWidget(self.cfcodigo)
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(40, 100, 321, 29))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(43)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setMargin(2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.cftitulo = QtGui.QLineEdit(self.widget)
        self.cftitulo.setObjectName(_fromUtf8("cftitulo"))
        self.horizontalLayout_2.addWidget(self.cftitulo)
        self.widget1 = QtGui.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(40, 160, 321, 29))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setSpacing(16)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.widget1)
        self.label_3.setMargin(3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.cfcategoria = QtGui.QLineEdit(self.widget1)
        self.cfcategoria.setObjectName(_fromUtf8("cfcategoria"))
        self.horizontalLayout_3.addWidget(self.cfcategoria)
        self.widget2 = QtGui.QWidget(Form)
        self.widget2.setGeometry(QtCore.QRect(40, 220, 321, 29))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget2)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.widget2)
        self.label_4.setMargin(3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.cfquantidade = QtGui.QLineEdit(self.widget2)
        self.cfquantidade.setObjectName(_fromUtf8("cfquantidade"))
        self.horizontalLayout_4.addWidget(self.cfquantidade)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Cadastro de Filme", None))
        self.cfbtsalvar.setText(_translate("Form", "Salvar", None))
        self.cfbtcancelar.setText(_translate("Form", "Cancelar", None))
        self.label_5.setText(_translate("Form", "Código:", None))
        self.label_2.setText(_translate("Form", "Título:", None))
        self.label_3.setText(_translate("Form", "Categoria:", None))
        self.label_4.setText(_translate("Form", "Quantidade:", None))


