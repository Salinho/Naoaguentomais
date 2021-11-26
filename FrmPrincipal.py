from PyQt4 import QtCore, QtGui
from View.FrmCliente import Ui_frmCliente
from View.frmPesqCliente import Ui_frmPesqCliente
from View.FrmVeiculos import Ui_frmVeiculos
from View.frmPesqVeiculos import Ui_frmPesqVeiculos
from View.FrmAluguel import Ui_FrmAluguel
from View.FrmPesqAluguel import Ui_FrmPesqAluguel

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

class Ui_FrmPrincipal(object):
    #BTN ALUGUEL.CLICK
    def FrmAluguel_Click(self):
        self.frmAluguel = QtGui.QMainWindow()
        self.ui = Ui_FrmAluguel()
        self.ui.setupUi(self.frmAluguel)
        self.frmAluguel.show()

	#BTNCLIENTE.CLICK
    def FrmCliente_Click(self):
        self.frmCliente = QtGui.QMainWindow()
        self.ui = Ui_frmCliente()
        self.ui.setupUi(self.frmCliente, 'inserir', 0)
        self.frmCliente.show()

    #BTNVEICULO.CLICK
    def FrmVeiculo_Click(self):
        self.frmVeiculo = QtGui.QMainWindow()
        self.ui = Ui_frmVeiculos()
        self.ui.setupUi(self.frmVeiculo, 'inserir', 0)
        self.frmVeiculo.show()

    #BTN LISTAR TODOS CLIENTES CLICK
    def btnListarCliente_Click(self):
        self.frmPesqCliente = QtGui.QMainWindow()
        self.ui = Ui_frmPesqCliente()
        self.ui.setupUi(self.frmPesqCliente)
        self.frmPesqCliente.show()

    #BTN LISTAR TODOS VEICULOS CLICK
    def btnListarVeiculo_Click(self):
        self.frmPesqVeiculo = QtGui.QMainWindow()
        self.ui = Ui_frmPesqVeiculos()
        self.ui.setupUi(self.frmPesqVeiculo)
        self.frmPesqVeiculo.show()

    #BTN LISTAR TODOS ALUGUEIS CLICK
    def btnListarAluguel_Click(self):
        self.frmPesqAluguel = QtGui.QMainWindow()
        self.ui = Ui_FrmPesqAluguel()
        self.ui.setupUi(self.frmPesqAluguel)
        self.frmPesqAluguel.show()
        
    
    def setupUi(self, FrmPrincipal):
        FrmPrincipal.setObjectName(_fromUtf8("FrmPrincipal"))
        FrmPrincipal.setWindowModality(QtCore.Qt.NonModal)

        #DESABILITAR REDIMENCIONAMENTO DA JANELA
        FrmPrincipal.setFixedSize(803, 422)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Imagens/FrmIcon_Car.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrmPrincipal.setWindowIcon(icon)
        FrmPrincipal.setAutoFillBackground(True)
        FrmPrincipal.setIconSize(QtCore.QSize(40, 40))
        self.centralwidget = QtGui.QWidget(FrmPrincipal)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.columnView = QtGui.QColumnView(self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(0, 0, 801, 101))
        self.columnView.setObjectName(_fromUtf8("columnView"))

        #BTN ALUGAR #############
        self.btnAlugar = QtGui.QPushButton(self.centralwidget)
        self.btnAlugar.setGeometry(QtCore.QRect(10, 10, 131, 81))
        self.btnAlugar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAlugar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnAlugar.setAutoFillBackground(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Imagens/btnAlugaVeiculo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAlugar.setIcon(icon1)
        self.btnAlugar.setIconSize(QtCore.QSize(40, 40))
        self.btnAlugar.setObjectName(_fromUtf8("btnAlugar"))
        ##BTN ALUGAR CLICK EVENT ######
        self.btnAlugar.clicked.connect(self.FrmAluguel_Click)

        #BTN CLIENTE ###################
        self.btnCliente = QtGui.QPushButton(self.centralwidget)
        self.btnCliente.setGeometry(QtCore.QRect(140, 10, 131, 81))
        self.btnCliente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Imagens/btnCadCli.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCliente.setIcon(icon2)
        self.btnCliente.setIconSize(QtCore.QSize(30, 30))
        self.btnCliente.setObjectName(_fromUtf8("btnCliente"))
        ##  BTNCLIENTE CLICK EVENT  ###
        self.btnCliente.clicked.connect(self.FrmCliente_Click)

        #BTN VEICULO #################
        self.btnVeiculo = QtGui.QPushButton(self.centralwidget)
        self.btnVeiculo.setGeometry(QtCore.QRect(270, 10, 131, 81))
        self.btnVeiculo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Imagens/FrmIcon_Car.png")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.btnVeiculo.setIcon(icon3)
        self.btnVeiculo.setIconSize(QtCore.QSize(40, 40))
        self.btnVeiculo.setObjectName(_fromUtf8("btnVeiculo"))
        #BTN VEICULO CLICK EVENT ##
        self.btnVeiculo.clicked.connect(self.FrmVeiculo_Click)

        #BTN LISTAR CLIENTE #####################
        self.btnListCliente = QtGui.QPushButton(self.centralwidget)
        self.btnListCliente.setGeometry(QtCore.QRect(400, 10, 131, 81))
        self.btnListCliente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("Imagens/btnListCliente.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("Imagens/btnListClientes.png")), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.btnListCliente.setIcon(icon4)
        self.btnListCliente.setIconSize(QtCore.QSize(30, 30))
        self.btnListCliente.setObjectName(_fromUtf8("btnListCliente"))
        #BTN LISTAR CLIENTE CLICK ##
        self.btnListCliente.clicked.connect(self.btnListarCliente_Click)

        #BTN LISTAR VEICULO ################
        self.btnListVeiculo = QtGui.QPushButton(self.centralwidget)
        self.btnListVeiculo.setGeometry(QtCore.QRect(530, 10, 131, 81))
        self.btnListVeiculo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("Imagens/btnListVeiculo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnListVeiculo.setIcon(icon5)
        self.btnListVeiculo.setIconSize(QtCore.QSize(30, 30))
        self.btnListVeiculo.setObjectName(_fromUtf8("btnListVeiculo"))
        #BTN LISTAR VEICULO CLICK
        self.btnListVeiculo.clicked.connect(self.btnListarVeiculo_Click)

        #BTN LISTAR ALUGUEL
        self.btnListAluguel = QtGui.QPushButton(self.centralwidget)
        self.btnListAluguel.setGeometry(QtCore.QRect(660, 10, 131, 81))
        self.btnListAluguel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("Imagens/btnListAluguel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnListAluguel.setIcon(icon6)
        self.btnListAluguel.setIconSize(QtCore.QSize(30, 30))
        self.btnListAluguel.setObjectName(_fromUtf8("btnListAluguel"))
        #BTN LISTAR ALUGUEL CLICK #
        self.btnListAluguel.clicked.connect(self.btnListarAluguel_Click)

        self.lbImg = QtGui.QLabel(self.centralwidget)
        self.lbImg.setGeometry(QtCore.QRect(10, 110, 781, 301))
        self.lbImg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lbImg.setFrameShape(QtGui.QFrame.WinPanel)
        self.lbImg.setText(_fromUtf8(""))
        self.lbImg.setPixmap(QtGui.QPixmap(_fromUtf8("Imagens/BGImg.png")))
        self.lbImg.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.lbImg.setObjectName(_fromUtf8("lbImg"))
        FrmPrincipal.setCentralWidget(self.centralwidget)
        self.actionCliente = QtGui.QAction(FrmPrincipal)
        self.actionCliente.setObjectName(_fromUtf8("actionCliente"))
        self.actionVe_culo = QtGui.QAction(FrmPrincipal)
        self.actionVe_culo.setObjectName(_fromUtf8("actionVe_culo"))
        self.actionAlugar = QtGui.QAction(FrmPrincipal)
        self.actionAlugar.setObjectName(_fromUtf8("actionAlugar"))
        self.actionCliente_2 = QtGui.QAction(FrmPrincipal)
        self.actionCliente_2.setObjectName(_fromUtf8("actionCliente_2"))
        self.actionVe_culos = QtGui.QAction(FrmPrincipal)
        self.actionVe_culos.setObjectName(_fromUtf8("actionVe_culos"))
        self.actionAlugueis = QtGui.QAction(FrmPrincipal)
        self.actionAlugueis.setObjectName(_fromUtf8("actionAlugueis"))
        self.actionSair = QtGui.QAction(FrmPrincipal)
        self.actionSair.setObjectName(_fromUtf8("actionSair"))

        self.retranslateUi(FrmPrincipal)
        QtCore.QMetaObject.connectSlotsByName(FrmPrincipal)

    def retranslateUi(self, FrmPrincipal):
        FrmPrincipal.setWindowTitle(_translate("FrmPrincipal", "Locadora de Veículos", None))
        self.btnAlugar.setText(_translate("FrmPrincipal", "Alugar Veículo", None))
        self.btnCliente.setText(_translate("FrmPrincipal", "Cadastrar Cliente", None))
        self.btnVeiculo.setText(_translate("FrmPrincipal", "Cadastrar Veículo", None))
        self.btnListCliente.setText(_translate("FrmPrincipal", "Listar Clientes", None))
        self.btnListVeiculo.setText(_translate("FrmPrincipal", "Listar Veículos", None))
        self.btnListAluguel.setText(_translate("FrmPrincipal", "Listar Alugueis", None))
        self.actionCliente.setText(_translate("FrmPrincipal", "Cliente", None))
        self.actionVe_culo.setText(_translate("FrmPrincipal", "Veículo", None))
        self.actionAlugar.setText(_translate("FrmPrincipal", "Alugar Veículo", None))
        self.actionCliente_2.setText(_translate("FrmPrincipal", "Clientes", None))
        self.actionVe_culos.setText(_translate("FrmPrincipal", "Veículos", None))
        self.actionAlugueis.setText(_translate("FrmPrincipal", "Alugueis", None))
        self.actionSair.setText(_translate("FrmPrincipal", "Sair", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FrmPrincipal = QtGui.QMainWindow()
    ui = Ui_FrmPrincipal()
    ui.setupUi(FrmPrincipal)
    FrmPrincipal.show()
    sys.exit(app.exec_())

