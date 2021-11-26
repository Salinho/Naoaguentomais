from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from Controller.ClienteCTR import ClienteCTR
from View.FrmCliente import Ui_frmCliente

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

class Ui_frmPesqCliente(object):
    def AlterarCliente_Click(self):
        linha = self.gridCliente.currentItem().row()
        codigoCli = self.gridCliente.item(linha, 0).text()
        nome = self.gridCliente.item(linha, 1).text()
        cpf = self.gridCliente.item(linha, 2).text()
        endereco = self.gridCliente.item(linha, 3).text()
        email = self.gridCliente.item(linha, 4).text()
        telefone = self.gridCliente.item(linha, 5).text()

        self.frmCliente = QtGui.QMainWindow()
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

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Cliente Excluído!")
        #msg.setInformativeText("This is additional information")
        msg.setWindowTitle("Excluir Cliente")
        #msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok)
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

        self.edtPesquisa.setText('')

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



    def setupUi(self, frmPesqCliente):
        frmPesqCliente.setObjectName(_fromUtf8("frmPesqCliente"))

        #DESABILITAR REDIMENCIONAMENTO DA JANELA
        frmPesqCliente.setFixedSize(651, 504)

        #GRID CLIENTE######
        self.gridCliente = QtGui.QTableWidget(frmPesqCliente)
        self.gridCliente.setGeometry(QtCore.QRect(20, 150, 621, 291))
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

        #EDT PESQUISAR#########3
        self.edtPesquisa = QtGui.QLineEdit(frmPesqCliente)
        self.edtPesquisa.setGeometry(QtCore.QRect(190, 60, 451, 20))
        self.edtPesquisa.setObjectName(_fromUtf8("edtPesquisa"))
        self.cbPesquisa = QtGui.QComboBox(frmPesqCliente)
        self.cbPesquisa.setGeometry(QtCore.QRect(20, 60, 161, 22))
        self.cbPesquisa.setObjectName(_fromUtf8("cbPesquisa"))
        self.cbPesquisa.addItem(_fromUtf8(""))
        self.cbPesquisa.addItem(_fromUtf8(""))
        self.cbPesquisa.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(frmPesqCliente)
        self.label.setGeometry(QtCore.QRect(20, 30, 271, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        #BTN PESQUISAR #########
        self.btnPesquisar = QtGui.QPushButton(frmPesqCliente)
        self.btnPesquisar.setGeometry(QtCore.QRect(530, 92, 111, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Imagens/lupa.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisar.setIcon(icon)
        self.btnPesquisar.setIconSize(QtCore.QSize(30, 30))
        self.btnPesquisar.setObjectName(_fromUtf8("btnPesquisar"))
        #BTN PESQUISAR CLICK #
        self.btnPesquisar.clicked.connect(lambda: self.PesquisarCliente(self.edtPesquisa.text(), self.cbPesquisa.currentText()))

        self.lblTotal = QtGui.QLabel(frmPesqCliente)
        self.lblTotal.setGeometry(QtCore.QRect(20, 450, 111, 16))
        self.lblTotal.setObjectName(_fromUtf8("lblTotal"))

        #BTN EXCLUIR
        self.btnExcluir = QtGui.QPushButton(frmPesqCliente)
        self.btnExcluir.setGeometry(QtCore.QRect(554, 450, 91, 51))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Imagens/excluir.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExcluir.setIcon(icon1)
        self.btnExcluir.setIconSize(QtCore.QSize(30, 30))
        self.btnExcluir.setObjectName(_fromUtf8("btnExcluir"))
        #BTN EXCLUIR CLICK
        self.btnExcluir.clicked.connect(lambda: self.ExcluirCliente_Click())

        #BTN ALTERAR##########
        self.btnAlterar = QtGui.QPushButton(frmPesqCliente)
        self.btnAlterar.setGeometry(QtCore.QRect(450, 450, 101, 51))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Imagens/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAlterar.setIcon(icon2)
        self.btnAlterar.setIconSize(QtCore.QSize(35, 35))
        self.btnAlterar.setObjectName(_fromUtf8("btnAlterar"))
        #BTN ALTERAR CLICK###
        self.btnAlterar.clicked.connect(lambda: self.AlterarCliente_Click())

        self.retranslateUi(frmPesqCliente)
        QtCore.QMetaObject.connectSlotsByName(frmPesqCliente)

        self.PesquisarTodosClientes()

    def retranslateUi(self, frmPesqCliente):
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
    app = QtGui.QApplication(sys.argv)
    frmPesqCliente = QtGui.QDialog()
    ui = Ui_frmPesqCliente()
    ui.setupUi(frmPesqCliente)
    frmPesqCliente.show()
    sys.exit(app.exec_())

