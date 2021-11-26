from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from Controller.VeiculoCTR import VeiculoCTR

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

class Ui_frmVeiculos(object):
    #PREENCHER OS CAMPOS PARA ALTERAÇÃO
    def PreencherAlterar(self, modelo, marca, anoModelo, placa, alugado, batido, kmAtual, valorDiaria, descricao, tipoVeiculo):
        self.edtModelo.setText(modelo)
        self.edtMarca.setText(marca)
        self.edtAno.setText(anoModelo)
        self.edtPlaca.setText(placa)
        self.edtKm.setText(kmAtual)
        self.edtDiaria.setText(valorDiaria)
        self.txtDescricao.setPlainText(descricao)
        self.edtTipo.setText(tipoVeiculo)

        if alugado=='Sim':
            self.rbAlugado.setChecked(True)
            self.rbDisponivel.setChecked(False)
        elif alugado=='Não':
            self.rbDisponivel.setChecked(True)
            self.rbAlugado.setChecked(False)

        if batido=='Sim':
            self.rbBatido.setChecked(True)
            self.rbPerfeito.setChecked(False)
        elif batido=='Não':
            self.rbPerfeito.setChecked(True)
            self.rbBatido.setChecked(False)


    #CLICK BTN_SALVAR
    def btnSalvar_Click(self, estado, codigoVeic):
        modelo = self.edtModelo.text()
        marca = self.edtMarca.text()
        anoModelo = self.edtAno.text()
        placa = self.edtPlaca.text()

        if self.rbAlugado.isChecked():
            alugado = self.rbAlugado.text()
        elif self.rbDisponivel.isChecked():
            alugado = self.rbDisponivel.text()

        if self.rbBatido.isChecked():
            batido = self.rbBatido.text()
        elif self.rbPerfeito.isChecked():
            batido = self.rbPerfeito.text()

        kmAtual = self.edtKm.text()
        valorDiaria = self.edtDiaria.text()
        descricao = self.txtDescricao.toPlainText()
        tipoVeiculo = self.edtTipo.text()


        #VERIFICA O ESTADO INSERIR/ALTERAR PARA CHAMAR A FUNÇAO APROPRIADA
        if estado=='inserir':
            veiculo = VeiculoCTR
            veiculo.CadastrarVeiculo(modelo, marca, anoModelo, placa, alugado,
                                     batido, kmAtual, valorDiaria, descricao, tipoVeiculo)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Veículo inserido com sucesso!")
            #msg.setInformativeText("This is additional information")
            msg.setWindowTitle("Inserir Veículo")
            #msg.setDetailedText("The details are as follows:")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        if estado=='alterar':
            veiculo = VeiculoCTR
            veiculo.AtualizarVeiculo(codigoVeic, modelo, marca, anoModelo, placa, alugado,
                                     batido, kmAtual, valorDiaria, descricao, tipoVeiculo)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Veículo alterado com sucesso!")
            #msg.setInformativeText("This is additional information")
            msg.setWindowTitle("Alterar Veículo")
            #msg.setDetailedText("The details are as follows:")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        self.edtModelo.setText('')
        self.edtMarca.setText('')
        self.edtAno.setText('')
        self.edtPlaca.setText('')
        self.edtKm.setText('')
        self.edtDiaria.setText('')
        self.txtDescricao.setText('')
        self.edtTipo.setText('')

    def setupUi(self, frmVeiculos, estado, codigoVeic):
        frmVeiculos.setObjectName(_fromUtf8("frmVeiculos"))

        #DESABILITAR REDIMENCIONAMENTO DA JANELA
        frmVeiculos.setFixedSize(543, 318)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Imagens/FrmIcon_Car.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmVeiculos.setWindowIcon(icon)
        self.groupBox = QtGui.QGroupBox(frmVeiculos)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 521, 211))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 10, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(220, 10, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lbEndereco = QtGui.QLabel(self.groupBox)
        self.lbEndereco.setGeometry(QtCore.QRect(220, 60, 51, 16))
        self.lbEndereco.setObjectName(_fromUtf8("lbEndereco"))
        self.lbEmail = QtGui.QLabel(self.groupBox)
        self.lbEmail.setGeometry(QtCore.QRect(420, 10, 46, 13))
        self.lbEmail.setObjectName(_fromUtf8("lbEmail"))
        self.edtModelo = QtGui.QLineEdit(self.groupBox)
        self.edtModelo.setGeometry(QtCore.QRect(10, 30, 201, 20))
        self.edtModelo.setObjectName(_fromUtf8("edtModelo"))
        self.edtMarca = QtGui.QLineEdit(self.groupBox)
        self.edtMarca.setGeometry(QtCore.QRect(220, 30, 191, 20))
        self.edtMarca.setObjectName(_fromUtf8("edtMarca"))
        self.edtAno = QtGui.QLineEdit(self.groupBox)
        self.edtAno.setGeometry(QtCore.QRect(420, 80, 91, 20))
        self.edtAno.setObjectName(_fromUtf8("edtAno"))
        self.edtKm = QtGui.QLineEdit(self.groupBox)
        self.edtKm.setGeometry(QtCore.QRect(220, 80, 91, 20))
        self.edtKm.setObjectName(_fromUtf8("edtKm"))
        self.edtDiaria = QtGui.QLineEdit(self.groupBox)
        self.edtDiaria.setGeometry(QtCore.QRect(320, 80, 91, 20))
        self.edtDiaria.setObjectName(_fromUtf8("edtDiaria"))
        self.edtTipo = QtGui.QLineEdit(self.groupBox)
        self.edtTipo.setGeometry(QtCore.QRect(10, 80, 201, 20))
        self.edtTipo.setObjectName(_fromUtf8("edtTipo"))
        self.edtPlaca = QtGui.QLineEdit(self.groupBox)
        self.edtPlaca.setGeometry(QtCore.QRect(420, 30, 91, 20))
        self.edtPlaca.setObjectName(_fromUtf8("edtPlaca"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(420, 60, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 120, 81, 80))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.rbAlugado = QtGui.QRadioButton(self.groupBox_3)
        self.rbAlugado.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.rbAlugado.setObjectName(_fromUtf8("rbAlugado"))
        self.rbDisponivel = QtGui.QRadioButton(self.groupBox_3)
        self.rbDisponivel.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.rbDisponivel.setObjectName(_fromUtf8("rbDisponivel"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(100, 120, 81, 80))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.rbBatido = QtGui.QRadioButton(self.groupBox_4)
        self.rbBatido.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.rbBatido.setObjectName(_fromUtf8("rbBatido"))
        self.rbPerfeito = QtGui.QRadioButton(self.groupBox_4)
        self.rbPerfeito.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.rbPerfeito.setObjectName(_fromUtf8("rbPerfeito"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(320, 60, 81, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(200, 120, 46, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 91, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.txtDescricao = QtGui.QTextEdit(self.groupBox)
        self.txtDescricao.setGeometry(QtCore.QRect(200, 140, 311, 61))
        self.txtDescricao.setObjectName(_fromUtf8("txtDescricao"))
        self.groupBox_2 = QtGui.QGroupBox(frmVeiculos)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 230, 521, 81))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))

        #BTN SALVAR
        self.btnSalvar = QtGui.QPushButton(self.groupBox_2)
        self.btnSalvar.setGeometry(QtCore.QRect(400, 10, 101, 61))
        self.btnSalvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Imagens/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalvar.setIcon(icon1)
        self.btnSalvar.setIconSize(QtCore.QSize(35, 35))
        self.btnSalvar.setObjectName(_fromUtf8("btnSalvar"))
        #btn salvar click
        self.btnSalvar.clicked.connect(lambda: self.btnSalvar_Click(estado, codigoVeic))

        self.retranslateUi(frmVeiculos)
        QtCore.QMetaObject.connectSlotsByName(frmVeiculos)

    def retranslateUi(self, frmVeiculos):
        frmVeiculos.setWindowTitle(_translate("frmVeiculos", "Cadastro de Veículos", None))
        self.label.setText(_translate("frmVeiculos", "Modelo", None))
        self.label_2.setText(_translate("frmVeiculos", "Marca", None))
        self.lbEndereco.setText(_translate("frmVeiculos", "KM Atual", None))
        self.lbEmail.setText(_translate("frmVeiculos", "Placa", None))
        self.label_3.setText(_translate("frmVeiculos", "Ano", None))
        self.groupBox_3.setTitle(_translate("frmVeiculos", "Alugado", None))
        self.rbAlugado.setText(_translate("frmVeiculos", "Sim", None))
        self.rbDisponivel.setText(_translate("frmVeiculos", "Não", None))
        self.groupBox_4.setTitle(_translate("frmVeiculos", "Batido", None))
        self.rbBatido.setText(_translate("frmVeiculos", "Sim", None))
        self.rbPerfeito.setText(_translate("frmVeiculos", "Não", None))
        self.label_4.setText(_translate("frmVeiculos", "Valor da Diária", None))
        self.label_5.setText(_translate("frmVeiculos", "Descrição", None))
        self.label_6.setText(_translate("frmVeiculos", "Tipo de Veículo", None))
        self.btnSalvar.setText(_translate("frmVeiculos", "Salvar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    frmVeiculos = QtGui.QWidget()
    ui = Ui_frmVeiculos()
    ui.setupUi(frmVeiculos)
    frmVeiculos.show()
    sys.exit(app.exec_())

