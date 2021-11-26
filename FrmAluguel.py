from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from Controller.AluguelCTR import AluguelCTR
from Controller.ClienteCTR import ClienteCTR
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

class Ui_FrmAluguel(object):
    #CLICK BTN_SALVAR
    def btnSalvar_Click(self):
        linha = self.gridCliente.currentItem().row()
        codigoCli = self.gridCliente.item(linha, 0).text()
        linha = self.gridVeiculo.currentItem().row()
        codigoVeic = self.gridVeiculo.item(linha, 0).text()

        DataAluguel = self.EdtDataAluguel.text()
        DataPrazo = self.EdtPrazo.text()
        DataDevolucao = self.EdtDataDev.text()
        ValorAluguel = self.EdtValor.text()
        ValorMulta = self.EdtMulta.text()
        KmEntrada = self.EdtkmEntrada.text()
        KmSaida = self.EdtKmSaida.text()

        aluguel = AluguelCTR
        aluguel.CadastrarAluguel(DataAluguel, DataPrazo, DataDevolucao, ValorAluguel,
                      ValorMulta, KmEntrada, KmSaida, codigoCli, codigoVeic)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Aluguel cadastrado com sucesso!")
        msg.setWindowTitle("Cadastro de  Aluguel")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

        self.EdtDataAluguel.setText('')
        self.EdtPrazo.setText('')
        self.EdtDataDev.setText('')
        self.EdtValor.setText('')
        self.EdtMulta.setText('')
        self.EdtkmEntrada.setText('')
        self.EdtKmSaida.setText('')


    def PesquisarTodosClientes(self):
        cliente = ClienteCTR
        query = cliente.PesquisarTodosClientes()

        while (self.gridCliente.rowCount() > 0):
                self.gridCliente.removeRow(0)

        row = 0
        while query.next():
            self.gridCliente.insertRow(row)
            codCli = QTableWidgetItem(str(query.value(0)))
            nome = QTableWidgetItem(str(query.value(1)))
            cpf = QTableWidgetItem(str(query.value(2)))
            endereco = QTableWidgetItem(str(query.value(3)))
            email = QTableWidgetItem(str(query.value(4)))
            telefone = QTableWidgetItem(str(query.value(5)))

            self.gridCliente.setItem(row, 0, codCli)
            self.gridCliente.setItem(row, 1, nome)
            self.gridCliente.setItem(row, 2, cpf)
            self.gridCliente.setItem(row, 3, endereco)
            self.gridCliente.setItem(row, 4, email)
            self.gridCliente.setItem(row, 5, telefone)

            row = row + 1

    def PesquisarCliente(self, valor, tipo):
        if valor == '':
            self.PesquisarTodosClientes()
        else:
            cliente = ClienteCTR
            query = cliente.PesquisarCliente(valor, tipo)

            while (self.gridCliente.rowCount() > 0):
                self.gridCliente.removeRow(0)

            row = 0
            while query.next():
                self.gridCliente.insertRow(row)
                codCli = QTableWidgetItem(str(query.value(0)))
                nome = QTableWidgetItem(str(query.value(1)))
                cpf = QTableWidgetItem(str(query.value(2)))
                endereco = QTableWidgetItem(str(query.value(3)))
                email = QTableWidgetItem(str(query.value(4)))
                telefone = QTableWidgetItem(str(query.value(5)))

                self.gridCliente.setItem(row, 0, codCli)
                self.gridCliente.setItem(row, 1, nome)
                self.gridCliente.setItem(row, 2, cpf)
                self.gridCliente.setItem(row, 3, endereco)
                self.gridCliente.setItem(row, 4, email)
                self.gridCliente.setItem(row, 5, telefone)

                row = row + 1

    def PesquisarVeiculo(self, valor, tipo):
        if (valor == '') :
            self.PesquisarVeiculosDisponiveis()
        else:
            veiculo = VeiculoCTR
            query = veiculo.PesquisarVeiculo(valor, tipo)

            while (self.gridVeiculo.rowCount() > 0):
                self.gridVeiculo.removeRow(0)

            row = 0
            while query.next():
                self.gridVeiculo.insertRow(row)
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

                self.gridVeiculo.setItem(row, 0, codigoVeic)
                self.gridVeiculo.setItem(row, 1, modelo)
                self.gridVeiculo.setItem(row, 2, marca)
                self.gridVeiculo.setItem(row, 3, anoModelo)
                self.gridVeiculo.setItem(row, 4, placa)
                self.gridVeiculo.setItem(row, 5, alugado)
                self.gridVeiculo.setItem(row, 6, batido)
                self.gridVeiculo.setItem(row, 7, kmAtual)
                self.gridVeiculo.setItem(row, 8, valorDiaria)
                self.gridVeiculo.setItem(row, 9, descricao)
                self.gridVeiculo.setItem(row, 10, tipoVeiculo)

                row = row + 1

    def PesquisarVeiculosDisponiveis(self):
        veiculo = VeiculoCTR
        query = veiculo.PesquisarVeiculosDisponiveis()

        while (self.gridVeiculo.rowCount() > 0):
                self.gridVeiculo.removeRow(0)

        row = 0
        while query.next():
            self.gridVeiculo.insertRow(row)
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

            self.gridVeiculo.setItem(row, 0, codigoVeic)
            self.gridVeiculo.setItem(row, 1, modelo)
            self.gridVeiculo.setItem(row, 2, marca)
            self.gridVeiculo.setItem(row, 3, anoModelo)
            self.gridVeiculo.setItem(row, 4, placa)
            self.gridVeiculo.setItem(row, 5, alugado)
            self.gridVeiculo.setItem(row, 6, batido)
            self.gridVeiculo.setItem(row, 7, kmAtual)
            self.gridVeiculo.setItem(row, 8, valorDiaria)
            self.gridVeiculo.setItem(row, 9, descricao)
            self.gridVeiculo.setItem(row, 10, tipoVeiculo)

            row = row + 1

    def setupUi(self, FrmAluguel):
        FrmAluguel.setObjectName(_fromUtf8("FrmAluguel"))
        FrmAluguel.setFixedSize(521, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Imagens/btnAlugaVeiculo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrmAluguel.setWindowIcon(icon)
        self.groupBox = QtGui.QGroupBox(FrmAluguel)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 501, 60))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))

        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(140, 10, 91, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(260, 10, 101, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(380, 10, 71, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 60, 71, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(140, 60, 81, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(260, 60, 91, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        self.EdtDataAluguel = QtGui.QLineEdit(self.groupBox)
        self.EdtDataAluguel.setGeometry(QtCore.QRect(20, 30, 111, 20))
        self.EdtDataAluguel.setObjectName(_fromUtf8("EdtDataAluguel"))

        self.EdtPrazo = QtGui.QLineEdit(self.groupBox)
        self.EdtPrazo.setGeometry(QtCore.QRect(140, 30, 113, 20))
        self.EdtPrazo.setObjectName(_fromUtf8("EdtPrazo"))

        self.EdtDataDev = QtGui.QLineEdit(self.groupBox)
        self.EdtDataDev.setGeometry(QtCore.QRect(140, 80, 113, 20)) #(260, 30, 113, 20)
        self.EdtDataDev.setObjectName(_fromUtf8("EdtDataDev"))
        self.EdtDataDev.setDisabled(True)

        self.EdtValor = QtGui.QLineEdit(self.groupBox)
        self.EdtValor.setGeometry(QtCore.QRect(260, 30, 113, 20))# (380, 30, 113, 20)
        self.EdtValor.setObjectName(_fromUtf8("EdtValor"))

        self.EdtMulta = QtGui.QLineEdit(self.groupBox)
        self.EdtMulta.setGeometry(QtCore.QRect(20, 80, 113, 20))
        self.EdtMulta.setObjectName(_fromUtf8("EdtMulta"))
        self.EdtMulta.setDisabled(True)

        self.EdtkmEntrada = QtGui.QLineEdit(self.groupBox)
        self.EdtkmEntrada.setGeometry(QtCore.QRect(380, 30, 113, 20)) #(140, 80, 113, 20)
        self.EdtkmEntrada.setObjectName(_fromUtf8("EdtkmEntrada"))

        self.EdtKmSaida = QtGui.QLineEdit(self.groupBox)
        self.EdtKmSaida.setGeometry(QtCore.QRect(260, 80, 113, 20))
        self.EdtKmSaida.setObjectName(_fromUtf8("EdtKmSaida"))
        self.EdtKmSaida.setDisabled(True)

        self.groupBox_2 = QtGui.QGroupBox(FrmAluguel)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 70, 501, 171))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.cbPesqCliente = QtGui.QComboBox(self.groupBox_2)
        self.cbPesqCliente.setGeometry(QtCore.QRect(10, 40, 111, 22))
        self.cbPesqCliente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cbPesqCliente.setObjectName(_fromUtf8("cbPesqCliente"))
        self.cbPesqCliente.addItem(_fromUtf8(""))
        self.cbPesqCliente.addItem(_fromUtf8(""))
        self.cbPesqCliente.addItem(_fromUtf8(""))
        self.EdtPesqCliente = QtGui.QLineEdit(self.groupBox_2)
        self.EdtPesqCliente.setGeometry(QtCore.QRect(130, 40, 261, 20))
        self.EdtPesqCliente.setObjectName(_fromUtf8("EdtPesqCliente"))

        #BTN PESQ CLIENTE
        self.btnPesqCliente = QtGui.QPushButton(self.groupBox_2)
        self.btnPesqCliente.setGeometry(QtCore.QRect(400, 30, 91, 31))
        self.btnPesqCliente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Imagens/lupa.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesqCliente.setIcon(icon1)
        self.btnPesqCliente.setIconSize(QtCore.QSize(30, 30))
        self.btnPesqCliente.setObjectName(_fromUtf8("btnPesqCliente"))
        #BTN PESQ CLIENTE CLICK
        self.btnPesqCliente.clicked.connect(lambda: self.PesquisarCliente(self.EdtPesqCliente.text(), self.cbPesqCliente.currentText()))

        #GRID CLIENTE
        self.gridCliente = QtGui.QTableWidget(self.groupBox_2)
        self.gridCliente.setGeometry(QtCore.QRect(10, 70, 481, 96))
        self.gridCliente.setObjectName(_fromUtf8("gridCliente"))
        self.gridCliente.setColumnCount(6)
        self.gridCliente.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.gridCliente.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.gridCliente.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.gridCliente.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.gridCliente.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.gridCliente.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.gridCliente.setHorizontalHeaderItem(5, item)
        #AJUSTANDO MODO DE SELEÇÃO - Uma linha por vez, desalitar editar
        self.gridCliente.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.gridCliente.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.gridCliente.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)


        self.groupBox_3 = QtGui.QGroupBox(FrmAluguel)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 250, 501, 171))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.cbPesqVeic = QtGui.QComboBox(self.groupBox_3)

        #cb Pesquisar Veiculo
        self.cbPesqVeic.setGeometry(QtCore.QRect(10, 40, 111, 22))
        self.cbPesqVeic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cbPesqVeic.setObjectName(_fromUtf8("cbPesqVeic"))
        self.cbPesqVeic.addItem(_fromUtf8(""))
        self.cbPesqVeic.addItem(_fromUtf8(""))
        self.cbPesqVeic.addItem(_fromUtf8(""))
        #self.cbPesqVeic.addItem(_fromUtf8(""))
        #self.cbPesqVeic.addItem(_fromUtf8(""))
        self.EdtPesqVeiculo = QtGui.QLineEdit(self.groupBox_3)
        self.EdtPesqVeiculo.setGeometry(QtCore.QRect(130, 40, 261, 20))
        self.EdtPesqVeiculo.setObjectName(_fromUtf8("EdtPesqVeiculo"))

        #BTN PESQUISAR VEICULO
        self.btnPesqVeic = QtGui.QPushButton(self.groupBox_3)
        self.btnPesqVeic.setGeometry(QtCore.QRect(400, 30, 91, 31))
        self.btnPesqVeic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPesqVeic.setIcon(icon1)
        self.btnPesqVeic.setIconSize(QtCore.QSize(30, 30))
        self.btnPesqVeic.setObjectName(_fromUtf8("btnPesqVeic"))
        #BTN PESQ VEIC CLICK
        self.btnPesqVeic.clicked.connect(lambda: self.PesquisarVeiculo(self.EdtPesqVeiculo.text(), self.cbPesqVeic.currentText()))

        #GRID VEICULO
        self.gridVeiculo = QtGui.QTableWidget(self.groupBox_3)
        self.gridVeiculo.setGeometry(QtCore.QRect(10, 70, 481, 96))
        self.gridVeiculo.setObjectName(_fromUtf8("gridVeiculo"))
        self.gridVeiculo.setColumnCount(11)
        self.gridVeiculo.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.gridVeiculo.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.gridVeiculo.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.gridVeiculo.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.gridVeiculo.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.gridVeiculo.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.gridVeiculo.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.gridVeiculo.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.gridVeiculo.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.gridVeiculo.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.gridVeiculo.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.gridVeiculo.setHorizontalHeaderItem(10, item)
        #AJUSTANDO MODO DE SELEÇÃO - Uma linha por vez, desalitar editar
        self.gridVeiculo.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.gridVeiculo.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.gridVeiculo.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)

        #BTN SALVAR
        self.btnSalvar = QtGui.QPushButton(FrmAluguel)
        self.btnSalvar.setGeometry(QtCore.QRect(430, 430, 81, 61))
        self.btnSalvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Imagens/save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalvar.setIcon(icon2)
        self.btnSalvar.setIconSize(QtCore.QSize(30, 30))
        self.btnSalvar.setObjectName(_fromUtf8("btnSalvar"))
        #BTN SALVAR CLICK
        self.btnSalvar.clicked.connect(lambda: self.btnSalvar_Click())

        self.retranslateUi(FrmAluguel)
        QtCore.QMetaObject.connectSlotsByName(FrmAluguel)

        self.PesquisarTodosClientes()
        self.PesquisarVeiculosDisponiveis()

    def retranslateUi(self, FrmAluguel):
        FrmAluguel.setWindowTitle(_translate("FrmAluguel", "Aluguel de Veículos", None))
        self.label.setText(_translate("FrmAluguel", "Data do Aluguel", None))
        self.label_2.setText(_translate("FrmAluguel", "Prazo de Entrega", None))
        self.label_3.setText(_translate("FrmAluguel", "Valor Aluguel", None))
        self.label_4.setText(_translate("FrmAluguel", "Km de Entrada", None))
        self.label_5.setText(_translate("FrmAluguel", "Valor Multa", None))
        self.label_6.setText(_translate("FrmAluguel", "Km de Entrada", None))
        self.label_7.setText(_translate("FrmAluguel", "Km de Saída", None))
        self.groupBox_2.setTitle(_translate("FrmAluguel", "Selecione o Cliente", None))
        self.label_8.setText(_translate("FrmAluguel", "Tipo de Pesquisa", None))
        self.cbPesqCliente.setItemText(0, _translate("FrmAluguel", "Código", None))
        self.cbPesqCliente.setItemText(1, _translate("FrmAluguel", "Nome", None))
        self.cbPesqCliente.setItemText(2, _translate("FrmAluguel", "CPF", None))
        self.btnPesqCliente.setText(_translate("FrmAluguel", "Pesquisar", None))
        item = self.gridCliente.horizontalHeaderItem(0)
        item.setText(_translate("FrmAluguel", "Código", None))
        item = self.gridCliente.horizontalHeaderItem(1)
        item.setText(_translate("FrmAluguel", "Nome", None))
        item = self.gridCliente.horizontalHeaderItem(2)
        item.setText(_translate("FrmAluguel", "CPF", None))
        item = self.gridCliente.horizontalHeaderItem(3)
        item.setText(_translate("FrmAluguel", "Endereço", None))
        item = self.gridCliente.horizontalHeaderItem(4)
        item.setText(_translate("FrmAluguel", "Email", None))
        item = self.gridCliente.horizontalHeaderItem(5)
        item.setText(_translate("FrmAluguel", "Telefone", None))
        self.groupBox_3.setTitle(_translate("FrmAluguel", "Veículos Disponíveis", None))
        self.label_9.setText(_translate("FrmAluguel", "Tipo de Pesquisa", None))
        self.cbPesqVeic.setItemText(0, _translate("FrmAluguel", "Código", None))
        self.cbPesqVeic.setItemText(1, _translate("FrmAluguel", "Marca", None))
        self.cbPesqVeic.setItemText(2, _translate("FrmAluguel", "Modelo", None))
        #self.cbPesqVeic.setItemText(3, _translate("FrmAluguel", "Disponível", None))
        #self.cbPesqVeic.setItemText(4, _translate("FrmAluguel", "Alugado", None))
        self.btnPesqVeic.setText(_translate("FrmAluguel", "Pesquisar", None))
        item = self.gridVeiculo.horizontalHeaderItem(0)
        item.setText(_translate("FrmAluguel", "Código", None))
        item = self.gridVeiculo.horizontalHeaderItem(1)
        item.setText(_translate("FrmAluguel", "Modelo", None))
        item = self.gridVeiculo.horizontalHeaderItem(2)
        item.setText(_translate("FrmAluguel", "Marca", None))
        item = self.gridVeiculo.horizontalHeaderItem(3)
        item.setText(_translate("FrmAluguel", "Ano", None))
        item = self.gridVeiculo.horizontalHeaderItem(4)
        item.setText(_translate("FrmAluguel", "Placa", None))
        item = self.gridVeiculo.horizontalHeaderItem(5)
        item.setText(_translate("FrmAluguel", "Alugado", None))
        item = self.gridVeiculo.horizontalHeaderItem(6)
        item.setText(_translate("FrmAluguel", "Batido", None))
        item = self.gridVeiculo.horizontalHeaderItem(7)
        item.setText(_translate("FrmAluguel", "Km Atual", None))
        item = self.gridVeiculo.horizontalHeaderItem(8)
        item.setText(_translate("FrmAluguel", "Valor Diária", None))
        item = self.gridVeiculo.horizontalHeaderItem(9)
        item.setText(_translate("FrmAluguel", "Descrição", None))
        item = self.gridVeiculo.horizontalHeaderItem(10)
        item.setText(_translate("FrmAluguel", "Tipo", None))
        self.btnSalvar.setText(_translate("FrmAluguel", "Salvar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FrmAluguel = QtGui.QDialog()
    ui = Ui_FrmAluguel()
    ui.setupUi(FrmAluguel)
    FrmAluguel.show()
    sys.exit(app.exec_())

