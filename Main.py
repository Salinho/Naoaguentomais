from PyQt5.QtWidgets import QApplication, QMainWindow
from View.FrmPrincipal import *
import sys



if __name__ == "__main__":
    app = QApplication(sys.argv)
    FrmPrincipal = QMainWindow()
    ui = Ui_FrmPrincipal()
    ui.setupUi(FrmPrincipal)
    FrmPrincipal.show()
    sys.exit(app.exec_())
