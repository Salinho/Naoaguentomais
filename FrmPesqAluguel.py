from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from Controller.AluguelCTR import AluguelCTR

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

class Ui_FrmPesqAluguel(object):
    def DevolverVeiculo(self):
        linha = self.gridAluguel.currentItem().row()
        codigoAlug = self.gridAluguel.item(linha, 0).text()
        dataDevol = self.edtDevolucao.text()
        valorMulta = self.edtMulta.text()
        kmSaida = self.edtSaida.text()

        aluguelCTR = AluguelCTR
        aluguelCTR.DevolverVeiculo(codigoAlug, dataDevol, valorMulta, kmSaida)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Veículo devolvido!")
        msg.setWindowTitle("Devolver Veículo")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

        self.edtDevolucao.setText('')
        self.edtMulta.setText('')
        self.edtSaida.setText('')

    def PesquisarAluguel(self, valor, tipo):
        if (valor == ''):
            self.PesquisarTodosAluguel()
        else:
            aluguel = AluguelCTR
            query = aluguel.PesquisarAluguel(valor, tipo)

            while (self.gridAluguel.rowCount() > 0):
                self.gridAluguel.removeRow(0)

            row = 0
            while query.next():
                self.gridAluguel.insertRow(row)
                codigoAlug = QTableWidgetItem(str(query.value(0)))
                nomecliente = QTableWidgetItem(str(query.value(10)))
                dataAlug = QTableWidgetItem(str(query.value(1)))
                dataPrazo = QTableWidgetItem(str(query.value(2)))
                dataDevolucao = QTableWidgetItem(str(query.value(3)))
                valorAluguel = QTableWidgetItem(str(query.value(4)))
                valorMulta = QTableWidgetItem(str(query.value(5)))
                kmEntrada = QTableWidgetItem(str(query.value(6)))
                kmSaida = QTableWidgetItem(str(query.value(7)))

                self.gridAluguel.setItem(row, 0, codigoAlug)
                self.gridAluguel.setItem(row, 1, nomecliente)
                self.gridAluguel.setItem(row, 2, dataAlug)
                self.gridAluguel.setItem(row, 3, dataPrazo)
                self.gridAluguel.setItem(row, 4, dataDevolucao)
                self.gridAluguel.setItem(row, 5, valorAluguel)
                self.gridAluguel.setItem(row, 6, valorMulta)
                self.gridAluguel.setItem(row, 7, kmEntrada)
                self.gridAluguel.setItem(row, 8, kmSaida)

                row = row + 1

        self.edtPesquisa.setText('')

    def PesquisarTodosAluguel(self):
        aluguel = AluguelCTR
        query = aluguel.PesquisarTodosAluguel()

        while (self.gridAluguel.rowCount() > 0):
                self.gridAluguel.removeRow(0)

        row = 0
        while query.next():
            self.gridAluguel.insertRow(row)
            codigoAlug = QTableWidgetItem(str(query.value(0)))
            nomecliente = QTableWidgetItem(str(query.value(10)))
            dataAlug = QTableWidgetItem(str(query.value(1)))
            dataPrazo = QTableWidgetItem(str(query.value(2)))
            dataDevolucao = QTableWidgetItem(str(query.value(3)))
            valorAluguel = QTableWidgetItem(str(query.value(4)))
            valorMulta = QTableWidgetItem(str(query.value(5)))
            kmEntrada = QTableWidgetItem(str(query.value(6)))
            kmSaida = QTableWidgetItem(str(query.value(7)))

            self.gridAluguel.setItem(row, 0, codigoAlug)
            self.gridAluguel.setItem(row, 1, nomecliente)
            self.gridAluguel.setItem(row, 2, dataAlug)
            self.gridAluguel.setItem(row, 3, dataPrazo)
            self.gridAluguel.setItem(row, 4, dataDevolucao)
            self.gridAluguel.setItem(row, 5, valorAluguel)
            self.gridAluguel.setItem(row, 6, valorMulta)
            self.gridAluguel.setItem(row, 7, kmEntrada)
            self.gridAluguel.setItem(row, 8, kmSaida)


            row = row + 1

    def setupUi(self, FrmPesqAluguel):
        FrmPesqAluguel.setObjectName(_fromUtf8("FrmPesqAluguel"))
        FrmPesqAluguel.setFixedSize(519, 365)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Imagens/btnListAluguel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrmPesqAluguel.setWindowIcon(icon)
        self.groupBox = QtGui.QGroupBox(FrmPesqAluguel)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 501, 71))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.cbPesquisa = QtGui.QComboBox(self.groupBox)
        self.cbPesquisa.setGeometry(QtCore.QRect(10, 40, 161, 22))
        self.cbPesquisa.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cbPesquisa.setObjectName(_fromUtf8("cbPesquisa"))
        self.cbPesquisa.addItem(_fromUtf8(""))
        self.cbPesquisa.addItem(_fromUtf8(""))
        self.cbPesquisa.addItem(_fromUtf8(""))
        self.cbPesquisa.addItem(_fromUtf8(""))
        self.edtPesquisa = QtGui.QLineEdit(self.groupBox)
        self.edtPesquisa.setGeometry(QtCore.QRect(180, 40, 221, 20))
        self.edtPesquisa.setObjectName(_fromUtf8("edtPesquisa"))

        #BTN PESQUISA
        self.btnPesquisa = QtGui.QPushButton(self.groupBox)
        self.btnPesquisa.setGeometry(QtCore.QRect(404, 10, 91, 51))
        self.btnPesquisa.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Imagens/lupa.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisa.setIcon(icon1)
        self.btnPesquisa.setIconSize(QtCore.QSize(30, 30))
        self.btnPesquisa.setObjectName(_fromUtf8("btnPesquisa"))
        #BTN PESQUISAR CLICK #
        self.btnPesquisa.clicked.connect(lambda: self.PesquisarAluguel(self.edtPesquisa.text(), self.cbPesquisa.currentText()))

        self.gridAluguel = QtGui.QTableWidget(FrmPesqAluguel)
        self.gridAluguel.setGeometry(QtCore.QRect(10, 80, 501, 192))
        self.gridAluguel.setObjectName(_fromUtf8("gridAluguel"))
        self.gridAluguel.setColumnCount(9)
        self.gridAluguel.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.gridAluguel.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.gridAluguel.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.gridAluguel.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.gridAluguel.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.gridAluguel.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.gridAluguel.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.gridAluguel.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.gridAluguel.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.gridAluguel.setHorizontalHeaderItem(8, item)
        #AJUSTANDO MODO DE SELEÇÃO - Uma linha por vez, desalitar editar
        self.gridAluguel.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.gridAluguel.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.gridAluguel.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)

        self.groupBox_2 = QtGui.QGroupBox(FrmPesqAluguel)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 280, 501, 80))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))

        #BTN DEVOLVER
        self.btnDevolver = QtGui.QPushButton(self.groupBox_2)
        self.btnDevolver.setGeometry(QtCore.QRect(394, 10, 101, 61))
        self.btnDevolver.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Imagens/return.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDevolver.setIcon(icon2)
        self.btnDevolver.setIconSize(QtCore.QSize(30, 30))
        self.btnDevolver.setObjectName(_fromUtf8("btnDevolver"))
        #btn DEVOLVER click
        self.btnDevolver.clicked.connect(lambda: self.DevolverVeiculo())


        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.edtDevolucao = QtGui.QLineEdit(self.groupBox_2)
        self.edtDevolucao.setGeometry(QtCore.QRect(10, 40, 113, 20))
        self.edtDevolucao.setObjectName(_fromUtf8("edtDevolucao"))
        self.edtMulta = QtGui.QLineEdit(self.groupBox_2)
        self.edtMulta.setGeometry(QtCore.QRect(130, 40, 113, 20))
        self.edtMulta.setObjectName(_fromUtf8("edtMulta"))
        self.edtSaida = QtGui.QLineEdit(self.groupBox_2)
        self.edtSaida.setGeometry(QtCore.QRect(250, 40, 113, 20))
        self.edtSaida.setObjectName(_fromUtf8("edtSaida"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(130, 20, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(250, 20, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(FrmPesqAluguel)
        QtCore.QMetaObject.connectSlotsByName(FrmPesqAluguel)

        self.PesquisarTodosAluguel()

    def retranslateUi(self, FrmPesqAluguel):
        FrmPesqAluguel.setWindowTitle(_translate("FrmPesqAluguel", "Lista de Aluguéis", None))
        self.groupBox.setTitle(_translate("FrmPesqAluguel", "Selecione o Tipo de Pesquisa", None))
        self.cbPesquisa.setItemText(0, _translate("FrmPesqAluguel", "Código Aluguel", None))
        self.cbPesquisa.setItemText(1, _translate("FrmPesqAluguel", "Código Cliente", None))
        self.cbPesquisa.setItemText(2, _translate("FrmPesqAluguel", "Código Veículo", None))
        self.cbPesquisa.setItemText(3, _translate("FrmPesqAluguel", "Nome Cliente", None))
        self.btnPesquisa.setText(_translate("FrmPesqAluguel", "Pesquisar", None))
        item = self.gridAluguel.horizontalHeaderItem(0)
        item.setText(_translate("FrmPesqAluguel", "Código Aluguel", None))
        item = self.gridAluguel.horizontalHeaderItem(1)
        item.setText(_translate("FrmPesqAluguel", "Nome Cliente", None))
        item = self.gridAluguel.horizontalHeaderItem(2)
        item.setText(_translate("FrmPesqAluguel", "Data Aluguel", None))
        item = self.gridAluguel.horizontalHeaderItem(3)
        item.setText(_translate("FrmPesqAluguel", "Data Prazo", None))
        item = self.gridAluguel.horizontalHeaderItem(4)
        item.setText(_translate("FrmPesqAluguel", "Data Devolução", None))
        item = self.gridAluguel.horizontalHeaderItem(5)
        item.setText(_translate("FrmPesqAluguel", "Valor Aluguel", None))
        item = self.gridAluguel.horizontalHeaderItem(6)
        item.setText(_translate("FrmPesqAluguel", "Valor Multa", None))
        item = self.gridAluguel.horizontalHeaderItem(7)
        item.setText(_translate("FrmPesqAluguel", "Km Entrada", None))
        item = self.gridAluguel.horizontalHeaderItem(8)
        item.setText(_translate("FrmPesqAluguel", "Km Saída", None))
        self.groupBox_2.setTitle(_translate("FrmPesqAluguel", "Devolver Veículo", None))
        self.btnDevolver.setText(_translate("FrmPesqAluguel", "Devolver", None))
        self.label.setText(_translate("FrmPesqAluguel", "Data Devolução", None))
        self.label_2.setText(_translate("FrmPesqAluguel", "Multa", None))
        self.label_3.setText(_translate("FrmPesqAluguel", "Km Saída", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FrmPesqAluguel = QtGui.QDialog()
    ui = Ui_FrmPesqAluguel()
    ui.setupUi(FrmPesqAluguel)
    FrmPesqAluguel.show()
    sys.exit(app.exec_())

