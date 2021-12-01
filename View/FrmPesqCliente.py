from PyQt5 import QtCore, QtGui, QtWidgets
from Controller.ClienteCTR import ClienteCTR
from View.FrmCliente import Ui_frmCliente



class Ui_frmPesqCliente(object):
    def AlterarCliente_Click(self):
        linha = self.gridCliente.currentItem().row()
        codigoCli = self.gridCliente.item(linha, 0).text()
        nome = self.gridCliente.item(linha, 1).text()
        cpf = self.gridCliente.item(linha, 2).text()
        endereco = self.gridCliente.item(linha, 3).text()
        email = self.gridCliente.item(linha, 4).text()
        telefone = self.gridCliente.item(linha, 5).text()

        self.frmCliente = QtWidgets.QMainWindow()
        self.ui = Ui_frmCliente()
        self.ui.setupUi(self.frmCliente, 'alterar', codigoCli)
        self.ui.PreencherAlterar(nome, cpf, endereco, email, telefone)
        self.frmCliente.show()

    
    def ExcluirCliente_Click(self):
        linha = self.gridCliente.currentItem().row()
        codigoCli = self.gridCliente.item(linha, 0).text()

        self.gridCliente.removeRow(linha)
        cliente = ClienteCTR
        cliente.ExcluirCliente(codigoCli)

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Cliente excluído!")
        msg.setWindowTitle('Excluir Cliente')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
    
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
                codCli = QtWidgets.QTableWidgetItem(str(query.value(0)))
                nome = QtWidgets.QTableWidgetItem(str(query.value(1)))
                cpf = QtWidgets.QTableWidgetItem(str(query.value(2)))
                endereco = QtWidgets.QTableWidgetItem(str(query.value(3)))
                email = QtWidgets.QTableWidgetItem(str(query.value(4)))
                telefone = QtWidgets.QTableWidgetItem(str(query.value(5)))

                self.gridCliente.setItem(row, 0, codCli)
                self.gridCliente.setItem(row, 1, nome)
                self.gridCliente.setItem(row, 2, cpf)
                self.gridCliente.setItem(row, 3, endereco)
                self.gridCliente.setItem(row, 4, email)
                self.gridCliente.setItem(row, 5, telefone)

                row = row + 1
        
        self.edtPesquisa.setText('')

    def PesquisarTodosClientes(self):
        cliente = ClienteCTR
        query = cliente.PesquisarTodosClientes()

        while (self.gridCliente.rowCount() > 0):
            self.gridCliente.removeRow(0)

        row = 0
        while query.next():
            self.gridCliente.insertRow(row)
            codCli = QtWidgets.QTableWidgetItem(str(query.value(0)))
            nome = QtWidgets.QTableWidgetItem(str(query.value(1)))
            cpf = QtWidgets.QTableWidgetItem(str(query.value(2)))
            endereco = QtWidgets.QTableWidgetItem(str(query.value(3)))
            email = QtWidgets.QTableWidgetItem(str(query.value(4)))
            telefone = QtWidgets.QTableWidgetItem(str(query.value(5)))

            self.gridCliente.setItem(row, 0, codCli)
            self.gridCliente.setItem(row, 1, nome)
            self.gridCliente.setItem(row, 2, cpf)
            self.gridCliente.setItem(row, 3, endereco)
            self.gridCliente.setItem(row, 4, email)
            self.gridCliente.setItem(row, 5, telefone)

            row = row + 1


    def setupUi(self, frmPesqCliente):
        
        frmPesqCliente.setObjectName("frmPesqCliente")

        #janela fixa
        frmPesqCliente.setFixedSize(651, 504)

        #grid cliente
        self.gridCliente = QtWidgets.QTableWidget(frmPesqCliente)
        self.gridCliente.setGeometry(QtCore.QRect(20, 150, 621, 291))
        self.gridCliente.setObjectName("gridCliente")
        self.gridCliente.setColumnCount(6)
        self.gridCliente.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.gridCliente.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridCliente.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridCliente.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridCliente.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridCliente.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridCliente.setHorizontalHeaderItem(5, item)
        #modo de seleção
        self.gridCliente.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.gridCliente.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.gridCliente.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)


        #edt pesquisar
        self.edtPesquisa = QtWidgets.QLineEdit(frmPesqCliente)
        self.edtPesquisa.setGeometry(QtCore.QRect(190, 60, 451, 20))
        self.edtPesquisa.setObjectName("edtPesquisa")
        self.cbPesquisa = QtWidgets.QComboBox(frmPesqCliente)
        self.cbPesquisa.setGeometry(QtCore.QRect(20, 60, 161, 22))
        self.cbPesquisa.setObjectName("cbPesquisa")
        self.cbPesquisa.addItem("")
        self.cbPesquisa.addItem("")
        self.cbPesquisa.addItem("")
        self.label = QtWidgets.QLabel(frmPesqCliente)
        self.label.setGeometry(QtCore.QRect(20, 30, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")

        #botão pesquisar
        self.btnPesquisar = QtWidgets.QPushButton(frmPesqCliente)
        self.btnPesquisar.setGeometry(QtCore.QRect(530, 92, 111, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".../../Imagens/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisar.setIcon(icon)
        self.btnPesquisar.setIconSize(QtCore.QSize(30, 30))
        self.btnPesquisar.setObjectName("btnPesquisar")
        #clickk
        self.btnPesquisar.clicked.connect(lambda: self.PesquisarCliente(self.edtPesquisa.text(), self.cbPesquisa.currentText()))

        self.lblTotal = QtWidgets.QLabel(frmPesqCliente)
        self.lblTotal.setGeometry(QtCore.QRect(20, 450, 111, 16))
        self.lblTotal.setObjectName("lblTotal")

        #botão excluir
        self.btnExcluir = QtWidgets.QPushButton(frmPesqCliente)
        self.btnExcluir.setGeometry(QtCore.QRect(554, 450, 91, 51))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".../../Imagens/delete-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExcluir.setIcon(icon1)
        self.btnExcluir.setIconSize(QtCore.QSize(30, 30))
        self.btnExcluir.setObjectName("btnExcluir")
        #clickk
        self.btnExcluir.clicked.connect(lambda: self.ExcluirCliente_Click())

        #botão alterar
        self.btnAlterar = QtWidgets.QPushButton(frmPesqCliente)
        self.btnAlterar.setGeometry(QtCore.QRect(450, 450, 101, 51))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".../../Imagens/editar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAlterar.setIcon(icon2)
        self.btnAlterar.setIconSize(QtCore.QSize(35, 35))
        self.btnAlterar.setObjectName("btnAlterar")
        #clickk
        self.btnAlterar.clicked.connect(lambda: self.AlterarCliente_Click())

        self.retranslateUi(frmPesqCliente)
        QtCore.QMetaObject.connectSlotsByName(frmPesqCliente)

        self.PesquisarTodosClientes()

    def retranslateUi(self, frmPesqCliente):
        _translate = QtCore.QCoreApplication.translate
        frmPesqCliente.setWindowTitle(_translate("frmPesqCliente", "Lista de Cliente", None))
        item = self.gridCliente.horizontalHeaderItem(0)
        item.setText(_translate("frmPesqCliente", "Código", None))
        item = self.gridCliente.horizontalHeaderItem(1)
        item.setText(_translate("frmPesqCliente", "Nome", None))
        item = self.gridCliente.horizontalHeaderItem(2)
        item.setText(_translate("frmPesqCliente", "CPF", None))
        item = self.gridCliente.horizontalHeaderItem(3)
        item.setText(_translate("frmPesqCliente", "Endereço", None))
        item = self.gridCliente.horizontalHeaderItem(4)
        item.setText(_translate("frmPesqCliente", "Email", None))
        item = self.gridCliente.horizontalHeaderItem(5)
        item.setText(_translate("frmPesqCliente", "Telefone", None))
        self.cbPesquisa.setItemText(0, _translate("frmPesqCliente", "Código", None))
        self.cbPesquisa.setItemText(1, _translate("frmPesqCliente", "Nome", None))
        self.cbPesquisa.setItemText(2, _translate("frmPesqCliente", "CPF", None))
        self.label.setText(_translate("frmPesqCliente", "Selecione o Tipo de Pesquisa:", None))
        self.btnPesquisar.setText(_translate("frmPesqCliente", "Pesquisar", None))
        self.lblTotal.setText(_translate("frmPesqCliente", "TextLabel", None))
        self.btnExcluir.setText(_translate("frmPesqCliente", "Excluir", None))
        self.btnAlterar.setText(_translate("frmPesqCliente", "Alterar", None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmPesqCliente = QtWidgets.QDialog()
    ui = Ui_frmPesqCliente()
    ui.setupUi(frmPesqCliente)
    frmPesqCliente.show()
    sys.exit(app.exec_())
