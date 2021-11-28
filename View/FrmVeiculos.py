# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmVeiculos.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Controller.VeiculoCTR import VeiculoCTR

class Ui_frmVeiculos(object):
     #PREENCHER OS CAMPOS PARA ALTERAÇÃO
    def PreencherAlterar(self, modelo, marca, anoModelo, placa, alugado, kmAtual, valorDiaria, tipoVeiculo):
        self.edtModelo.setText(modelo)
        self.edtMarca.setText(marca)
        self.edtAno.setText(anoModelo)
        self.edtPlaca.setText(placa)
        self.edtKm.setText(kmAtual)
        self.edtDiaria.setText(valorDiaria)
        self.edtTipo.setText(tipoVeiculo)

        if alugado=='Sim':
            self.rbAlugado.setChecked(True)
            self.rbDisponivel.setChecked(False)
        elif alugado=='Não':
            self.rbDisponivel.setChecked(True)
            self.rbAlugado.setChecked(False)


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


        kmAtual = self.edtKm.text()
        valorDiaria = self.edtDiaria.text()
        
        tipoVeiculo = self.edtTipo.text()


        #VERIFICA O ESTADO INSERIR/ALTERAR PARA CHAMAR A FUNÇAO APROPRIADA
        if estado=='inserir':
            veiculo = VeiculoCTR
            veiculo.CadastrarVeiculo(modelo, marca, anoModelo, placa, alugado,
                                    kmAtual, valorDiaria, tipoVeiculo)

            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.information)
            msg.setText("Veículo inserido com sucesso!")
            msg.setWindowTitle("Inserir Veículo")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        if estado=='alterar':
            
            veiculo = VeiculoCTR
            veiculo.AtualizarVeiculo(codigoVeic, modelo, marca, anoModelo, placa, alugado,
                                     kmAtual, valorDiaria, tipoVeiculo)

            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.information)
            msg.setText("Veículo alterado com sucesso!")
            msg.setWindowTitle("Alterar Veículo")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()

        self.edtModelo.setText('')
        self.edtMarca.setText('')
        self.edtAno.setText('')
        self.edtPlaca.setText('')
        self.edtKm.setText('')
        self.edtDiaria.setText('')
        self.edtTipo.setText('')


    def setupUi(self, frmVeiculos, estado, codigoVeic):
        frmVeiculos.setObjectName("frmVeiculos")
        
        #desabilitar tamanho tela
        frmVeiculos.setFixedSize(543, 318)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../TesteProjeto/View/Imagens/btnCadCli.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmVeiculos.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(frmVeiculos)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 521, 211))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 10, 46, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(220, 10, 46, 13))
        self.label_2.setObjectName("label_2")
        self.lbEndereco = QtWidgets.QLabel(self.groupBox)
        self.lbEndereco.setGeometry(QtCore.QRect(220, 60, 51, 16))
        self.lbEndereco.setObjectName("lbEndereco")
        self.lbEmail = QtWidgets.QLabel(self.groupBox)
        self.lbEmail.setGeometry(QtCore.QRect(420, 10, 46, 13))
        self.lbEmail.setObjectName("lbEmail")
        self.edtModelo = QtWidgets.QLineEdit(self.groupBox)
        self.edtModelo.setGeometry(QtCore.QRect(10, 30, 201, 20))
        self.edtModelo.setObjectName("edtModelo")
        self.edtMarca = QtWidgets.QLineEdit(self.groupBox)
        self.edtMarca.setGeometry(QtCore.QRect(220, 30, 191, 20))
        self.edtMarca.setObjectName("edtMarca")
        self.edtAno = QtWidgets.QLineEdit(self.groupBox)
        self.edtAno.setGeometry(QtCore.QRect(420, 80, 91, 20))
        self.edtAno.setObjectName("edtAno")
        self.edtKm = QtWidgets.QLineEdit(self.groupBox)
        self.edtKm.setGeometry(QtCore.QRect(220, 80, 91, 20))
        self.edtKm.setObjectName("edtKm")
        self.edtDiaria = QtWidgets.QLineEdit(self.groupBox)
        self.edtDiaria.setGeometry(QtCore.QRect(320, 80, 91, 20))
        self.edtDiaria.setObjectName("edtDiaria")
        self.edtTipo = QtWidgets.QLineEdit(self.groupBox)
        self.edtTipo.setGeometry(QtCore.QRect(10, 80, 201, 20))
        self.edtTipo.setObjectName("edtTipo")
        self.edtPlaca = QtWidgets.QLineEdit(self.groupBox)
        self.edtPlaca.setGeometry(QtCore.QRect(420, 30, 91, 20))
        self.edtPlaca.setObjectName("edtPlaca")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(420, 60, 46, 13))
        self.label_3.setObjectName("label_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 120, 81, 80))
        self.groupBox_3.setObjectName("groupBox_3")
        self.rbAlugado = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbAlugado.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.rbAlugado.setObjectName("rbAlugado")
        self.rbDisponivel = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbDisponivel.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.rbDisponivel.setObjectName("rbDisponivel")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(320, 60, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 91, 16))
        self.label_6.setObjectName("label_6")
        self.groupBox_2 = QtWidgets.QGroupBox(frmVeiculos)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 230, 521, 81))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")

        #botão salvar
        self.btnSalvar = QtWidgets.QPushButton(self.groupBox_2)
        self.btnSalvar.setGeometry(QtCore.QRect(400, 10, 101, 61))
        self.btnSalvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../../../TesteProjeto/Imagens/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalvar.setIcon(icon1)
        self.btnSalvar.setIconSize(QtCore.QSize(35, 35))
        self.btnSalvar.setObjectName("btnSalvar")
        #botão salvar click
        self.btnSalvar.clicked.connect(lambda: self.btnSalvar_Click(estado, codigoVeic))

        self.retranslateUi(frmVeiculos)
        QtCore.QMetaObject.connectSlotsByName(frmVeiculos)

    def retranslateUi(self, frmVeiculos):
        _translate = QtCore.QCoreApplication.translate
        frmVeiculos.setWindowTitle(_translate("frmVeiculos", "Cadastro de Veículos", None))
        self.label.setText(_translate("frmVeiculos", "Modelo", None))
        self.label_2.setText(_translate("frmVeiculos", "Marca", None))
        self.lbEndereco.setText(_translate("frmVeiculos", "KM Atual", None))
        self.lbEmail.setText(_translate("frmVeiculos", "Placa", None))
        self.label_3.setText(_translate("frmVeiculos", "Ano", None))
        self.groupBox_3.setTitle(_translate("frmVeiculos", "Alugado", None))
        self.rbAlugado.setText(_translate("frmVeiculos", "Sim", None))
        self.rbDisponivel.setText(_translate("frmVeiculos", "Não", None))
        self.label_4.setText(_translate("frmVeiculos", "Valor da Diária", None))
        self.label_6.setText(_translate("frmVeiculos", "Tipo de Veículo", None))
        self.btnSalvar.setText(_translate("frmVeiculos", "Salvar", None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmVeiculos = QtWidgets.QWidget()
    ui = Ui_frmVeiculos()
    ui.setupUi(frmVeiculos)
    frmVeiculos.show()
    sys.exit(app.exec_())
