# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmCliente.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from Controller.ClienteCTR import ClienteCTR

class Ui_frmCliente(object):
    #preencher os campos para alteração
    def PreencherAlterar(self, nome, cpf, endereco, email, telefone):
        self.edtNome.setText(nome)
        self.edtCPF.setText(cpf)
        self.edtEndereco.setText(endereco)
        self.edtEmail.setText(email)
        self.edtTelefone.setText(telefone)
    
    #click botão salvar
    def btnSalvar_Click(self, estado, codigoCli):
        nome = self.edtNome.text()
        cpf = self.edtCPF.text()
        endereco = self.edtEndereco.text()
        email = self.edtEmail.text()
        telefone = self.edtTelefone.text()

        #verifica o estado inserir/alterar e chama a função
        if estado=='inserir':
            cliente = ClienteCTR
            cliente.CadastrarCliente(nome, cpf, endereco, email, telefone)

            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Cliente inserido com sucesso!")
            msg.setWindowTitle("Inserir Cliente")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        
        if estado=='alterar':
            cliente = ClienteCTR
            cliente.AtualizarCliente(codigoCli, nome, cpf, endereco, email, telefone)

            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Cliente alterado com sucesso!")
            msg.setWindowTitle('Alterar Cliente')
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()

        self.edtNome.setText('')
        self.edtCPF.setText('')
        self.edtEndereco.setText('')
        self.edtEmail.setText('')
        self.edtTelefone.setText('')    

    def setupUi(self, frmCliente, estado, codigoCli):
        frmCliente.setObjectName("FrmCliente")

        #desabilitar aumentar e diminuir tela
        frmCliente.setFixedSize(532, 269)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../TesteProjeto/View/Imagens/btnCadCli.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmCliente.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(frmCliente)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 511, 161))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 10, 46, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(340, 10, 46, 13))
        self.label_2.setObjectName("label_2")
        self.lbEndereco = QtWidgets.QLabel(self.groupBox)
        self.lbEndereco.setGeometry(QtCore.QRect(10, 110, 51, 16))
        self.lbEndereco.setObjectName("lbEndereco")
        self.lbEmail = QtWidgets.QLabel(self.groupBox)
        self.lbEmail.setGeometry(QtCore.QRect(10, 60, 46, 13))
        self.lbEmail.setObjectName("lbEmail")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(340, 60, 46, 13))
        self.label_5.setObjectName("label_5")
        self.edtNome = QtWidgets.QLineEdit(self.groupBox)
        self.edtNome.setGeometry(QtCore.QRect(10, 30, 321, 20))
        self.edtNome.setObjectName("edtNome")
        self.edtCPF = QtWidgets.QLineEdit(self.groupBox)
        self.edtCPF.setGeometry(QtCore.QRect(340, 30, 161, 20))
        self.edtCPF.setObjectName("edtCPF")
        self.edtEmail = QtWidgets.QLineEdit(self.groupBox)
        self.edtEmail.setGeometry(QtCore.QRect(10, 80, 321, 20))
        self.edtEmail.setObjectName("edtEmail")
        self.edtTelefone = QtWidgets.QLineEdit(self.groupBox)
        self.edtTelefone.setGeometry(QtCore.QRect(340, 80, 161, 20))
        self.edtTelefone.setObjectName("edtTelefone")
        self.edtEndereco = QtWidgets.QLineEdit(self.groupBox)
        self.edtEndereco.setGeometry(QtCore.QRect(10, 130, 491, 20))
        self.edtEndereco.setObjectName("edtEndereco")
        self.groupBox_2 = QtWidgets.QGroupBox(frmCliente)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 180, 511, 81))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.btnSalvar = QtWidgets.QPushButton(self.groupBox_2)
        self.btnSalvar.setGeometry(QtCore.QRect(400, 10, 101, 61))
        self.btnSalvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../../TesteProjeto/Imagens/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalvar.setIcon(icon1)
        self.btnSalvar.setIconSize(QtCore.QSize(35, 35))
        self.btnSalvar.setObjectName("btnSalvar")
        #Click botão salvar
        self.btnSalvar.clicked.connect(lambda: self.btnSalvar_Click(estado, codigoCli))

        self.retranslateUi(frmCliente)
        QtCore.QMetaObject.connectSlotsByName(frmCliente)

    def retranslateUi(self, frmCliente):
        _translate = QtCore.QCoreApplication.translate
        frmCliente.setWindowTitle(_translate("frmCliente", "Cadastro de Cliente", None))
        self.label.setText(_translate("frmCliente", "Nome", None))
        self.label_2.setText(_translate("frmCliente", "CPF", None))
        self.lbEndereco.setText(_translate("frmCliente", "Endereço", None))
        self.lbEmail.setText(_translate("frmCliente", "Email", None))
        self.label_5.setText(_translate("frmCliente", "Telefone", None))
        self.btnSalvar.setText(_translate("frmCliente", "Salvar", None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmCliente = QtWidgets.QWidget()
    ui = Ui_frmCliente()
    ui.setupUi(frmCliente)
    frmCliente.show()
    sys.exit(app.exec_())
