from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from Controller.VeiculoCTR import VeiculoCTR
from View.FrmVeiculos import Ui_frmVeiculos

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

class Ui_frmPesqVeiculos(object):
    def AlterarVeiculo_Click(self):
        linha = self.gridVeiculos.currentItem().row()
        codigoVeic = self.gridVeiculos.item(linha, 0).text()
        modelo = self.gridVeiculos.item(linha, 1).text()
        marca = self.gridVeiculos.item(linha, 2).text()
        anoModelo = self.gridVeiculos.item(linha, 3).text()
        placa = self.gridVeiculos.item(linha, 4).text()
        alugado = self.gridVeiculos.item(linha, 5).text()
        batido = self.gridVeiculos.item(linha, 6).text()
        kmAtual = self.gridVeiculos.item(linha, 7).text()
        valorDiaria = self.gridVeiculos.item(linha, 8).text()
        descricao = self.gridVeiculos.item(linha, 9).text()
        tipoVeiculo = self.gridVeiculos.item(linha, 10).text()

        self.frmVeiculos = QtGui.QMainWindow()
        self.ui = Ui_frmVeiculos()
        self.ui.setupUi(self.frmVeiculos, 'alterar', codigoVeic)
        self.ui.PreencherAlterar(modelo, marca, anoModelo, placa, alugado, batido, kmAtual, valorDiaria, descricao, tipoVeiculo)
        self.frmVeiculos.show()

    def ExcluirVeiculo_Click(self):

        linha = self.gridVeiculos.currentItem().row()
        codigoVeic = self.gridVeiculos.item(linha, 0).text()

        self.gridVeiculos.removeRow(linha)
        veiculo = VeiculoCTR
        veiculo.ExcluirVeiculo(codigoVeic)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Veículo Excluído!")
        #msg.setInformativeText("This is additional information")
        msg.setWindowTitle("Excluir Veículo")
        #msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


    def PesquisarVeiculo(self, valor, tipo):
        if (valor == '') and (tipo!='Disponível') and (tipo!='Alugado'):
            self.PesquisarTodosVeiculos()
        else:
            veiculo = VeiculoCTR
            query = veiculo.PesquisarVeiculo(valor, tipo)

            while (self.gridVeiculos.rowCount() > 0):
                self.gridVeiculos.removeRow(0)

            row = 0
            while query.next():
                self.gridVeiculos.insertRow(row)
                codigoVeic = QTableWidgetItem(str(query.value(0)))
                modelo = QTableWidgetItem(str(query.value(1)))
                marca = QTableWidgetItem(str(query.value(2)))
                anoModelo = QTableWidgetItem(str(query.value(3)))
                placa = QTableWidgetItem(str(query.value(4)))
                alugado = QTableWidgetItem(str(query.value(5)))
                batido = QTableWidgetItem(str(query.value(6)))
                kmAtual = QTableWidgetItem(str(query.value(7)))
                valorDiaria = QTableWidgetItem(str(query.value(8)))
                descricao = QTableWidgetItem(str(query.value(9)))
                tipoVeiculo = QTableWidgetItem(str(query.value(10)))

                self.gridVeiculos.setItem(row, 0, codigoVeic)
                self.gridVeiculos.setItem(row, 1, modelo)
                self.gridVeiculos.setItem(row, 2, marca)
                self.gridVeiculos.setItem(row, 3, anoModelo)
                self.gridVeiculos.setItem(row, 4, placa)
                self.gridVeiculos.setItem(row, 5, alugado)
                self.gridVeiculos.setItem(row, 6, batido)
                self.gridVeiculos.setItem(row, 7, kmAtual)
                self.gridVeiculos.setItem(row, 8, valorDiaria)
                self.gridVeiculos.setItem(row, 9, descricao)
                self.gridVeiculos.setItem(row, 10, tipoVeiculo)

                row = row + 1

        self.edtPesquisa.setText('')

    def PesquisarTodosVeiculos(self):
        veiculo = VeiculoCTR
        query = veiculo.PesquisarTodosVeiculos()

        while (self.gridVeiculos.rowCount() > 0):
                self.gridVeiculos.removeRow(0)

        row = 0
        while query.next():
            self.gridVeiculos.insertRow(row)
            codigoVeic = QTableWidgetItem(str(query.value(0)))
            modelo = QTableWidgetItem(str(query.value(1)))
            marca = QTableWidgetItem(str(query.value(2)))
            anoModelo = QTableWidgetItem(str(query.value(3)))
            placa = QTableWidgetItem(str(query.value(4)))
            alugado = QTableWidgetItem(str(query.value(5)))
            batido = QTableWidgetItem(str(query.value(6)))
            kmAtual = QTableWidgetItem(str(query.value(7)))
            valorDiaria = QTableWidgetItem(str(query.value(8)))
            descricao = QTableWidgetItem(str(query.value(9)))
            tipoVeiculo = QTableWidgetItem(str(query.value(10)))

            self.gridVeiculos.setItem(row, 0, codigoVeic)
            self.gridVeiculos.setItem(row, 1, modelo)
            self.gridVeiculos.setItem(row, 2, marca)
            self.gridVeiculos.setItem(row, 3, anoModelo)
            self.gridVeiculos.setItem(row, 4, placa)
            self.gridVeiculos.setItem(row, 5, alugado)
            self.gridVeiculos.setItem(row, 6, batido)
            self.gridVeiculos.setItem(row, 7, kmAtual)
            self.gridVeiculos.setItem(row, 8, valorDiaria)
            self.gridVeiculos.setItem(row, 9, descricao)
            self.gridVeiculos.setItem(row, 10, tipoVeiculo)

            row = row + 1

    def setupUi(self, frmPesqVeiculos):
        frmPesqVeiculos.setObjectName(_fromUtf8("frmPesqVeiculos"))

        #DESABILITAR REDIMENCIONAMENTO DA JANELA
        frmPesqVeiculos.setFixedSize(820, 504)

        #GRID VEICULOS
        self.gridVeiculos = QtGui.QTableWidget(frmPesqVeiculos)
        self.gridVeiculos.setGeometry(QtCore.QRect(10, 150, 800, 291))
        self.gridVeiculos.setObjectName(_fromUtf8("gridVeiculos"))
        self.gridVeiculos.setColumnCount(11)
        self.gridVeiculos.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(10, item)
        #AJUSTANDO MODO DE SELEÇÃO - Uma linha por vez, desalitar editar
        self.gridVeiculos.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.gridVeiculos.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.gridVeiculos.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)

        #EDT PESQUISAR#########3
        self.edtPesquisa = QtGui.QLineEdit(frmPesqVeiculos)
        self.edtPesquisa.setGeometry(QtCore.QRect(190, 60, 621, 20))
        self.edtPesquisa.setObjectName(_fromUtf8("edtPesquisa"))
        self.cbPesquisa = QtGui.QComboBox(frmPesqVeiculos)
        self.cbPesquisa.setGeometry(QtCore.QRect(20, 60, 161, 22))
        self.cbPesquisa.setObjectName(_fromUtf8("cbPesquisa"))
        self.cbPesquisa.addItem(_fromUtf8(""))
        self.cbPesquisa.addItem(_fromUtf8(""))
        self.cbPesquisa.addItem(_fromUtf8(""))
        self.cbPesquisa.addItem(_fromUtf8(""))
        self.cbPesquisa.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(frmPesqVeiculos)
        self.label.setGeometry(QtCore.QRect(20, 30, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.btnPesquisar = QtGui.QPushButton(frmPesqVeiculos)
        self.btnPesquisar.setGeometry(QtCore.QRect(700, 90, 111, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Imagens/lupa.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        #BTN PESQUISAR #########
        self.btnPesquisar.setIcon(icon)
        self.btnPesquisar.setIconSize(QtCore.QSize(30, 30))
        self.btnPesquisar.setObjectName(_fromUtf8("btnPesquisar"))
        #BTN PESQUISAR CLICK #
        self.btnPesquisar.clicked.connect(lambda: self.PesquisarVeiculo(self.edtPesquisa.text(), self.cbPesquisa.currentText()))


        self.lblTotal = QtGui.QLabel(frmPesqVeiculos)
        self.lblTotal.setGeometry(QtCore.QRect(20, 450, 111, 16))
        self.lblTotal.setObjectName(_fromUtf8("lblTotal"))

        #BTN EXCLUIR#####
        self.btnExcluir = QtGui.QPushButton(frmPesqVeiculos)
        self.btnExcluir.setGeometry(QtCore.QRect(720, 450, 91, 51))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Imagens/excluir.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExcluir.setIcon(icon1)
        self.btnExcluir.setIconSize(QtCore.QSize(30, 30))
        self.btnExcluir.setObjectName(_fromUtf8("btnExcluir"))
        #BTN EXCLUIR CLICK
        self.btnExcluir.clicked.connect(lambda: self.ExcluirVeiculo_Click())

        #BTN ALTERAR
        self.btnAlterar = QtGui.QPushButton(frmPesqVeiculos)
        self.btnAlterar.setGeometry(QtCore.QRect(610, 450, 101, 51))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Imagens/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAlterar.setIcon(icon2)
        self.btnAlterar.setIconSize(QtCore.QSize(35, 35))
        self.btnAlterar.setObjectName(_fromUtf8("btnAlterar"))
        #BTN ALTERAR CLICK###
        self.btnAlterar.clicked.connect(lambda: self.AlterarVeiculo_Click())

        self.retranslateUi(frmPesqVeiculos)
        QtCore.QMetaObject.connectSlotsByName(frmPesqVeiculos)

        self.PesquisarTodosVeiculos()

    def retranslateUi(self, frmPesqVeiculos):
        frmPesqVeiculos.setWindowTitle(_translate("frmPesqVeiculos", "Lista de Veículo", None))
        item = self.gridVeiculos.horizontalHeaderItem(0)
        item.setText(_translate("frmPesqVeiculos", "Código", None))
        item = self.gridVeiculos.horizontalHeaderItem(1)
        item.setText(_translate("frmPesqVeiculos", "Modelo", None))
        item = self.gridVeiculos.horizontalHeaderItem(2)
        item.setText(_translate("frmPesqVeiculos", "Marca", None))
        item = self.gridVeiculos.horizontalHeaderItem(3)
        item.setText(_translate("frmPesqVeiculos", "Ano", None))
        item = self.gridVeiculos.horizontalHeaderItem(4)
        item.setText(_translate("frmPesqVeiculos", "Placa", None))
        item = self.gridVeiculos.horizontalHeaderItem(5)
        item.setText(_translate("frmPesqVeiculos", "Alugado", None))
        item = self.gridVeiculos.horizontalHeaderItem(6)
        item.setText(_translate("frmPesqVeiculos", "Batido", None))
        item = self.gridVeiculos.horizontalHeaderItem(7)
        item.setText(_translate("frmPesqVeiculos", "Quilometragem", None))
        item = self.gridVeiculos.horizontalHeaderItem(8)
        item.setText(_translate("frmPesqVeiculos", "Valor da Diária", None))
        item = self.gridVeiculos.horizontalHeaderItem(9)
        item.setText(_translate("frmPesqVeiculos", "Descrição", None))
        item = self.gridVeiculos.horizontalHeaderItem(10)
        item.setText(_translate("frmPesqVeiculos", "Tipo do Veículo", None))
        self.cbPesquisa.setItemText(0, _translate("frmPesqVeiculos", "Código", None))
        self.cbPesquisa.setItemText(1, _translate("frmPesqVeiculos", "Marca", None))
        self.cbPesquisa.setItemText(2, _translate("frmPesqVeiculos", "Modelo", None))
        self.cbPesquisa.setItemText(3, _translate("frmPesqVeiculos", "Disponível", None))
        self.cbPesquisa.setItemText(4, _translate("frmPesqVeiculos", "Alugado", None))
        self.label.setText(_translate("frmPesqVeiculos", "Selecione o Tipo de Pesquisa:", None))
        self.btnPesquisar.setText(_translate("frmPesqVeiculos", "Pesquisar", None))
        self.lblTotal.setText(_translate("frmPesqVeiculos", "TextLabel", None))
        self.btnExcluir.setText(_translate("frmPesqVeiculos", "Excluir", None))
        self.btnAlterar.setText(_translate("frmPesqVeiculos", "Alterar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    frmPesqVeiculos = QtGui.QDialog()
    ui = Ui_frmPesqVeiculos()
    ui.setupUi(frmPesqVeiculos)
    frmPesqVeiculos.show()
    sys.exit(app.exec_())

