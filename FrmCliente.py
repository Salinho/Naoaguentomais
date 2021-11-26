from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from Controller.ClienteCTR import ClienteCTR

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

class Ui_frmCliente(object):
    #PREENCHER OS CAMPOS PARA ALTERAÇÃO
    def PreencherAlterar(self, nome, cpf, endereco, email, telefone):
        self.edtNome.setText(nome)
        self.edtCPF.setText(cpf)
        self.edtEndereco.setText(endereco)
        self.edtEmail.setText(email)
        self.edtTelefone.setText(telefone)

    #CLICK BTN_SALVAR
    def btnSalvar_Click(self, estado, codigoCli):
        nome = self.edtNome.text()
        cpf = self.edtCPF.text()
        endereco = self.edtEndereco.text()
        email = self.edtEmail.text()
        telefone = self.edtTelefone.text()

        #VERIFICA O ESTADO INSERIR/ALTERAR PARA CHAMAR A FUNÇAO APROPRIADA
        if estado=='inserir':
            cliente = ClienteCTR
            cliente.CadastrarCliente(nome, cpf, endereco, email, telefone)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Cliente inserido com sucesso!")
            msg.setWindowTitle("Inserir Cliente")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        if estado=='alterar':
            cliente = ClienteCTR
            cliente.AtualizarCliente(codigoCli, nome, cpf, endereco, email, telefone)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Cliente alterado com sucesso!")
            msg.setWindowTitle("Alterar Cliente")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        self.edtNome.setText('')
        self.edtCPF.setText('')
        self.edtEndereco.setText('')
        self.edtEmail.setText('')
        self.edtTelefone.setText('')

    def setupUi(self, frmCliente, estado, codigoCli):
        frmCliente.setObjectName(_fromUtf8("frmCliente"))

        #DESABILITAR REDIMENCIONAMENTO DA JANELA
        frmCliente.setFixedSize(532, 269)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Imagens/btnCadCli.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmCliente.setWindowIcon(icon)
        self.groupBox = QtGui.QGroupBox(frmCliente)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 511, 161))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 10, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(340, 10, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lbEndereco = QtGui.QLabel(self.groupBox)
        self.lbEndereco.setGeometry(QtCore.QRect(10, 110, 51, 16))
        self.lbEndereco.setObjectName(_fromUtf8("lbEndereco"))
        self.lbEmail = QtGui.QLabel(self.groupBox)
        self.lbEmail.setGeometry(QtCore.QRect(10, 60, 46, 13))
        self.lbEmail.setObjectName(_fromUtf8("lbEmail"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(340, 60, 46, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.edtNome = QtGui.QLineEdit(self.groupBox)
        self.edtNome.setGeometry(QtCore.QRect(10, 30, 321, 20))
        self.edtNome.setObjectName(_fromUtf8("edtNome"))
        self.edtCPF = QtGui.QLineEdit(self.groupBox)
        self.edtCPF.setGeometry(QtCore.QRect(340, 30, 161, 20))
        self.edtCPF.setObjectName(_fromUtf8("edtCPF"))
        self.edtEmail = QtGui.QLineEdit(self.groupBox)
        self.edtEmail.setGeometry(QtCore.QRect(10, 80, 321, 20))
        self.edtEmail.setObjectName(_fromUtf8("edtEmail"))
        self.edtTelefone = QtGui.QLineEdit(self.groupBox)
        self.edtTelefone.setGeometry(QtCore.QRect(340, 80, 161, 20))
        self.edtTelefone.setObjectName(_fromUtf8("edtTelefone"))
        self.edtEndereco = QtGui.QLineEdit(self.groupBox)
        self.edtEndereco.setGeometry(QtCore.QRect(10, 130, 491, 20))
        self.edtEndereco.setObjectName(_fromUtf8("edtEndereco"))
        self.groupBox_2 = QtGui.QGroupBox(frmCliente)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 180, 511, 81))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.btnSalvar = QtGui.QPushButton(self.groupBox_2)
        self.btnSalvar.setGeometry(QtCore.QRect(400, 10, 101, 61))
        self.btnSalvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Imagens/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalvar.setIcon(icon1)
        self.btnSalvar.setIconSize(QtCore.QSize(35, 35))
        self.btnSalvar.setObjectName(_fromUtf8("btnSalvar"))
        #CLICK BOTAO SALVAR
        self.btnSalvar.clicked.connect(lambda: self.btnSalvar_Click(estado, codigoCli))

        self.retranslateUi(frmCliente)
        QtCore.QMetaObject.connectSlotsByName(frmCliente)

    def retranslateUi(self, frmCliente):
        frmCliente.setWindowTitle(_translate("frmCliente", "Cadastro de Cliente", None))
        self.label.setText(_translate("frmCliente", "Nome", None))
        self.label_2.setText(_translate("frmCliente", "CPF", None))
        self.lbEndereco.setText(_translate("frmCliente", "Endereço", None))
        self.lbEmail.setText(_translate("frmCliente", "EMail", None))
        self.label_5.setText(_translate("frmCliente", "Telefone", None))
        self.btnSalvar.setText(_translate("frmCliente", "Salvar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    frmCliente = QtGui.QWidget()
    ui = Ui_frmCliente()
    ui.setupUi(frmCliente)
    frmCliente.show()
    sys.exit(app.exec_())

